from typing import Callable, TypeVar

from typing_extensions import ParamSpec

T = TypeVar("T")
P = ParamSpec("P")

def stream(fn: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T: ...
def portforward(fn: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T: ...
