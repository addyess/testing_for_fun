import importlib
import sys


def test_module_main_starts_async(mock_asyncio_run, mock_amain):
    main_module = "testing_for_fun.__main__"
    assert main_module not in sys.modules.keys()
    mod = importlib.import_module(main_module)
    del mod
    del sys.modules[main_module]
    assert main_module not in sys.modules.keys()

    # confirm the asyncio.run method is called once
    # with the return_value from calling amain()
    mock_asyncio_run.assert_called_once_with(mock_amain.return_value)
