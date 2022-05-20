import unittest.mock as mock
import pytest


@pytest.fixture()
def mock_asyncio_run():
    # Mock out asyncio:run method
    with mock.patch("asyncio.run") as run:
        yield run


@pytest.fixture()
def mock_amain():
    # Mock out an method -- amain
    with mock.patch("testing_for_fun.amain", mock.MagicMock()) as amain:
        yield amain


@pytest.fixture(autouse=True)
def client_get():
    # with autouse=True, this prevents any testing
    # from ever calling out to the URL by accident
    with mock.patch("aiohttp.ClientSession.get", mock.AsyncMock()) as mock_get:
        yield mock_get
