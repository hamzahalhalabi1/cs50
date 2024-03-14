from working import convert
import pytest

def test_convert_12():
    assert convert("12 PM to 5 AM") == "12:00 to 05:00"
    assert convert("12 AM to 5 AM") == "00:00 to 05:00"

def test_convert_no_mins():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9 PM to 11 PM") == "21:00 to 23:00"
    assert convert("7 AM to 2 AM") == "07:00 to 02:00"

def test_convert_mins():
    assert convert("9:45 AM to 11:12 PM") == "09:45 to 23:12"
    assert convert("1:55 PM to 6:00 PM") == "13:55 to 18:00"

def test_convert_wrong_hour():
    with pytest.raises(ValueError):
        assert(convert("13:00 AM to 18:00 PM"))
        assert(convert("12:00 AM to -1:00 AM"))

def test_convert_wrong_minute():
    with pytest.raises(ValueError):
        assert(convert("5:84 AM to 12:75 PM"))

def test_convert_wrong_format():
    with pytest.raises(ValueError):
        assert(convert("9 AM - 5 PM"))
        assert(convert("09:00 AM - 17:00 PM"))
        assert(convert("12:00AM to 1:00AM"))
        assert(convert("12:00 AM 1:00 AM"))