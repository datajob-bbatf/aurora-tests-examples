import time
from aurora_tests.pytest_fixtures.config_fixtures import display, touches


def test_find_and_tap_passwords_and_accounts(display, touches):
    # Find the text on the Settings menu
    passwords_and_accounts = display.grab().find_text("Passwords & accounts")
    assert passwords_and_accounts, "'Passwords & accounts' not found on the Settings menu"

    # Tap on the found text to open a child menu
    touches.tap(passwords_and_accounts.center())
