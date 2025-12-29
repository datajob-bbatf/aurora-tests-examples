# Copyright (C) 2025 DataJob Sweden AB
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

import time
from aurora_tests.pytest.fixtures import display, touches, log_monitors


def test_alarm_clock_logcat_logs(display, touches, log_monitors):
    """
    Verify that launching the Clock app produces
    the expected logcat message.

    NOTE:
    adb logcat always dumps buffered logs when started. To ensure
    expectations only apply to logs produced by this test, a short
    stabilization timeout is used after starting the monitor to
    allow old log entries to be flushed.
    """

    # Wait after start for buffered logs to flush before registering expectations
    LOGCAT_FLUSH_TIMEOUT_S = 2
    # Maximum time to wait for expected log entry
    LOG_WAIT_TIMEOUT_S = 3

    logcat = log_monitors["logcat"]

    # Use context manager, which calls start() and stop()
    with logcat:
        # Wait until old buffered logs will be dumped
        time.sleep(LOGCAT_FLUSH_TIMEOUT_S)

        # Register an expectation for Clock app launch
        clock_app_started = logcat.expect(
            "Started watching com.android.deskclock.DeskClock"
        )

        # Find the Clock text on the All Apps menu
        clock_icon = display.grab().find_text("Clock")
        assert clock_icon, "'Clock' text not found on the All Apps menu"

        # Tap on the found text to open the Clock app
        touches.tap(clock_icon.center())

        # Wait for app launch log entry
        assert clock_app_started.event.wait(timeout=LOG_WAIT_TIMEOUT_S), \
            f"Expected log message with '{clock_app_started.keyword}' not received"

        print(f"Received log: {clock_app_started.line}")
