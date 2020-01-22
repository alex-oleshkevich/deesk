class Storage:
    def exists(self, path: str) -> bool: ...
    def missing(self, path: str) -> bool: ...


class FilesystemStorage(Storage):
    async def put(self, path: str, data: str): ...
    async def prepend(self, path: str, data: str): ...
    async def chmod(self): ...
    async def delete(self): ...
    async def move(self): ...
    async def copy(self): ...
    async def rename(self): ...
    async def name(self): ...
    async def basename(self): ...
    async def dirname(self): ...
    async def extension(self): ...
    async def exists(self): ...
    async def open(self): ...
    async def write(self): ...
    async def mime_type(self): ...
    async def size(self): ...
    async def mkdir(self): ...
    async def generate_filename(self): ...
    async def list_directory(self): ...
    async def get_created_time(self, path): ...
    async def get_modified_time(self, path): ...
    async def get_accessed_time(self, path): ...
    def glob(self): ...
    def files(): ...
    def directories(self): ...
    def clear(self): ...
    def hash(self): str: ...


storage = FilesystemStorage()
await storage.read('/home/alex/file/file.txt')
await storage.write('/home/alex/file/file.txt', contents)