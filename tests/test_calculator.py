import unittest

from src.calculator import suma, resta, multiplicacion, divicion

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 2), 4)

    def test_divicion(self):
        self.assertEqual(divicion(4, 2), 2)
