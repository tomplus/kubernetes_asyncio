# Copyright 2018 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import re
from os import path

import yaml

from kubernetes_asyncio import client

DEFAULT_DELETION_BODY = client.V1DeleteOptions(
    propagation_policy="Background",
    grace_period_seconds=5,
)


def delete_from_yaml(
    k8s_client,
    yaml_file,
    verbose=False,
    namespace="default",
    body=None,
    **kwargs,
):
    """
    Perform delete objects from yaml file. Pass True for verbose to
    print confirmation information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    k8s_client: an ApiClient object, initialized with the client args.
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    body: V1 delete options
    Raises:
        FailToDeleteError which holds list of `client.rest.ApiException`
        instances for each object that failed to delete.
    """
    if body is None:
        body = DEFAULT_DELETION_BODY

    with open(path.abspath(yaml_file)) as f:
        yml_document_all = yaml.safe_load_all(f)
        failures = []
        for yml_document in yml_document_all:
            try:
                # call delete from dict function
                await delete_from_dict(
                    k8s_client,
                    yml_document,
                    verbose,
                    namespace=namespace,
                    body=body,
                    **kwargs,
                )
            except FailToDeleteError as failure:
                failures.extend(failure.api_exceptions)
        if failures:
            raise FailToDeleteError(failures)


async def delete_from_dict(
    k8s_client,
    yml_document,
    verbose=False,
    namespace="default",
    body=None,
    **kwargs,
):
    if body is None:
        body = DEFAULT_DELETION_BODY

    api_exceptions = []
    if "List" in yml_document["kind"]:
        kind = yml_document["kind"].replace("List", "")
        for yml_doc in yml_document["items"]:
            if kind != "":
                yml_doc["apiVersion"] = yml_document["apiVersion"]
                yml_doc["kind"] = kind
            try:
                await delete_from_yaml_single_item(
                    k8s_client,
                    yml_doc,
                    verbose,
                    namespace=namespace,
                    body=body,
                    **kwargs,
                )
            except client.rest.ApiException as api_exception:
                api_exceptions.append(api_exception)
    else:

        try:
            await delete_from_yaml_single_item(
                k8s_client,
                yml_document,
                verbose,
                namespace=namespace,
                body=body,
                **kwargs,
            )
        except client.rest.ApiException as api_exception:
            api_exceptions.append(api_exception)

    if api_exceptions:
        raise FailToDeleteError(api_exceptions)


async def delete_from_yaml_single_item(
    k8s_client,
    yml_document,
    verbose=False,
    namespace="default",
    body=None,
    **kwargs,
):
    if body is None:
        body = DEFAULT_DELETION_BODY

    # get group and version from apiVersion
    group, _, version = yml_document["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    # Only replace the last instance
    group = "".join(group.rsplit(".k8s.io", 1))
    # convert group name from DNS subdomain format to
    # python class name convention
    group = "".join(word.capitalize() for word in group.split("."))
    fcn_to_call = "{0}{1}Api".format(group, version.capitalize())
    k8s_api = getattr(client, fcn_to_call)(k8s_client)
    # Replace CamelCased action_type into snake_case
    kind = yml_document["kind"]
    kind = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", kind)
    kind = re.sub("([a-z0-9])([A-Z])", r"\1_\2", kind).lower()

    # Decide which namespace we are going to use for deleteing the object
    # IMPORTANT: Its ignore namespace in args:
    #    create_from_yaml_single_item have same behaviour
    if "namespace" in yml_document["metadata"]:
        namespace = yml_document["metadata"]["namespace"]
    name = yml_document["metadata"]["name"]

    # Expect the user to delete namespaced objects more often
    if hasattr(k8s_api, "delete_namespaced_{0}".format(kind)):
        resp: client.V1Status = await getattr(
            k8s_api, "delete_namespaced_{0}".format(kind)
        )(name=name, namespace=namespace, body=body, **kwargs)
    else:
        resp: client.V1Status = await getattr(k8s_api, "delete_{0}".format(kind))(
            name=name, body=body, **kwargs
        )
    if verbose:
        print("{0} deleted. status='{1}'".format(kind, str(resp.status)))
    return resp


class FailToDeleteError(Exception):
    """
    An exception class for handling error if an error occurred when
    handling a yaml file during deletion of the resource.
    """

    def __init__(self, api_exceptions):
        self.api_exceptions = api_exceptions

    def __str__(self):
        msg = ""
        for api_exception in self.api_exceptions:
            msg += "Error from server ({0}):{1}".format(
                api_exception.reason, api_exception.body
            )
        return msg
