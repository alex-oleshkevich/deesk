from __future__ import annotations

import typing as t
from types import TracebackType


class FileReader(t.Protocol[t.AnyStr]):
    async def read(self, size: int = -1) -> t.AnyStr: ...

    async def __aenter__(self) -> FileReader: ...

    async def __aexit__(self, exc_type: t.Type[BaseException], exc_val: BaseException, exc_tb: TracebackType): ...
