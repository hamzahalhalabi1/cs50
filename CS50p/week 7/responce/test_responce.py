from responce import email_validator
import pytest

def test_normal():
    assert email_validator("malan@harvard.edu") == "Valid"
    assert email_validator("malan@harvard..edu") == "Invalid"
    assert email_validator("malan@@@harvard.edu") == "Invalid"
    assert email_validator("edu") == "Invalid"
    assert email_validator("@") == "Invalid"
    assert email_validator("") == "Invalid"
    assert email_validator("x") == "Invalid"