# Copyright 2026 The Kubernetes Authors.
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

"""Helpers to convert between plain dict manifests and typed client models."""

from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any, Mapping, TypeVar

from kubernetes_asyncio.client.api_client import ApiClient
from kubernetes_asyncio.client.configuration import Configuration

T = TypeVar("T")


def _serialization_api_client() -> ApiClient:
    """Build an ApiClient usable for (de)serialization without a running loop.

    ``ApiClient()`` constructs an aiohttp connector, which requires a running
    event loop. Dict/model conversion only needs ``deserialize`` /
    ``sanitize_for_serialization``, so we skip the REST client.
    """
    client = ApiClient.__new__(ApiClient)
    configuration = Configuration.get_default_copy()
    client.configuration = configuration
    client.pool_threads = 1
    client.rest_client = None
    client.default_headers = {}
    client.cookie = None
    client.user_agent = "OpenAPI-Generator/serialization-only"
    client.client_side_validation = configuration.client_side_validation
    client._pool = None
    return client


def model_from_dict(
    data: Mapping[str, Any],
    model_class: type[T],
    *,
    api_client: ApiClient | None = None,
) -> T:
    """Build a typed model instance from a plain dict (YAML/JSON manifest).

    Useful when manifests are loaded dynamically and the API method expects a
    typed body (e.g. ``V1Secret``) rather than ``dict``.

    Example::

        secret = model_from_dict(manifest_dict, client.V1Secret)
        await v1.create_namespaced_secret(namespace, secret)

    :param data: Mapping with Kubernetes JSON field names (camelCase).
    :param model_class: Model class such as ``V1Secret`` or ``V1Pod``.
    :param api_client: Optional existing ``ApiClient`` to reuse.
    :return: An instance of ``model_class``.
    """
    client = api_client or _serialization_api_client()
    return client.deserialize(
        SimpleNamespace(data=json.dumps(data)),
        model_class,
    )


def model_to_dict(obj: Any, *, api_client: ApiClient | None = None) -> Any:
    """Serialize a model instance to a dict with Kubernetes JSON field names.

    Nested models are converted recursively. Values that are already
    primitives, lists, or dicts are returned as sanitized structures.

    Example::

        payload = model_to_dict(secret)
        # payload["stringData"] rather than payload["string_data"]

    :param obj: A client model instance (or nested structure of models).
    :param api_client: Optional existing ``ApiClient`` to reuse.
    :return: JSON-serializable structure using API field names.
    """
    if api_client is None and hasattr(obj, "to_dict"):
        # Prefer the generated helper when no client is supplied.
        try:
            return obj.to_dict(serialize=True)
        except TypeError:
            # Older generated models may not accept serialize=
            pass
    client = api_client or _serialization_api_client()
    return client.sanitize_for_serialization(obj)
