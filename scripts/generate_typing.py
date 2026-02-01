import argparse
import glob
import importlib
import inspect
import re
from collections import defaultdict
from types import ModuleType
from typing import Any


class PyiFile:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.cls_name: str | None = None
        self.methods: list[list[Any]] = []
        self.types: set[str] = set()

    def add_class(self, name: str):
        self.cls_name = name

    def add_method(
        self,
        name: str,
        params: dict[str, dict],
        retval: str | None,
        decorator: str | None = None,
        awaitable: bool = False,
    ):
        if retval:
            retval = retval.replace("HTTPHeaderDict", "CIMultiDictProxy")
            rtypes = re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\b(?!\s*\()", retval)
            if retval.startswith("tuple"):
                retval = f"tuple[{', '.join(rtypes)}]"
            if awaitable:
                retval = f"Awaitable[{retval}]"
                rtypes.append("Awaitable")
            self.types.update(rtypes)
        if params:
            # if "kwargs" in params:
            # ignore kwargs
            #    del params["kwargs"]

            for param, pvd in params.items():
                if param == "kwargs":
                    pvd["type"] = "Any"
                    pvd["required"] = False
                if pvd:
                    rtypes = re.findall(
                        r"\b([A-Za-z_][A-Za-z0-9_]*)\b(?!\s*\()", pvd.get("type", "Any")
                    )
                    self.types.update(rtypes)

        self.methods.append([name, params, retval, decorator])

    def add_property(self, name: str, type: str) -> None:
        self.add_method(name, {"self": {}}, type, "@property")
        self.add_method(
            name,
            {"self": {}, name: {"required": True, "type": type}},
            None,
            f"@{name}.setter",
        )

    def save(self) -> None:
        with open(self.path, "w") as fp:

            def write_ln(text: str) -> None:
                fp.write(text)
                fp.write("\n")

            write_ln("\n".join(self._get_imports()))
            write_ln("")

            write_ln(f"class {self.cls_name}:")
            for name, params, retval, decorator in self.methods:
                params_typing = []

                for pn, v in params.items():
                    if pn == "kwargs":
                        # process keywords after kwargs
                        params_typing.append("*")
                        continue
                    if v.get("type"):
                        pt = ": " + v.get("type")
                    else:
                        pt = ""
                    if "default" in v:
                        if v["default"] is None:
                            pt += " | None = None"
                        else:
                            pt += f" = {v['default']}"
                    elif "required" in v and not v["required"]:
                        pt += " = ..."

                    params_typing.append(f"{pn}{pt}")

                params_typing_str = ", ".join(params_typing)
                if decorator:
                    write_ln(f"    {decorator}")
                write_ln(f"    def {name}({params_typing_str}) -> {retval}: ...")

    def _get_imports(self) -> list[str]:
        ret = []
        for itype in self.types:
            if itype in (
                "None",
                "int",
                "float",
                "str",
                "bytes",
                "bool",
                "dict",
                "list",
                "tuple",
            ):
                continue
            if itype == self.cls_name:
                continue
            if itype == "CIMultiDictProxy":
                ret.append("from multidict import CIMultiDictProxy")
            elif itype == "Any":
                ret.append("from typing import Any")
            elif itype == "Awaitable":
                ret.append("from typing import Awaitable")
            elif itype == "datetime":
                ret.append("from datetime import datetime")
            elif itype == "ClientTimeout":
                ret.append("from aiohttp import ClientTimeout")
            elif itype == "ApiClient":
                ret.append("from kubernetes_asyncio.client.api_client import ApiClient")
            else:
                ret.append(f"from kubernetes_asyncio.client.models import {itype}")
        ret.sort()
        return ret


def map_types(type: str) -> str:
    if "object" in type:
        type = type.replace("object", "Any")
    if type.startswith("dict("):
        return "dict[" + type[5:-1] + "]"
    return type


def module_to_path(file: str) -> str:
    return file.replace(".", "/")


def path_to_module(file: str) -> str:
    return file.replace("/", ".")


def get_defined_classes(module: ModuleType) -> list[tuple]:
    return [
        (name, cls)
        for name, cls in inspect.getmembers(module, inspect.isclass)
        if cls.__module__ == module.__name__
    ]


def params_from_method_doc(
    doc: str,
) -> tuple[dict[str, dict[str, str | bool]], str | None]:
    params: defaultdict[str, dict[str, str | bool]] = defaultdict(dict)
    rettype = None

    for line in doc.splitlines():
        rparam = re.search(r"^:param (\S+):.*?(\(required\))?$", line)
        if rparam:
            params[rparam.group(1)]["required"] = rparam.group(2) == "(required)"
            continue

        rtype = re.search(r"^:type (\S+): (\S*)(, optional)?$", line)
        if rtype:
            params[rtype.group(1)]["type"] = map_types(rtype.group(2))
            continue

        rrtype = re.search(r"^:rtype: (.*)$", line)
        if rrtype:
            rettype = map_types(str(rrtype.group(1)))

    if "_request_timeout" in params:
        params["_request_timeout"]["type"] = (
            "None | int | float | tuple[float, float] | ClientTimeout"
        )

    return dict(params), rettype


def list_modules(path: str) -> list[str]:
    files = glob.glob(f"{module_to_path(path)}/*.py")
    return [path_to_module(file[:-3]) for file in files if file != "__init__.py"]


def gen_api_typing(module: str) -> None:
    path_pyi = module_to_path(module) + ".pyi"
    print(f"Generating {path_pyi}...")
    pyi = PyiFile(path_pyi)

    mod = importlib.import_module(module)
    classes = get_defined_classes(mod)

    for cls_name, cls in classes:
        pyi.add_class(cls_name)

        for method_name, method in inspect.getmembers(
            cls, predicate=inspect.isfunction
        ):
            sig = inspect.signature(method)
            method_params: dict[str, dict] = {}
            retval = None
            if method_name == "__init__":
                method_params = {
                    "self": {},
                    "api_client": {
                        "required": False,
                        "type": "ApiClient",
                        "default": None,
                    },
                }
                retval = None
            else:
                doc = inspect.getdoc(method)
                if doc:
                    params, retval = params_from_method_doc(doc)
                    method_params = {}
                    for param_name in sig.parameters.keys():
                        method_params[param_name] = params.get(param_name, {})

                    for param_name in params.keys():
                        if param_name not in method_params:
                            method_params[param_name] = params.get(param_name, {})

            pyi.add_method(
                method_name,
                method_params,
                retval,
                awaitable=not method_name.startswith("__"),
            )

    pyi.save()


def gen_model_typing(module: str) -> None:
    path_pyi = module_to_path(module) + ".pyi"
    print(f"Generating {path_pyi}...")
    pyi = PyiFile(path_pyi)

    mod = importlib.import_module(module)
    classes = get_defined_classes(mod)

    for cls_name, cls in classes:
        pyi.add_class(cls_name)

        openapi_types = cls.openapi_types

        # add methods
        for method_name, method in inspect.getmembers(
            cls, predicate=inspect.isfunction
        ):
            sig = inspect.signature(method)
            params: dict[str, dict] = {}
            retval: str | None = None
            if method_name == "to_dict":
                params["serialize"] = {"required": False, "type": "bool"}
                retval = "dict[str, Any]"
            elif method_name in ("to_str", "__repr__"):
                retval = "str"
            elif method_name in ("__eq__", "__ne__"):
                params["other"] = {"required": True, "type": "Any"}
                retval = "bool"
            elif method_name == "__init__":
                for param_name in sig.parameters.keys():
                    if param_name in openapi_types:
                        params[param_name] = {
                            "required": False,
                            "type": map_types(openapi_types[param_name]),
                        }
                    elif param_name == "local_vars_configuration":
                        params[param_name] = {
                            "required": False,
                            "type": "Any",
                        }
                retval = "None"
            else:
                doc = inspect.getdoc(method)
                if doc:
                    params, retval = params_from_method_doc(doc)
                else:
                    continue

            method_params = {}
            for param_name in sig.parameters.keys():
                method_params[param_name] = params.get(param_name, {})
                if sig.parameters[param_name].default != inspect.Parameter.empty:
                    method_params[param_name]["default"] = sig.parameters[
                        param_name
                    ].default

            pyi.add_method(method_name, method_params, retval)

        # add model properties
        for method_name, method_prop in inspect.getmembers(
            cls, predicate=inspect.isdatadescriptor
        ):
            if not isinstance(method_prop, property):
                continue
            assert method_prop.fset and method_prop.fget
            sig = inspect.signature(method_prop.fset)
            assert len(sig.parameters) == 2
            assert list(sig.parameters.keys())[-1] == method_name
            pyi.add_property(method_name, map_types(openapi_types[method_name]))

    pyi.save()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?")
    args = parser.parse_args()

    files: list[str] = []
    if args.file:
        files.append(args.file)
    else:
        files = list_modules("kubernetes_asyncio.client.api") + list_modules(
            "kubernetes_asyncio.client.models"
        )

    for file in files:
        if file.endswith("__init__"):
            continue

        if file.startswith("kubernetes_asyncio.client.api."):
            gen_api_typing(file)
        elif file.startswith("kubernetes_asyncio.client.models."):
            gen_model_typing(file)
        else:
            print("Ignore", file)


if __name__ == "__main__":
    main()
