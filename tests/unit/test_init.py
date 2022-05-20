import unittest.mock as mock
import sys

import pytest

import testing_for_fun


async def test_main_starts_async(mock_asyncio_run, mock_amain):
    # confirm the asyncio.run method is called once
    # with the return_value from calling amain()
    testing_for_fun.main()
    mock_asyncio_run.assert_called_once_with(mock_amain.return_value)


# mock sys.argv values so that Argparser is satisfied
@mock.patch.object(sys, "argv", ["testing_for_fun", "testing"])
@pytest.mark.parametrize(
    "picked",
    [
        tuple(),
        ("one thing",),
        ("two", "things"),
    ],
    ids=["empty", "one-thing", "two-things"],
)
async def test_amain(caplog, picked):
    mock_picker = mock.AsyncMock(return_value=picked)
    with mock.patch("testing_for_fun.EmojiPicker.pick", mock_picker):
        await testing_for_fun.amain()
    mock_picker.assert_called_once_with("testing")
    assert [f"URL: {pick}" for pick in picked] == [_.message for _ in caplog.records]


async def test_pick_success(client_get):
    mock_response = client_get.return_value
    mock_response.status = 200
    mock_response.read.return_value = '<html><a href="https://a.link"></a></html>'
    picker = testing_for_fun.EmojiPicker()
    results = await picker.pick("testing")
    client_get.assert_called_with(picker.SLACKMOJIS, params=dict(query="testing"))
    assert results == ["https://a.link"]


async def test_pick_fails(client_get):
    mock_response = client_get.return_value
    mock_response.status = 401
    picker = testing_for_fun.EmojiPicker()
    results = await picker.pick("testing")
    client_get.assert_called_with(picker.SLACKMOJIS, params=dict(query="testing"))
    assert results == []
