import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(triangle.classify_triangle(3, 3, 3), 'Equilateral')
        self.assertNotEqual(triangle.classify_triangle(
            10, 10, 11), 'Equilateral')
        self.assertNotEqual(triangle.classify_triangle(
            1, 2, 3), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(triangle.classify_triangle(6, 6, 8), 'Isosceles')
        self.assertNotEqual(
            triangle.classify_triangle(10, 10, 10), 'Isosceles')
        self.assertNotEqual(triangle.classify_triangle(1, 2, 3), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(triangle.classify_triangle(2, 3, 11), 'Scalene')
        self.assertNotEqual(triangle.classify_triangle(2, 2, 3), 'Scalene')
        self.assertNotEqual(triangle.classify_triangle(2, 2, 2), 'Scalene')

    def test_right(self):
        self.assertEqual(triangle.classify_triangle(3, 4, 5), 'Right')
        self.assertNotEqual(triangle.classify_triangle(1, 2, 3), 'Right')
        self.assertNotEqual(triangle.classify_triangle(5, 5, 5), 'Right')
        self.assertNotEqual(triangle.classify_triangle(3, 3, 12), 'Right')

    def test_valid_triangle(self):
        # testing invalid arguments
        self.assertEqual(triangle.classify_triangle(0, 2, 3), 'Not Valid')
        self.assertEqual(triangle.classify_triangle(4, 0, 3), 'Not Valid')
        self.assertEqual(triangle.classify_triangle(9, 10, 0), 'Not Valid')
        self.assertEqual(triangle.classify_triangle(-3, -4, -10), 'Not Valid')
        self.assertNotEqual(triangle.classify_triangle(9, 10, 0), 'Scalene')

    def test_c_is_greater(self):
        # this is a test case for testing that a right triangle's c is the longest side
        self.assertEqual(triangle.classify_triangle(5, 3, 4), 'Not Valid')
        self.assertNotEqual(triangle.classify_triangle(5, 3, 4), 'Scalene')


if __name__ == '__main__':
    unittest.main()
