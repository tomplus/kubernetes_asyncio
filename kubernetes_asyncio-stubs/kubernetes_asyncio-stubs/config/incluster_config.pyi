from typing import Optional

from kubernetes_asyncio.client.configuration import Configuration

def load_incluster_config(
    client_configuration: Optional[Configuration] = ..., try_refresh_token: bool = ...
) -> None: ...
