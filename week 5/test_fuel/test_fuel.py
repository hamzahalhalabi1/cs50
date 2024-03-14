import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("2/4") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def tes_dev_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

