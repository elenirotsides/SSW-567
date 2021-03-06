# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle_program import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        # not sure about this one
        self.assertNotEqual(classify_triangle(5, 3, 4),
                            'Right', '5,3,4 is a scalene triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testInputsAreValidA(self):
        self.assertEqual(classify_triangle(200, 5, 6), 'InvalidInput')

    def testInputsAreValidB(self):
        self.assertEqual(classify_triangle(5, 200, 6), 'InvalidInput')

    def testInputsAreValidC(self):
        self.assertEqual(classify_triangle(5, 6, 200), 'InvalidInput')

    def testInputsAreValidD(self):
        self.assertEqual(classify_triangle(-5, 5, 6), 'InvalidInput')

    def testInputsAreValidE(self):
        self.assertEqual(classify_triangle(5, -5, 6), 'InvalidInput')

    def testInputsAreValidF(self):
        self.assertEqual(classify_triangle(6, 5, -5), 'InvalidInput')

    def testInputsAreValidG(self):
        self.assertEqual(classify_triangle(6, 5, 'Hello'), 'InvalidInput')

    def testInputsAreValidH(self):
        self.assertEqual(classify_triangle('Hello', 5, 5), 'InvalidInput')

    def testInputsAreValidI(self):
        self.assertEqual(classify_triangle(6, 'Hello', 5), 'InvalidInput')

    def testSideLengthsAreValidA(self):
        self.assertEqual(classify_triangle(3, 4, 50), 'NotATriangle')

    def testSideLengthsAreValidB(self):
        self.assertEqual(classify_triangle(50, 4, 3), 'NotATriangle')

    def testSideLengthsAreValidC(self):
        self.assertEqual(classify_triangle(3, 50, 4), 'NotATriangle')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(2, 4, 5), 'Scalene')

    def testIsocelesTriangleA(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classify_triangle(3, 2, 2), 'Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classify_triangle(2, 3, 2), 'Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
