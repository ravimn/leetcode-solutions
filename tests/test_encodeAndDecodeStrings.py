from typing import Literal
import pytest
from solutions.encodeAndDecodeStrings import Solution as encodeAndDecodeStrings

class TestEncodeAndDecodeStrings:
    @pytest.mark.parametrize("input, expected", [
        (["abc", "def"], "abc#def#"),
        (["abc#", "def"], "abc###def#"),
        (["ab#c", "def"], "ab##c#def#"),
    ])
    def test_encodeStrings(self, input: list[str], expected: str):
        s = encodeAndDecodeStrings()
        assert s.encode(input) == expected

    @pytest.mark.parametrize("input, expected", [
        ("abc#def#", ["abc", "def"] ),
        ("abc###def#", ["abc#", "def"]),
        ("ab##c#def#", ["ab#c", "def"]),
    ])
    def test_decodeStrings(self, input: str, expected: list[str]):
        s = encodeAndDecodeStrings()
        assert s.decode(input) == expected

    @pytest.mark.parametrize("input", [
        (["abc", "def"]),
        (["abc#", "def"]),
        (["ab#c", "def"]),
    ])
    def test_encodeanddecodeStrings(self, input: list[str]):
        s = encodeAndDecodeStrings()
        assert s.decode(s.encode(input)) == input

    
