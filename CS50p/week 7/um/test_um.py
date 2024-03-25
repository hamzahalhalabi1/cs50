import pytest
from um import count


def test_um_normal():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("umbrella") == 0


def test_um_symbols():
    assert count("um.") == 1
    assert count("um?") == 1
    assert count("um,") == 1


def test_um_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um,") == 1
