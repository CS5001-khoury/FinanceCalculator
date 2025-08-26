# Homework 03 - Report


Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you open up IDLE or the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)

1. Thinking about functions, a common design is to have functions that do one thing and do it well.  This is called the Single Responsibility Principle.  What are some advantages of this design?  

2. Looking at the Single Responsibility Principle, why would it be bad design to have a function both print and return a value?

3. In practice, prints are often isolated to a certain set of functions, and every other function returns values - including strings to print. While we did not follow this rule strictly for this assignment, what are some advantages of this design?

4. A **pure** function is defined as
   * the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams), and
   * the function has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).

    4.1 What are some advantages of writing pure functions? Think about testing, and correctness.

    4.2 Are the functions in finance_functions.py pure functions? If there are exceptions list them.

    4.3 Are the functions in budget_planner pure functions? 

5. Take a look at the following code:
    ```python
    def get_name(which):
        if which == 1:
            which = 13
            return "Who"
        else:
            which = 3
            return "Strange"

    def welcome():
        print("Welcome Doctor?")
        which = 0
        name = get_name(1)
        print(which)
        print(f"Doctor {name}")
    
    welcome() ## execute the above
    ```
    Here is a link if you want to visualize it: [Visualize](https://pythontutor.com/render.html#code=def%20get_name%28which%29%3A%0A%20%20%20%20if%20which%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20which%20%3D%2013%0A%20%20%20%20%20%20%20%20return%20%22Who%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20which%20%3D%203%0A%20%20%20%20%20%20%20%20return%20%22Strange%22%0A%0Adef%20welcome%28%29%3A%0A%20%20%20%20print%28%22Welcome%20Doctor%3F%22%29%0A%20%20%20%20which%20%3D%200%0A%20%20%20%20name%20%3D%20get_name%281%29%0A%20%20%20%20print%28which%29%0A%20%20%20%20print%28f%22Doctor%20%7Bname%7D%22%29%0A%0Awelcome%28%29%20%23%23%20execute%20the%20above&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

    5.1 What is printed on `print(which)`? What about `print(f"Doctor {name}")` (really, use the visualizer)? 

    5.2 Why is this the case?

6. In budget_planner.py there are a number of variables at the top before any functions.

    6.1 What is the scope of those variables? 

    6.2 Look up the term "magic number". What does it mean? How do variables like the ones shown help reduce magic numbers?

    > You should make sure your finance_functions.py doesn't have any magic numbers!

7. Designing code can be hard. Look up and find at least two articles online that talk about how to design / write code - provide the links and a short paragraph describing what they suggest. 


## Deeper Thinking

If this calculator stored user data, how would you verify someone's identity? Research multi-factor authentication, biometrics, and session management in banking apps.  Pick one particular authentication feature, and find a few links about it. They can be a video on the topic, a link describing how it is accomplished, etc. Then in your own words (about a paragraph) describe what you learned. Note, you should answer as a paragraph, not as bullet points! This question is both meant to help you learn more about security as a domain, and to help you improve your research capabilities. 

