import pytest
from twttr import shorten


def test_cases():
    assert shorten('Hello') == 'Hll'
    assert shorten('world') == 'wrld'
    assert shorten('PYTHON') == 'PYTHN'
    assert shorten('aeiou') == ''


def numbers():
    assert shorten('1234') == '1234'
    assert shorten('a1b2c3') == 'a1b2c3'

def nothing():
    assert shorten('') == ''


def punctuation():
    assert shorten('!,.?') == '!,.?'
