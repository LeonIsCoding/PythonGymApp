import unittest
from CalculatorEngine import CalculatorEngine

Engine = CalculatorEngine()


class TestCalculatorEngine(unittest.TestCase):

    def test_calc_rdi(self):
        self.assertEqual(1200.0, Engine.calc_rdi("Sedentary", 1000))
        self.assertEqual(1375.0, Engine.calc_rdi("Light (1-3 days per week)", 1000))
        self.assertEqual(1550.0, Engine.calc_rdi("Moderate (3-5 days per week)", 1000))
        self.assertEqual(1725.0, Engine.calc_rdi("Heavy (6-7 days per week)", 1000))
        self.assertEqual(1900.0, Engine.calc_rdi("Very Heavy (Twice per day or more)", 1000))

    def test_calc_bmr(self):
        Engine.is_male = False
        Engine.age_years = 21
        Engine.weight_kg = 64
        Engine.height_cm = 210

        Engine.set_bmr(Engine.bmr_rhb())
        self.assertEqual(1599.051, Engine.get_bmr())

    def test_calc_bmi(self):
        Engine.is_male = False
        Engine.age_years = 21
        Engine.weight_kg = 64
        Engine.height_m = 2.1
        Engine.bmi = Engine.calc_bmi()

        self.assertEqual(14.512471655328797, Engine.get_bmi())
