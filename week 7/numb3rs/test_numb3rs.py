    import pytest
    from numb3rs import validate


    def test_validate():
        assert validate("2.3.5.2") is True
        assert validate("2222.3.5.2") is False
        assert validate("2.3.5.2.24") is False
        assert validate("cat") is False
        assert validate("512.255.255.255") is False
        assert validate("2,35,2,1") is False
