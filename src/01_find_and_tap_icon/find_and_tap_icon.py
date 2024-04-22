from aurora_tests.hello_world import say_hello


def test_say_hello():
    assert "Hello World!" == say_hello()
