import unittest
from unit4.shape import Rectangle as t, InvalidSideError


class RectangleClassTest(unittest.TestCase):

    def setUp(self):
        self.shape = t(12, 23.4)

    def tearDown(self):
        del self.shape

    def test_constructor(self):
        with self.assertRaises(InvalidSideError):
            r = t(5, -5)
        with self.assertRaises(InvalidSideError):
            r = t(-5, 5)

    def test_shape_area(self):
        self.assertAlmostEqual(280.8, self.shape.area())


if __name__ == '__main__':
    unittest.main()
