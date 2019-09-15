import unittest
from Customer import Customer


class MyTestCase(unittest.TestCase):
    def test_customer_properties(self):
        cu = Customer("Dr", "Tobias", "Rieper", "23 Fake St", "email@tobias.com", "4883784", False)

        self.assertEqual("23 Fake St", cu.get_address())
        self.assertEqual("email@tobias.com", cu.get_email())
        self.assertEqual("Tobias", cu.get_first_name())
        self.assertEqual(False, cu.get_member())
        self.assertEqual("4883784", cu.get_number())
        self.assertEqual("Rieper", cu.get_surname())
        self.assertEqual("Dr", cu.get_title())
