import pytest
from app.calculator import Calculator


class TestCalc:
    @pytest.fixture
    def calc(self):
        return Calculator()

    def test_addition(self, calc):
        assert calc.add(2, 2) == 4

    def test_subtraction(self, calc):
        assert calc.subtract(4, 2) == 2

    def test_multiplication(self, calc):
        assert calc.multiply(2, 3) == 6

    def test_division(self, calc):
        assert calc.divide(6, 2) == 3
