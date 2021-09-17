# Triangle HW02a

[![build status of master](https://travis-ci.org/elenirotsides/SSW-567.svg?branch=master)](https://travis-ci.org/elenirotsides/SSW-567/tree/main/HW02)

## Report

### Assignment Description

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program. In this assignment you will start with an existing implementation of the classify triangle program that will be given to you. You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.

There are two files: `Triangle.py` and `TestTriangle.py`

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program. You will need to update the test program until you feel that your tests adequately test all of the conditions. Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is. Capture and then report on those results in a formal test report described below. For this first part you should not make any changes to the classify triangle program. You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects. Continue to run the test cases as you fix defects until all of the defects have been fixed. Run one final execution of the test program and capture and then report on those results in a formal test report described below.

Note that you should NOT simply replace the logic with your logic from Assignment 1. Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team.

### Author

Eleni Rotsides

### Summary

When I wrote and then ran my test cases in the first round of testing before code changes were made, I noticed there were lots of errors in the logic due to the amount of test cases that were failing. The test cases were a really effective way to quickly test the `Triangle.py` program to spot defects. When I saw what failed (and what didn't; there were a few false positives in there due to logic errors in the program), I was able to pinpoint the exact areas where things were going wrong, and fix them. Overall, this sped up the the testing process because it was automated, which saved me a lot of time! There is great value in writing test cases, and I'm for sure going to adopt this practice in my leisure coding acitivies (and for class assignments for my other courses).

### Honor Pledge

I pledge my honor that I have abided by the Stevens honor system.

### Detailed results

Part 1 (see below) shows a breakdown of the tests that were executed in the initial round of testing. I tested variations of similar inputs and tried to test edge cases as well. Most of the test cases failed due to logic errors that were introduced in the initial version of the program. When I ran the tests after addressing the bugs I knew were present (the unit tests made the issues very clear), everything passed. Part 2 (see below) shows a breakdown of the tests I executed the second time around after fixing the bugs and everything passed.

When writing test cases, I looked at the notes in the code to understand what was _supposed_ to happen. The code itself was unreliable since code is just an interpretation of the requirements specification; this wouldn't have been a good measure to use to write tests because someone's interpretation isn't valid, you need to look at the root and that is anywhere where the requirements are detailed out. So, I wrote my test cases based on the notes in the code in order to see what worked and what didn't. After the initial run, it was clear the the original developer misinterpretted the requirements, and so I went one-by-one and fixed the issues.

I'd also like to note that in the initial run, some tests passed, but they were false positives. `testInputsAreValidA`, `testInputsAreValidB`, and `testInputsAreValidC` all passed but shouldn't have. This can happen because logic errors don't necessarily make code fail; it can make code pass, but for the wrong reason. In this case, the conditional that was checking that the inputs were valid was written incorrectly, which was making the code pass because it didn't assess the edge cases correctly.

I think the biggest takeaway here is that test automation is a fantastic tool to speed up the process and is useful in helping developers spot issues in their code, but it shouldn't be the only metric used for assessing correctness. It is important for us to check our work and make sure it matches with the requirements specification as best we can, in addition to using these tools and techniques.

Some more details regarding qualitative metrics I discussed can be found in the Test Matrix below.

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

## Testing Matrix

|                    | Test Run 1 | Test Run 2 |
| ------------------ | ---------- | ---------- |
| **Tests Planned**  | 19         | 19         |
| **Tests Executed** | 19         | 19         |
| **Tests Passed**   | 7          | 19         |
| **Defects Found**  | 6          | 0          |
| **Defects Fixed**  | 0          | 6          |
