"""
Intenionally introduced bugs so that I can test for them in test.py

@author: Eleni Rotsides
I pledge my honor that I have abided by the Stevens honor system.
"""


def classify_triangle(a, b, c):
    """Given 3 triangle side lengths, this funtion identifies what type of triangle it is"""
    if(a == b and b == c and c == a):
        return 'Equilateral'
    elif(a * a + b * b == c * c):
        return 'Right'
    elif(a != b and b != c and c != a):
        return 'Scalene'
    else:
        return 'Isosceles'


if __name__ == '__main__':
    print(classify_triangle(3, 3, 3))  # equilateral
    print(classify_triangle(6, 6, 8))  # isoceles
    print(classify_triangle(3, 4, 5))  # right
    print(classify_triangle(2, 3, 11))  # scalene
