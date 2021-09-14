# Deliverable 3

## What challenges did you encounter with this assignment, if any?

A challenge that I encountered was getting used to the `unittest` library. I have never written unit tests in python before, so this was a bit different for me. Getting started was the longest part, but once I understood what I needed to do, the rest was easy.

## What did you think about the requirements specification for this assignment?

I found the requirements to be helpful in understanding what the goal was. However, the requirements specification do not adequately discuss the edge cases, which is how bugs can arise. Since they weren't detailed in the document, then most likely, they will be missed. At that point, the issues will be found out through testing or in the worst case, when the product reaches the client.

I deliberately wrote the bare minimum code in `triangle.py` to demonstrate this idea. I tested the edge cases in `test.py` in the last two test functions: `test_valid_triangle` and `test_c_is_greater` where I show that these edge cases were not considered in the code I wrote.

## What challenges did you encounter with the tools?

Overall, I found the tools to be very easy and intuitive to use. I think this was the case for me because I've written frontend javascript tests for React in the past, so I have a little background in this area of software (unit testing). I just needed to adapt my knowledge to python, take a look at the `unittest` documentation, and then apply it to my code. Overall, it was a pleasant experience with no hiccups! I really like the `unittest` library and am looking forward to working with it more.

## Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?

The approach I took was to write a test case for each condition in my code. For example, I wrote a test case for each `if`/`elif` and else statement. This would test that particular condition I wrote code for. Then, I decided to take a look at any potential edge cases that I missed in the code, and then write test cases for those (testing that a user passes in a 0 for one of the arguments which is invalid, or that `c` is not the longest length of a triangle in a right triangle). Once I felt that I covered all the test cases I could think of, then I stopped.

This however still isn't an ideal situation. Due to the fact that the requirements specification wasn't thorough enough, that put a lot more weight on the developer to think of those edge cases. I may have missed an edge case or two, and this is a perfect example of how bugs can arise. In a more complex real world situation, the software in question that is being developed may not be as inuitive as a program to classify triangles, so the developer may not be able to see those edge cases as easily. That is why requirements specifications are so important to the overall process and the resulting product!
