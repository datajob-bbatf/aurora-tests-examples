import time
from aurora_tests.pytest_fixtures.config_fixtures import resources, display, touches


def test_find_and_tap_phone_icon(resources, display, touches):
    # Locate the phone icon on the home screen
    phone_icon = display.grab().find(resources["PHONE_ICON"])
    assert phone_icon, "Phone icon not found on the home screen"

    # Tap on the phone icon to open the phone app
    touches.tap(phone_icon.center())
