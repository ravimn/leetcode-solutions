import pytest
from solutions.restoreIPAddresses import Solution as resotreIPAddressess

class TestRestoreIPAddresses:
    @pytest.mark.parametrize("s, expected", [
        ("123", True),
        ("0", True),
        ("01", False),
        ("123", True),
        ("345", False),
        ("34", True)
    ])
    def test_isValidIPv4Part(self, s:str, expected:bool):
        r = resotreIPAddressess()
        assert r.isValidIPv4Part(s) == expected

    @pytest.mark.parametrize("parts, expected", [
        ([0,0,0,0], "0.0.0.0"),
        ([0,0,0], ""),
    ])
    def test_returnIPAddress(self, parts:list[int], expected: str):
        r = resotreIPAddressess()
        assert r.returnIPAddress(parts) == expected

    @pytest.mark.parametrize("s, expected", [
        ("0000", ['0.0.0.0']),
        ("25525511135", ["255.255.11.135","255.255.111.35"]),
        ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
    ])
    def test_resotreIPAddressess(self, s:str, expected: list[str]):
        r = resotreIPAddressess()
        assert r.restoreIpAddresses(s) == expected
