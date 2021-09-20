import typing as t


class File:
    async def read(self, size: int = -1) -> t.AnyStr:
        ...
