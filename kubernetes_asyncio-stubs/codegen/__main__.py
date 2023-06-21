import collections
import json
import keyword
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import inflection

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_FILE = ROOT_DIR / ".." / "scripts" / "swagger.json"
STUBS_DIR = ROOT_DIR / "kubernetes_asyncio-stubs"
CLIENT_STUBS_DIR = STUBS_DIR / "client"
MODELS_STUBS_DIR = CLIENT_STUBS_DIR / "models"
API_STUBS_DIR = CLIENT_STUBS_DIR / "api"
EXT_DIR = ROOT_DIR / "kubernetes_asyncio_ext"

schema = json.load(open(SCHEMA_FILE))

for dir in [STUBS_DIR, EXT_DIR]:
    shutil.rmtree(dir, ignore_errors=True)
shutil.copytree(ROOT_DIR / "codegen" / "base", ROOT_DIR, dirs_exist_ok=True)


class CodegenBuf:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open(mode="a")
        self.indent = 0

    def writeln(self, s: str = ""):
        print(f"{self.indent * '    '}{s}", file=self.file)

    def start_block(self, s: str):
        self.writeln(f"{s}:")
        self.indent += 1

    def end_block(self):
        self.indent -= 1


def make_class_name(s: str):
    return inflection.camelize("".join(s[0].upper() + s[1:] for s in s.split(".")))


def make_file_name(s: str):
    return "_".join(inflection.underscore(s) for s in s.split("."))


def make_type_name(
    config: dict[str, Any], is_optional: bool, use_dict: bool = False
) -> str:
    def inner():
        ty = config.get("type")
        if not ty and "schema" in config:
            ty = config["schema"].get("type")
        if ty:
            if ty == "boolean":
                return "bool"
            elif ty == "string":
                if config.get("format") == "date-time":
                    return "datetime.datetime"
                else:
                    return "str"
            elif ty == "integer":
                return "int"
            elif ty == "number":
                return "float"
            elif ty == "array":
                item_ty = make_type_name(
                    config["items"], is_optional=False, use_dict=use_dict
                )
                return f"list[{item_ty}]"
            elif ty == "object":
                if "additionalProperties" in config:
                    val_ty = make_type_name(
                        config["additionalProperties"],
                        is_optional=False,
                        use_dict=use_dict,
                    )
                    return f"dict[str, {val_ty}]"
                else:
                    return "typing.Any"
            else:
                assert "unknown type"

        ref = config.get("$ref") or config["schema"]["$ref"]
        assert ref.startswith("#/definitions/")
        ref = ref.removeprefix("#/definitions/")
        out = "kubernetes_asyncio.client." + make_class_name(ref)
        if use_dict:
            out += "Dict"
        return out

    if is_optional:
        return f"typing.Optional[{inner()}]"
    return inner()


def make_property_name(s: str, underscored: bool = True):
    if underscored:
        s = inflection.underscore(s)
    else:
        s = s.replace("-", "_")
    s = s.replace("$", "")
    if keyword.iskeyword(s):
        return "_" + s
    return s


@dataclass
class Property:
    name: str
    ty: str
    is_optional: bool

    def __str__(self):
        return f"{self.name}: {self.ty}"

    def arg_str(self) -> str:
        s = str(self)
        if self.is_optional:
            s += " = None"
        return s

    def param_str(self) -> str:
        s = str(self)
        if self.is_optional:
            s += " = ..."
        return s


@dataclass(eq=True, frozen=True)
class Manager:
    name: str
    api_name: str


@dataclass
class ManagerOp:
    name: str
    api_name: str
    required_params: list[Property]
    optional_params: list[Property]
    return_ty: str


# `kubernetes_asyncio.client.models` modules.
for name, config in schema["definitions"].items():
    class_name = make_class_name(name)
    file_name = make_file_name(name)
    required = config.get("required", [])
    props: list[Property] = []
    dict_props: list[Property] = []
    for name, config in config["properties"].items():
        is_optional = name not in required
        props.append(
            Property(
                name=make_property_name(name),
                ty=make_type_name(config, is_optional=is_optional),
                is_optional=is_optional,
            )
        )
        dict_props.append(
            Property(
                name=make_property_name(name, underscored=False),
                ty=make_type_name(config, is_optional=is_optional, use_dict=True),
                is_optional=is_optional,
            )
        )
    buf = CodegenBuf(MODELS_STUBS_DIR / (file_name + ".pyi"))
    buf.writeln("import datetime")
    buf.writeln("import kubernetes_asyncio.client")
    buf.writeln("import kubernetes_asyncio.client.api_client")
    buf.writeln("import typing")
    buf.writeln()
    buf.start_block(f"class {class_name}")
    for prop in props:
        buf.writeln(str(prop))
    buf.writeln()
    params = ", ".join(prop.param_str() for prop in props)
    buf.start_block(f"def __init__(self, *, {params}) -> None")
    buf.writeln("...")
    buf.end_block()
    buf.start_block(f"def to_dict(self) -> {class_name}Dict")
    buf.writeln("...")
    buf.end_block()
    buf.end_block()
    buf.start_block(f"class {class_name}Dict(typing.TypedDict, total=False)")
    for dict_prop in dict_props:
        buf.writeln(str(dict_prop))
    buf.end_block()

# `kubernetes_asyncio.client.models` root.
buf = CodegenBuf(MODELS_STUBS_DIR / "__init__.pyi")
for name in schema["definitions"]:
    buf.writeln(
        f"from kubernetes_asyncio.client.models.{make_file_name(name)} import {make_class_name(name)} as {make_class_name(name)}"
    )
    buf.writeln(
        f"from kubernetes_asyncio.client.models.{make_file_name(name)} import {make_class_name(name)}Dict as {make_class_name(name)}Dict"
    )

# `kubernetes_asyncio.client.api` modules.
apis: collections.defaultdict[str, Any] = collections.defaultdict(list)
for name, config in schema["paths"].items():
    for method in ["get", "put", "post", "delete", "options", "head", "patch"]:
        if method not in config:
            continue
        op = config[method]
        if "parameters" in config:
            op["parameters"] = config["parameters"] + op.get("parameters", [])
        op["path"] = name
        for tag in op.get("tags", []):
            apis[tag].append(op)
managers: collections.defaultdict[Manager, list[ManagerOp]] = collections.defaultdict(
    list
)
for name, api in apis.items():
    class_name = make_class_name(name)
    buf = CodegenBuf(API_STUBS_DIR / f"{name}_api.pyi")
    buf.writeln("import kubernetes_asyncio.client")
    buf.writeln("import typing")
    buf.writeln()
    buf.start_block(f"class {class_name}Api")
    buf.start_block(
        f"def __init__(self, api_client: typing.Optional[kubernetes_asyncio.client.api_client.ApiClient] = ...) -> None"
    )
    buf.writeln("...")
    buf.end_block()
    for op in api:
        name = inflection.underscore(op["operationId"])
        responses = op["responses"]
        if "200" in responses:
            return_ty = make_type_name(responses["200"]["schema"], is_optional=False)
        else:
            return_ty = "None"
        params: list[Property] = []
        for param in op.get("parameters", []):
            is_optional = not param.get("required", False)
            param_name = param["name"]
            i = 2
            while any(param.name == param_name for param in params):
                param_name = param["name"] + str(i)
                i += 1
            params.append(
                Property(
                    name=make_property_name(param_name),
                    ty=make_type_name(param, is_optional=is_optional),
                    is_optional=is_optional,
                )
            )
        required_params, optional_params = [], []
        for param in params:
            if param.is_optional:
                optional_params.append(param)
            else:
                required_params.append(param)
        required_params_str = ", ".join(param.param_str() for param in required_params)
        if required_params_str:
            required_params_str = ", " + required_params_str
        optional_params_str = ", ".join(param.param_str() for param in optional_params)
        if optional_params_str:
            optional_params_str = ", *, " + optional_params_str
        params_str = required_params_str + optional_params_str
        if "x-kubernetes-group-version-kind" in op:
            is_namespaced = any(param.name == "namespace" for param in params)
            gvk = op["x-kubernetes-group-version-kind"]
            [op_name, resource_name] = name.split("_", 1)
            manager = Manager(
                name=make_class_name(
                    ".".join(
                        [
                            class_name,
                            resource_name,
                        ]
                    )
                ),
                api_name=class_name,
            )
            manager_op = ManagerOp(
                name=op_name,
                api_name=name,
                required_params=required_params,
                optional_params=optional_params,
                return_ty=return_ty,
            )
            managers[manager].append(manager_op)
        buf.start_block(f"async def {name}(self{params_str}) -> {return_ty}")
        buf.writeln("...")
        buf.end_block()
    buf.end_block()

# `kubernetes_asyncio.client.api` root.
buf = CodegenBuf(API_STUBS_DIR / "__init__.pyi")
for name in apis:
    buf.writeln(
        f"from kubernetes_asyncio.client.api.{name}_api import {make_class_name(name)}Api as {make_class_name(name)}Api"
    )

# `kubernetes_asyncio.client` root.
buf = CodegenBuf(CLIENT_STUBS_DIR / "__init__.pyi")
for name in schema["definitions"]:
    buf.writeln(
        f"from kubernetes_asyncio.client.models.{make_file_name(name)} import {make_class_name(name)} as {make_class_name(name)}"
    )
    buf.writeln(
        f"from kubernetes_asyncio.client.models.{make_file_name(name)} import {make_class_name(name)}Dict as {make_class_name(name)}Dict"
    )
for name in apis:
    buf.writeln(
        f"from kubernetes_asyncio.client.api.{name}_api import {make_class_name(name)}Api as {make_class_name(name)}Api"
    )

# `kubernetes` root.
CodegenBuf(STUBS_DIR / "__init__.pyi")

# `kubernetes_ext` root.
buf = CodegenBuf(EXT_DIR / "__init__.py")
buf.writeln("import kubernetes_asyncio.client")
buf.writeln("import typing")
for manager, ops in managers.items():
    buf.start_block(f"class {manager.name}Manager")
    buf.start_block(
        f"def __init__(self, client: kubernetes_asyncio.client.{manager.api_name}Api) -> None"
    )
    buf.writeln("self.client = client")
    buf.end_block()
    for op in ops:
        required_params_str = ", ".join(param.arg_str() for param in op.required_params)
        if required_params_str:
            required_params_str = ", " + required_params_str
        optional_params_str = ", ".join(param.arg_str() for param in op.optional_params)
        if optional_params_str:
            optional_params_str = ", *, " + optional_params_str
        params_str = required_params_str + optional_params_str
        buf.start_block(f"async def {op.name}(self{params_str}) -> {op.return_ty}")
        args = ", ".join(
            f"{param.name}={param.name}"
            for param in op.required_params + op.optional_params
        )
        buf.writeln(f"return await self.client.{op.api_name}({args})")
        buf.end_block()
    buf.end_block()
