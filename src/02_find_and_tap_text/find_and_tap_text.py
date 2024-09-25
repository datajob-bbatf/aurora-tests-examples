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

from aurora_tests.pytest.fixtures import display, touches


def test_find_and_tap_passwords_and_accounts(display, touches):
    # Find the text on the Settings menu
    passwords_and_accounts = display.grab().find_text("Passwords & accounts")
    assert passwords_and_accounts, "'Passwords & accounts' not found on the Settings menu"

    # Tap on the found text to open a child menu
    touches.tap(passwords_and_accounts.center())
