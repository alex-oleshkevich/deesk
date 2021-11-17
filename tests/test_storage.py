import io
import pytest
from moto import mock_s3

from deesk.drivers.base import Driver
from deesk.storage import Storage
from tests.conftest import drivers


@pytest.mark.asyncio
@pytest.mark.parametrize('driver', drivers)
@mock_s3
async def test_get_put_exists_delete(driver: Driver, image: bytes) -> None:
    fs = Storage(driver)

    # load binary file
    await fs.put('project/user/avatar.png', image)

    # test that file exists
    assert await fs.exists('project/user/avatar.png') is True
    assert await fs.exists('project/user/missing.png') is False

    # read file contents
    async with await fs.get('project/user/avatar.png') as f:
        assert await f.read() == image

    # delete file
    await fs.delete('project/user/avatar.png')
    assert await fs.exists('project/user/avatar.png') is False


@pytest.mark.asyncio
@pytest.mark.parametrize('driver', drivers)
@mock_s3
async def test_text_content(driver: Driver) -> None:
    fs = Storage(driver)

    await fs.put('project/user/book.txt', 'Hello World')
    async with await fs.get('project/user/book.txt', 'r') as f:
        assert await f.read() == 'Hello World'

    await fs.delete('project/user/book.txt')


@pytest.mark.asyncio
@pytest.mark.parametrize('driver', drivers)
@mock_s3
async def test_bytes_io_stream_content(driver: Driver) -> None:
    fs = Storage(driver)

    stream = io.BytesIO(b'hello')
    await fs.put('project/user/book.txt', stream)
    async with await fs.get('project/user/book.txt') as f:
        assert await f.read() == b'hello'

    await fs.delete('project/user/book.txt')
