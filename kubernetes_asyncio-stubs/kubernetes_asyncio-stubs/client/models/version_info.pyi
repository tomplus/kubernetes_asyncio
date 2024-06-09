import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class VersionInfo:
    build_date: str
    compiler: str
    git_commit: str
    git_tree_state: str
    git_version: str
    go_version: str
    major: str
    minor: str
    platform: str
    
    def __init__(self, *, build_date: str, compiler: str, git_commit: str, git_tree_state: str, git_version: str, go_version: str, major: str, minor: str, platform: str) -> None:
        ...
    def to_dict(self) -> VersionInfoDict:
        ...
class VersionInfoDict(typing.TypedDict, total=False):
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str
