import unittest
from unit2.customer import Customer



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Customer = Customer(1001, 'Klein', 'Kelly', '319-333-8898')

    def test_customer_cust_id__passes(self):
        cust1 = Customer(1001, 'Klein', 'Kelly', '319-333-8898')
        self.assertEqual(cust1.cid, 1001)

    """
    def test_customer_lname_passes(self):
        cust1 = Customer(1001, 'Klein', 'Kelly', '319-333-8898')
        self.assertEqual(cust1.last_name, 'Klein')

    def test_customer_fname_passes(self):
        cust1 = Customer(1001, 'Klein', 'Kelly', '319-333-8898')
        self.assertEqual(cust1.first_name, 'Kelly')

    def test_customer_phone_passes(self):
        cust1 = Customer(1001, 'Klein', 'Kelly', '319-333-8898')
        self.assertEqual(cust1.phone, '319-333-8898')
    
    def test_display_passes(self):
        expected_string_display = "1001 Kelly Klein 319-333-8898"
        self.assertEqual(cust1.display(), expected_string_display)
"""

    def test_customer_cust_id__exception(self):
        with self.assertRaises(Exception):
            Customer(999, 'Klein', 'Kelly', '319-333-8898')

    def test_customer_lname_exception(self):
        with self.assertRaises(Exception):
            Customer(1001, 9, 'Kelly', '319-333-8898')

    def test_customer_fname_exception(self):
        with self.assertRaises(Exception):
            Customer(1001, 'Klein', 9, '319-333-8898')

    def test_customer_phone_exception(self):
        with self.assertRaises(Exception):
            Customer(1001, 'Klein', 'Kelly', 'phone')

    #def tearDown(self):
        #del Customer


if __name__ == '__main__':
    unittest.main()
