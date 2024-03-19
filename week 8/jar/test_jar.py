from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(50)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(50)
