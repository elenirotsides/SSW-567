# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(a_side, b_side, c_side):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a_side, int) and isinstance(b_side, int) and isinstance(c_side, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if (a_side >= 200 or b_side >= 200 or c_side >= 200):
        return 'InvalidInput'
    if (a_side <= 0 or b_side <= 0 or c_side <= 0):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    type_of_triangle = 'Isoceles'

    if (a_side >= (b_side + c_side)) or (b_side >= (a_side + c_side)) \
            or (c_side >= (a_side + b_side)):
        type_of_triangle = 'NotATriangle'
    elif a_side == b_side and b_side == c_side and c_side == a_side:
        type_of_triangle = 'Equilateral'
    elif ((a_side * a_side) + (b_side * b_side)) == (c_side * c_side):
        type_of_triangle = 'Right'
    elif (a_side != b_side) and (b_side != c_side) and (a_side != c_side):
        type_of_triangle = 'Scalene'

    return type_of_triangle
