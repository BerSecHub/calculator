import math
import runpy

import pytest

from calculator import Calculator

class TestCalculator:
    def test_sum(self):
        calc = Calculator(2, 3)
        result = calc.sum()
        assert result == 5

    def test_subtract(self):
        calc = Calculator(2, 3)
        result = calc.subtract()
        assert result == -1

    def test_multiply(self):
        calc = Calculator(2, 3)
        result = calc.multiply()
        assert result == 6

    def test_divide(self):
        calc = Calculator(6, 3)
        result = calc.divide()
        assert result == 2

    def test_sum_of_fractions(self):
        assert Calculator(0.1, 0.2).sum() == pytest.approx(0.3)

    def test_divide_by_zero_gives_nan(self):
        assert math.isnan(Calculator(1, 0).divide())

    @pytest.mark.parametrize(
        "bad_value",
        ["abc", None, [1, 2], 10**400],
        ids=["text", "none", "list", "huge_int"],
    )
    def test_invalid_operand_gives_nan(self, bad_value):
        assert math.isnan(Calculator(bad_value, 1).sum())

    def test_examples_run_without_errors(self, capsys):
        runpy.run_module("calculator", run_name="__main__")
        assert "10 / 0 = nan" in capsys.readouterr().out
