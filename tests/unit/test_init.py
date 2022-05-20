import unittest.mock as mock
import testing_for_fun
import sys


def test_main_starts_async():
    # Mock out an entire module -- asyncio
    with mock.patch("testing_for_fun.asyncio") as mock_asyncio:

        # Mock out an method -- amain
        with mock.patch("testing_for_fun.amain", mock.MagicMock()) as mock_amain:
            testing_for_fun.main()

    # confirm the asyncio.run method is called once
    # with the return_value from calling amain()
    mock_asyncio.run.assert_called_once_with(mock_amain.return_value)


# mock sys.argv values so that Argparser is satisfied
@mock.patch.object(sys, "argv", ["testing_for_fun", "testing"])
async def test_amain(caplog):
    picked = ["print", "me"]
    mock_picker = mock.AsyncMock(return_value=picked)
    with mock.patch("testing_for_fun.EmojiPicker.pick", mock_picker):
        await testing_for_fun.amain()
    mock_picker.assert_called_once_with("testing")
    assert [f"URL: {pick}" for pick in picked] == [_.message for _ in caplog.records]


async def test_pick_success():
    with mock.patch("aiohttp.ClientSession.get", mock.AsyncMock()) as mock_get:
        mock_response = mock_get.return_value
        mock_response.status = 200
        mock_response.read.return_value = '<html><a href="https://a.link"></a></html>'
        picker = testing_for_fun.EmojiPicker()
        results = await picker.pick("testing")
    mock_get.assert_called_with(picker.SLACKMOJIS, params=dict(query="testing"))
    assert results == ["https://a.link"]
