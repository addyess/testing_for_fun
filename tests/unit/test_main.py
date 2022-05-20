import unittest.mock as mock
import importlib
import sys


def test_module_main_starts_async():
    # Mock out an entire module -- asyncio
    with mock.patch("testing_for_fun.asyncio") as mock_asyncio:

        # Mock out an method -- amain
        with mock.patch("testing_for_fun.amain", mock.MagicMock()) as mock_amain:
            main_module = "testing_for_fun.__main__"
            assert main_module not in sys.modules.keys()
            mod = importlib.import_module(main_module)
            del mod
            del sys.modules[main_module]
            assert main_module not in sys.modules.keys()

    # confirm the asyncio.run method is called once
    # with the return_value from calling amain()
    mock_asyncio.run.assert_called_once_with(mock_amain.return_value)
