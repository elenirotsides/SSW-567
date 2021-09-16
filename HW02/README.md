# Triangle HW02a

## Part 1 - Test Report of initial round of testing

(No changes made to original program, only test cases have been written to test `classifyTriangle(a,b,c)`)

| TestID                   | Input           | Expected Results                                         | Actual Results                                                    | Pass or Fail |
| ------------------------ | --------------- | -------------------------------------------------------- | ----------------------------------------------------------------- | ------------ |
| testRightTriangleA       | (3, 4, 5)       | 'Right'                                                  | 'InvalidInput'                                                    | Fail         |
| testRightTriangleB       | (5, 3, 4)       | !'Right' (not right, using `asserNotEqual` for this one) | !'Right'                                                          | Pass         |
| testEquilateralTriangles | (1, 1, 1)       | 'Equilateral'                                            | 'InvalidInput'                                                    | Fail         |
| testInputsAreValidA      | (200, 5, 6)     | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidB      | (5, 200, 6)     | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidC      | (5, 6, 200)     | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidD      | (-5, 5, 6)      | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidE      | (5, -5, 6)      | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidF      | (6, 5, -5)      | 'InvalidInput'                                           | 'InvalidInput'                                                    | Pass         |
| testInputsAreValidG      | (6, 5, 'Hello') | 'InvalidInput'                                           | TypeError: '>' not supported between instances of 'str' and 'int' | Fail         |
| testInputsAreValidH      | ('Hello', 5, 5) | 'InvalidInput'                                           | TypeError: '>' not supported between instances of 'str' and 'int' | Fail         |
| testInputsAreValidI      | (6, 'Hello', 5) | 'InvalidInput'                                           | TypeError: '>' not supported between instances of 'str' and 'int' | Fail         |
| testSideLengthsAreValidA | (3, 4, 50)      | 'NotATriangle'                                           | 'InvalidInput'                                                    | Fail         |
| testSideLengthsAreValidB | (50, 4, 3)      | 'NotATriangle'                                           | 'InvalidInput'                                                    | Fail         |
| testSideLengthsAreValidC | (3, 50, 4)      | 'NotATriangle'                                           | 'InvalidInput'                                                    | Fail         |
| testScaleneTriangle      | (2, 4, 5)       | 'Scalene'                                                | 'InvalidInput'                                                    | Fail         |
| testIsocelesTriangleA    | (2, 2, 3)       | 'Isoceles'                                               | 'InvalidInput'                                                    | Fail         |
| testIsocelesTriangleB    | (3, 2, 2)       | 'Isoceles'                                               | 'InvalidInput'                                                    | Fail         |
| testIsocelesTriangleC    | (2, 3, 2)       | 'Isoceles'                                               | 'InvalidInput'                                                    | Fail         |

## Part 2 - Test report after bugs have been fixed in `Triangle.py`

| TestID                   | Input           | Expected Results                                         | Actual Results | Pass or Fail |
| ------------------------ | --------------- | -------------------------------------------------------- | -------------- | ------------ |
| testRightTriangleA       | (3, 4, 5)       | 'Right'                                                  | 'Right'        | Pass         |
| testRightTriangleB       | (5, 3, 4)       | !'Right' (not right, using `asserNotEqual` for this one) | !'Right'       | Pass         |
| testEquilateralTriangles | (1, 1, 1)       | 'Equilateral'                                            | 'Equilateral'  | Pass         |
| testInputsAreValidA      | (200, 5, 6)     | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidB      | (5, 200, 6)     | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidC      | (5, 6, 200)     | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidD      | (-5, 5, 6)      | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidE      | (5, -5, 6)      | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidF      | (6, 5, -5)      | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidG      | (6, 5, 'Hello') | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidH      | ('Hello', 5, 5) | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testInputsAreValidI      | (6, 'Hello', 5) | 'InvalidInput'                                           | 'InvalidInput' | Pass         |
| testSideLengthsAreValidA | (3, 4, 50)      | 'NotATriangle'                                           | 'NotATriangle' | Pass         |
| testSideLengthsAreValidB | (50, 4, 3)      | 'NotATriangle'                                           | 'NotATriangle' | Pass         |
| testSideLengthsAreValidC | (3, 50, 4)      | 'NotATriangle'                                           | 'NotATriangle' | Pass         |
| testScaleneTriangle      | (2, 4, 5)       | 'Scalene'                                                | 'Scalene'      | Pass         |
| testIsocelesTriangleA    | (2, 2, 4)       | 'Isoceles'                                               | 'Isoceles'     | Pass         |
| testIsocelesTriangleB    | (4, 2, 2)       | 'Isoceles'                                               | 'Isoceles'     | Pass         |
| testIsocelesTriangleC    | (2, 4, 2)       | 'Isoceles'                                               | 'Isoceles'     | Pass         |
