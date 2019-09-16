import unittest
from CalculatorEngine import CalculatorEngine

Engine = CalculatorEngine()


class TestCalculatorEngine(unittest.TestCase):

    def test_calc_bmi(self):
        Engine.is_male = False
        Engine.age_years = 21
        Engine.weight_kg = 64
        Engine.height_m = 2.1
        Engine.bmi = Engine.calc_bmi()

        self.assertEqual(14.512471655328797, Engine.get_bmi())
