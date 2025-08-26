# Homework 3 - Functions 

**Divide-Conquer-Glue** whenever we talk about programming, those three terms are at the heart of what we do. Take a problem,
break it into smaller, more abstract parts, conquer those parts, and glue them back together to solve the original problem. That is the heart of programming, and the mindset you need with functions! 

As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!

## Financial Budgeting Application 

For this assignment, you are tasked with writing a set of functions to help with a larger Financial Budgeting Application. Each function you will write will be in the file [finance_functions.py](../src/finance_functions.py). For each function, you will need to think about defining the function, documenting the function including examples, implementing the function, and then testing it (based on the examples you added). 

We have set up the file so that it will run your tests every time you run the file, and it will run the tests based on the examples you provide. That will help you focus on the first three steps of the four-step mantra. 

To get you started, we have already defined a few functions for you, and added **incomplete** docstrings. You will want to read through the function, docstring, and then:
1. Add more examples - every one needs at least 4
2. Implement the function (and then test by running the file)

The ones we have provided are:
* **calculate_tax(float, float)->float**: Requires a float for amount and tax rate, and returns the tax at the given rate. 
* **hourly_to_annual_salary(float)->float**: Takes in an hourly rate, calculates the annual rate based on a 40-hour work week and 52 weeks a year. Returns the yearly rate.
* **annual_to_monthly(float)->float**: Takes in a yearly rate, divides it by 12 and returns the result. 
* **calculate_federal_tax(float)->float**: Calculates the federal tax rate based on the 2025 US brackets. The way the rate is calculated is that it is 10% on the first \$10,275 made (single filers), then 12% on amounts above that until \$41,775. So let's say someone makes \$37,000 a year, they would pay 0.10 * \$10,275, and then 0.12 * (\$37,000 - \$10,275). The sum returned would be $4,234.50 (assume no deductions or credits). There are multiple ways to implement this with if/elif statements, but one can also think about it as a running calculation. You do NOT need lists, nor should you use a list to do this. 
* **suggest_food_budget(int, str) -> int**: Takes in a number of people and string for a plan id. Returns the rate times number of people. 

> [!NOTE]
> Think about how we took the definition of function(parameter, parameter...) -> return 
> type, and converted into the actual function in python. This is a very common way
> to list functions in design documents, and a good format to get used to. 

You will also need to implement the following functions. Note that you will need to define and fully document all of them!

* **calculate_state_tax(float)->float**: Calculate the state tax rate. To simplify it, our fictitious state taxes at a 5.5% flat tax rate. As such, any annual amount will just be taxed at 5.5%. It will be based on the gross yearly income amount, no adjustments. 
* **calculate_total_taxes(float)->float**: Takes in an annual salary, returns the total taxes (both federal and state). Consider just calling other functions and returning the sum of those results. 
* **calculate_monthly_take_home(float)->float**: Annual salary minus taxes. Takes in the annual salary, and returns the amount minus state and federal taxes at the monthly rate. Consider calling the three associated functions for this. 
* **calculate_total_expenses(float, float, float)->float**: Provides the summation of rent, food, and other_expenses. You do not have to calculate the expenses, they are provided, you only need to return the summation of the three. 
* **is_budget_balanced(float, float) -> bool**: Takes in monthly income and monthly expenses - and returns True if the income - expenses >= 0, or False if < 0. Consider using calculate_leftover_money 
* **calculate_leftover_money(float, float) -> float**: Takes in monthly income and monthly expenses, returns the result of income - expenses.

Many of these functions are 1-3 lines, except for federal taxes and suggested food budget. That is intentional in the design. This is more about process than overly complex functions.

> **Just implementing functions?**  
> Yes, you are looking at the small/zoomed in part of the greater application. 
> View this as a designer who handed you a quick specification and asked you to 
> implement them. 

> [!IMPORTANT]
> Make sure to run the code as you write / after **every** function. Doing so will generate output for you to see on the command line. In fact, if you run it without changes you will see...
> ```
> **********************************************************************
> 5 items had failures:
>   2 of   2 in __main__.annual_to_monthly
>   2 of   2 in __main__.calculate_federal_tax
>   2 of   2 in __main__.calculate_tax
>   2 of   2 in __main__.hourly_to_annual_salary
>   3 of   3 in __main__.suggest_food_budget
> 11 tests in 6 items.
> 0 passed and 11 failed.
>***Test Failed*** 11 failures.
> ```
> Along with information on each test ran! Needless to say, it is important to make sure each function passes all tests, before moving onto the next function!


## Running Unit Tests
We have provided unit tests in [tests/test_financial_functions.py](../tests/test_finance_functions.py) to run after you have finished the application. You can run those tests in VS code or via the command line. Ideally your code should pass all of them. If it does not, you will want to evaluate why not. Looking through them will also help you think of edge cases you may have forgotten in your examples. 

## Running the Larger Application
Once you have **fully** completed the finance functions, you can run the larger application by running [budget_planner.py](../src/budget_planner.py). This can be run via vs code or via the command line. If running on the command line, you can do the following

```
> python3 budget_planner.py
```

or on windows
```
> python budget_planner.py
```

For both you need to be in the `src` directory! So you may have to first do the following `cd src` in the terminal (depending on where it starts). 



## Report.md and README.md

👉🏽 **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files. 


As always you are free to ask about the questions in MS Teams, including clarifications on the code. 

## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1) 
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file). 

## 🤖 Use of LLMs
You should **not** use LLMs for writing your code. This is about learning the process, and without learning the process you may find it actually more difficult to generate code with LLMs. This is because the prompts for LLMs need to be exact, or they will make faulty assumptions about the code you are trying to generate (often generating incorrect test cases!). 

You are free to use LLMs to help you think of edge cases  **after** you have a working function. An example prompt could be:

> Please evaluate the following function focusing on these specific areas:
>
> 1. **Code correctness**: Does the implementation match the docstring description?
> 2. **Docstring completeness**: Are the parameters, return value, and examples clear and accurate?
> 3. **Edge cases**: What boundary conditions or unusual inputs could cause issues?
>
> For any edge cases you identify:
> - Explain why they're problematic
> - Show what would happen with specific input examples
> - Suggest how to handle them (documentation or code changes)
>
> Focus your feedback on the most important issues first. Assume this is for a beginner programming course at week 3 of our learning. We have not covered error checking yet, 
> nor should I include specialized statements for invalid input.
>
> (then paste in the single function you are looking at)

As part of your learning process, another example prompt could be:

> Can you describe a Python function to me, explaining each component: function signature, type hints, docstring structure, and examples. Use a function from basic programming (like math, string manipulation, or simple calculations) as your example.
>
> After your explanation, I want you to ask me THREE questions, but present them ONE AT A TIME. Wait for my response to each question before asking the next one.
> 
> Question requirements:
> 1. First question: Test my understanding of function components
> 2. Second question: Give me a function specification (including purpose, parameters, 
> return type, and expected behavior) and ask me to write ONLY the function definition with complete docstring - no implementation needed
> 3. Third question: Ask me to analyze or improve something about function design
> 
> For question 2, evaluate my docstring on these criteria:
> - Clear description of what the function does
> - Proper parameter documentation with types
> - Clear return value description  
> - Appropriate examples that demonstrate usage
> - Follows standard Python docstring format
> 
> Be specific in your feedback about what's missing or could be improved.

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
   * No magic numbers are used in finance_functions.py
   * Functions are DRY (make sure to call other functions as needed instead of duplicating code)


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