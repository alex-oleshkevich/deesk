import pytest

from ekko.storage import Storage
from tests.conftest import drivers


@pytest.mark.asyncio
@pytest.mark.parametrize('driver', drivers)
async def test_get_put_exists_delete(driver, image):
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
async def test_text_content(driver):
    fs = Storage(driver)

    await fs.put('project/user/book.txt', 'Hello World')
    async with await fs.get('project/user/book.txt', 'r') as f:
        assert await f.read() == 'Hello World'

    await fs.delete('project/user/book.txt')
