import unittest
from shapes import rectangle, triangle, trapeze


class ShapesTestCase(unittest.TestCase):
    def setUp(self):
        self.side_a = 6
        self.side_b = 5
        self.height = 4

    def test_rectangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            rectangle(self.side_a, 'example')

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(self.side_a, 'abc')

    def test_trapeze_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            trapeze(self.side_a, self.side_b, [0, 1, 2])

    def test_rectangle_with_correct_values(self):
        self.assertEqual(rectangle(self.side_a, self.side_b), 30)
        self.assertEqual(rectangle(self.side_a + 1, self.side_b + 1), 42)

    def test_triangle_with_correct_values(self):
        self.assertEqual(triangle(self.side_a, self.side_b), 15)

    def test_trapeze_with_correct_values(self):
        self.assertEqual(trapeze(self.side_a, self.side_b, self.height), 22)

    def tearDown(self):
        del self.side_b
        del self.side_a


if __name__ == '__main__':
    unittest.main()
