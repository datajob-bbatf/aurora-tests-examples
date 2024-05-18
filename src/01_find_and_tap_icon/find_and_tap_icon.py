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
