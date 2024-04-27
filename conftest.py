
import pytest


def pytest_addoption(parser):
    parser.addoption("--config_file", action="store", default=None)
    parser.addoption("--res_file", action="store", default=None)


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    config_file_value = metafunc.config.option.config_file
    if 'config_file' in metafunc.fixturenames and config_file_value is not None:
        metafunc.parametrize("config_file", [config_file_value])

    res_file_value = metafunc.config.option.res_file
    if 'res_file' in metafunc.fixturenames and res_file_value is not None:
        metafunc.parametrize("res_file", [res_file_value])


def pytest_runtest_setup(item):
    pass


def pytest_runtest_teardown(item):
    # TODO: To save failed test artifacts
    pass
