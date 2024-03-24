from plates import is_valid
import pytest



def test_valid_plate():
    assert is_valid("AB1234")


def test_invalid_plate_length():
    assert not is_valid("A1")
    assert not is_valid("C5")

def test_invalid_plate_alpha():
    assert not is_valid("123456")
    assert not is_valid("HELLOCS50")


def test_invalid_plate_startswith_zero():
    assert not is_valid("AB0123")


def test_invalid_plate_alpha_suffix():
    assert not is_valid("AB12CD")


def test_invalid_plate_alpha_at_end():
    assert not is_valid("ABCD01")


def test_invalid_plate_special_characters():
    assert not is_valid("AB#123")



def test_invalid_plate_empty_string():
    assert not is_valid("")

