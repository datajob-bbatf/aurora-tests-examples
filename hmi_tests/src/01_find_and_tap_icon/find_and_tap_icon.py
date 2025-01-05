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

from aurora_tests.pytest.fixtures import resources, display, touches


def test_find_and_tap_phone_icon(resources, display, touches):
    # We use resources to configure and store parameters (variables)
    # for the test, for example for the path to icon
    phone_icon_path = resources["PHONE_ICON"]

    # Locate the phone icon on the home screen
    phone_icon = display.grab().find_image(phone_icon_path)
    assert phone_icon, "Phone icon not found on the home screen"

    # Tap on the phone icon to open the phone app
    touches.tap(phone_icon.center())
