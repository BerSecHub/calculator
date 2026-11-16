"""Unit tests for the Calculator class."""
import math
import runpy

import pytest

from calculator import Calculator

class TestCalculator:
    """Unit tests for the Calculator class."""
    def test_sum(self):
        """Sum of numbers gives result."""
        calc = Calculator(2, 3)
        result = calc.sum()
        assert result == 5

    def test_subtract(self):
        """Subtract two numbers."""
        calc = Calculator(2, 3)
        result = calc.subtract()
        assert result == -1

    def test_multiply(self):
        """Multiply two numbers."""
        calc = Calculator(2, 3)
        result = calc.multiply()
        assert result == 6

    def test_divide(self):
        """Divide by zero gives nan instead of raising."""
        calc = Calculator(6, 3)
        result = calc.divide()
        assert result == 2

    def test_sum_of_fractions(self):
        """Sum of fractions gives fraction result."""
        assert Calculator(0.1, 0.2).sum() == pytest.approx(0.3)

    def test_divide_by_zero_gives_nan(self):
        """Division by zero returns nan instead of raising."""
        assert math.isnan(Calculator(1, 0).divide())

    @pytest.mark.parametrize(
        "bad_value",
        ["abc", None, [1, 2], 10**400],
        ids=["text", "none", "list", "huge_int"],
    )
    def test_invalid_operand_gives_nan(self, bad_value):
        """Invalid operand gives nan instead of raising."""
        assert math.isnan(Calculator(bad_value, 1).sum())

    def test_examples_run_without_errors(self, capsys):
        """Run without errors gives expected output."""
        runpy.run_module("calculator", run_name="__main__")
        assert "10 / 0 = nan" in capsys.readouterr().out
