import pytest
from solutions.myAtoi import Solution as myAtoi

class TestValidParaththesis:
    @pytest.mark.parametrize("text, expected", [
        ("    ", ""),
        ("    abc", "abc"),
        ("abc    ", "abc    "),
        ("  abc    ", "abc    "), 
        ])
    def test_myAtoi_trim(self, text, expected):
        r = myAtoi()
        assert r.trim(text) == expected


    @pytest.mark.parametrize("text, expected", [
        ("    -42", -42),
        ("    -42  dsfasdfa", -42),
        ("abc  -42  ", 0),
        ("  +42    ", 42),
        ("42", 42), 
        ])
    def test_myAtoi(self, text, expected):
        r = myAtoi()
        assert r.myAtoi(text) == expected