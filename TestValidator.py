import unittest
from Validator import ValidatorClass


class TestValidator(unittest.TestCase):
    def test_isempty(self):
        self.assertEqual(False, ValidatorClass.isempty("amiempty"))
        self.assertEqual(True, ValidatorClass.isempty(""))

    def test_isexerciselevelunselected(self):
        self.assertEqual(False, ValidatorClass.isexerciselevelunselected(1))
        self.assertEqual(True, ValidatorClass.isexerciselevelunselected(-1))
