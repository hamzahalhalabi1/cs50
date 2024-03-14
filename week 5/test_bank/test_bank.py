from bank import value
import pytest


def test_value():
    assert value('hello') == 0
    assert value('hfdsbn') == 20
    assert value('fjkdfjdkf') == 100
    assert value('HELLO') == 0