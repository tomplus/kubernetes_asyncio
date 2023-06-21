from typing import Optional

class Configuration(object):
    host: str
    temp_folder_path: str
    api_key: dict[str, str]
    api_key_prefix: str
    username: str
    password: str
    discard_unknown_keys: bool
    def __init__(
        self,
        host: str = ...,
        api_key: Optional[str] = ...,
        api_key_prefix: Optional[str] = ...,
        username: Optional[str] = ...,
        password: Optional[str] = ...,
        discard_unknown_keys: bool = ...,
    ) -> None: ...
