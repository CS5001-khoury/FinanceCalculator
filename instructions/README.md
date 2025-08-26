# Homework 3 - Functions with a Finance Calculator

**Divide-Conquer-Glue** whenever we talk about programming, those three terms are at the heart of what we do. Take a problem,
break it into smaller, more abstract parts, conquer those parts, and glue them back together to solve the original problem. That is the heart of programming, and the mindset you need with functions! 

As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!




## Report.md and README.md

👉🏽 **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files. 


As always you are free to ask about the questions in MS Teams, including clarifications on the code. 

## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1) 
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file). 


## 📝 Grading Rubric

You need to submit the following files:

* [finance_functions.py](../src/finance_functions.py)
* Your Coding Practice file
* [Report.md](../Report.md)
* [README.md](../README.md) (the one with your name in it)

Note: if you haven't finished finance_functions.py, the autograder will most likely
have strange errors. Make sure you can run and pass the [test file](../tests/test_finance_functions.py) locally first
before submitting to the autograder.

### Rubric

1. Learning (AG)
   * passes basic tests
2. Approaching  (AG)
   * Passes more difficult tests including edge cases
   * passes PEP8 style check
3. Meets  (MG)
   * Every function in has at least 4 examples in docstring
   * Properly formatted docstrings exist for each function
   * Coding practice file provided
   * Report questions 1-4 answered correctly
4. Exceeds  (MG)
   * All Report questions answered properly, including links for references
   * Report deeper thinking answered with some thought, including links for references


AG - Auto-graded  
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Additional Resources

For our functions, we have been using type hints. If you are interested in learning more, feel free to follow the additional resources, but these are mostly beyond the scope of the class. Type hints were introduced in Python 3.0, but they weren't really given a purpose until Python 3.5 (PEP 484). It has become common in industry to include them even though python is a dynamically typed language. Dynamically typed means specifying the types are not required as the language will determine the memory needed at runtime. Some languages, like Java which you will learn in CS5004, are strongly typed which means the types are required and strictly enforced at time of programming (compile time). 

Adding the type hints in python is two fold. First, it makes it easier to see what is expected both as the arguments of a function and as the return value of the function. This helps you debug and helps other programmers. Second, there are tools that someone can run against your code to make sure the types are being followed, such as mypy below! This matters for large scale application development.

While not required for this course, you can learn about types hints
* [mypy](https://mypy.readthedocs.io/en/latest/)
* [typing library](https://docs.python.org/3/library/typing.html)

Above all, keep it simple! There are far more features in python than we will need. 