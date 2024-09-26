# Copyright (C) 2024 DataJob Sweden AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
