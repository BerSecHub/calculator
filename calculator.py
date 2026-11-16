"""Calculator class from Lab 2 with usage examples."""
import math

class Calculator:
    """Two-operand calculator.

    Contract: no method raises. When a result cannot be computed
    (division by zero, operand that is not a number), the result is NaN.
    """
    def __init__(self, op1:float, op2:float):
        self.__op1 = self.__to_float(op1)
        self.__op2 = self.__to_float(op2)


    @staticmethod
    def __to_float(value) -> float:
        try:
            return float(value)
        except (TypeError, ValueError, OverflowError):
            return math.nan

    def sum(self) -> float:
        """Return op1 + op2."""
        return self.__op1 + self.__op2
    def subtract(self) -> float:
        """Return op1 - op2."""
        return self.__op1 - self.__op2
    def multiply(self) -> float:
        """Return op1 * op2."""
        return self.__op1 * self.__op2
    def divide(self) -> float:
        """Return op1 / op2, or nan when op2 is zero"""
        if self.__op2 == 0:
            return math.nan
        return self.__op1 / self.__op2


if __name__ == "__main__":
    calc = Calculator(10, 4)
    print("10 + 4 =", calc.sum())
    print("10 - 4 =", calc.subtract())
    print("10 * 4 =", calc.multiply())
    print("10 / 4 =", calc.divide())

    # Special cases: nan instead of an exception
    print("10 / 0 =", Calculator(10, 0).divide())
    print("'abc' + 2 =", Calculator("abc", 2).sum())
    print("None * 2 =", Calculator(None, 2).multiply())
