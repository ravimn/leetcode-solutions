import pytest
from solutions.stack.validParanthesis import Solution as validParaththesis

class TestValidParaththesis:
    @pytest.mark.parametrize("text, expected", [
        ("()", True), 
        ("()[]{}", True), 
        ("()[{}]", True), 
        ("())", False),
        ("[)", False)
        ])
    def test_validParanthesis(self, text, expected):
        r = validParaththesis()
        assert r.isValid(text) == expected
        