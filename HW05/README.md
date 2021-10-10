# Report

## Summary

I found this exercise to be helpful in seeing how the code I've written could be improved. My code coverage reached 100% coverage on the inital run of the tool `Coverage.py` on `TestTriangle.py`, so I didn't need to add any additional tests, but I did have a lot to fix after my initial run of `Pylint`.

## Detailed Analysis

**1.** Analyzed: https://github.com/elenirotsides/SSW-567/tree/main/HW02
**2.** Static code analyzer tool I used: `Pylint`

Output of initial run:
_(Please note: in the output it says "previous run: ....." but that's beacuase I ran it once before to test that pylint was working. This is indeed my first true run of this tool.)_

```
************* Module Triangle
Triangle.py:15:91: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:16:19: C0303: Trailing whitespace (trailing-whitespace)
Triangle.py:1:0: C0103: Module name "Triangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:13:0: C0103: Function name "classifyTriangle" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:13:0: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:13:0: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:13:0: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
Triangle.py:51:4: R1705: Unnecessary "elif" after "return" (no-else-return)
Triangle.py:13:0: R0911: Too many return statements (8/6) (too-many-return-statements)

------------------------------------------------------------------
Your code has been rated at 4.38/10 (previous run: 4.38/10, +0.00)
```

**3.** Code coverate tool I used: `Coverage.py`

Output of initial run:

```
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
TestTriangle.py      45      0   100%
Triangle.py          17      0   100%
-----------------------------------------------
TOTAL                62      0   100%
```

**4.** I did not need to add any additional test cases since my original test cases achieved over 80% code coverage, according to `Coverage.py`. The test cases can be found at https://github.com/elenirotsides/SSW-567/blob/main/HW02/TestTriangle.py .

**5.1.** Static Code analysis report on original program:

![static code analysis on original program](/HW05/pylint_initial.png)
_I redirected the output of the pylint results into a txt file._

**5.2** Code coverage report on original program:

![code coverage report on original program](/HW05/coverage_initial.png)
_I redirected the output of the code coverage results into a txt file._

You can also view an enhanced version of this report by running `HW05/htmlcov/index.html` in your browser.

**5.3.** Static Code analysis report after changes have been applied:

First attempt:
![code coverage report on first attempt](/HW05/pylint_second_results.png)

Second attempt:
![code coverage report on second attempt](/HW05/pylint_third_results.png)

Third attempt:
![code coverage report on third attempt](/HW05/pylint_fourth_results.png)

Fourth attempt:
![code coverage report on fourth attempt](/HW05/pylint_fifth_results.png)

Fifth attempt:
![code coverage report on fifth attempt](/HW05/pylint_sixth_results.png)

Sixth attempt:
![code coverage report on seventh attempt](/HW05/pylint_seventh_results.png)

I had to run pylint many times because I wasn't successful the first time. It took me 7 tries to get my code up to par!

**5.4.** Code coverage report after changes have been applied:

N/A since it was 100% on the first attempt!

_Note: all of the screenshots and files I mention in this report can be found in the root of this homework's directory!_
