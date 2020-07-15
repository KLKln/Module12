import unittest
from unit2.customer import Customer



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Customer = Customer(1001, 'Klein', 'Kelly', '319-333-8898')

    def test_customer_cust_id__passes(self):
        with self.assertEqual(Customer(1001, 'Klein', 'Kelly', '319-333-8898'),
                              Customer):
            Customer(1001, 'Klein', 'Kelly', '319-333-8898')
    """
    def test_customer_lname_passes(self):
        with self.assertRaises(Exception):
            Customer(1001, 'Klein', 'Kelly', '319-333-8898')

    def test_customer_fname_passes(self):
        with self.assertRaises(Exception):
            Customer(1001, 'Klein', 'Kelly', '319-333-8898')

    def test_customer_phone_passes(self):
        with self.assertRaises(Exception):
            Customer(1001, 'Klein', 'Kelly', '319-333-8898')
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
