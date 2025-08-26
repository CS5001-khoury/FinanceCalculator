""" 
This is a simple budget planner app. In order to run the application, from the command  line run

python3 budget_planner.py 

(or python budget_planner.py if in windows)

"""
LEFT_OVER_GOOD = 500
NO_LEFT_OVER = 0
HOUSING_RULE = 0.3


from finance_functions import *


def get_salary_information() -> float:
    """
    Get user's salary information (hourly or annual) and return annual salary.
    
    Returns:
        float: Annual salary
    """
    print("STEP 1: Income Information")
    print("-" * 25)
    
    salary_type = input("Do you want to enter (H)ourly wage or (A)nnual salary? ").upper().strip()
    
    if salary_type == "H":
        hourly_wage = float(input("Enter your hourly wage: $"))
        annual_salary = hourly_to_annual_salary(hourly_wage)
        print(f"Based on 40 hours/week, your annual salary is: ${annual_salary:,.2f}")
    else:
        annual_salary = float(input("Enter your annual salary: $"))
    
    return annual_salary


def display_take_home_pay(annual_salary: float) -> float:
    """
    Calculate and display monthly take-home pay.
    
    Arguments:
        annual_salary (float): Annual salary before taxes
        
    Returns:
        float: Monthly take-home pay
    """
    monthly_take_home = calculate_monthly_take_home(annual_salary)
    print(f"Your monthly take-home pay (after taxes): ${monthly_take_home:,.2f}")
    print()
    return monthly_take_home


def get_housing_costs() -> float:
    """
    Get user's monthly housing costs.
    
    Returns:
        float: Monthly rent/mortgage amount
    """
    print("STEP 2: Housing Costs")
    print("-" * 20)
    rent = float(input("Enter your monthly rent/mortgage: $"))
    print()
    return rent


def get_food_budget() -> float:
    """
    Get user's food budget based on household size and plan choice.
    
    Returns:
        float: Monthly food budget
    """
    print("STEP 3: Food Budget")
    print("-" * 18)
    num_people = int(input("How many people are in your household? "))
    
    print("\nUSDA Food Plan Options:")
    print("1. Thrifty Plan     ($200/person/month)")
    print("2. Low-Cost Plan    ($250/person/month)")
    print("3. Moderate Plan    ($300/person/month)")
    print("4. Liberal Plan     ($375/person/month)")
    
    plan_choice = int(input("Choose a plan (1-4): "))
    
    # Convert number choice to string key
    plan_keys = {1: "THRIFTY", 2: "LOW", 3: "MODERATE", 4: "LIBERAL"}
    plan_key = plan_keys.get(plan_choice, "MODERATE")
    
    suggested_food = suggest_food_budget(num_people, plan_key)
    
    plan_names = {"THRIFTY": "Thrifty", "LOW": "Low-Cost", "MODERATE": "Moderate", "LIBERAL": "Liberal"}
    plan_name = plan_names[plan_key]
    
    print(f"\n{plan_name} Plan for {num_people} people: ${suggested_food}")
    
    use_suggested = input("Use this amount? (Y/N): ").upper().strip()
    if use_suggested == "Y":
        food_budget = suggested_food
    else:
        food_budget = float(input("Enter your custom monthly food budget: $"))
    
    print()
    return food_budget


def get_other_expenses() -> float:
    """
    Get user's other monthly expenses across various categories.
    
    Returns:
        float: Total other monthly expenses
    """
    print("STEP 4: Other Monthly Expenses")
    print("-" * 30)
    print("Let's add up your other monthly expenses...")
    
    other_expenses = 0.0
    expense_categories = [
        "Transportation (gas, bus pass, car payment)",
        "Utilities (electricity, water, internet)", 
        "Insurance (health, car, renters/home)",
        "Entertainment (movies, dining out, hobbies)",
        "Personal care (haircuts, gym, clothing)",
        "Miscellaneous (gifts, subscriptions, etc.)"
    ]
    
    for category in expense_categories:
        expense = float(input(f"Enter monthly cost for {category}: $"))
        other_expenses += expense
    
    print(f"Total other expenses: ${other_expenses:,.2f}")
    print()
    return other_expenses


def display_budget_analysis(annual_salary: float, monthly_take_home: float, rent: float, 
                          food_budget: float, other_expenses: float) -> None:
    """
    Calculate and display complete budget analysis with recommendations.
    
    Arguments:
        annual_salary (float): Annual salary before taxes
        monthly_take_home (float): Monthly take-home pay
        rent (float): Monthly rent/mortgage
        food_budget (float): Monthly food budget
        other_expenses (float): Other monthly expenses
    """
    total_expenses = calculate_total_expenses(rent, food_budget, other_expenses)
    leftover = calculate_leftover_money(monthly_take_home, total_expenses)
    is_balanced = is_budget_balanced(monthly_take_home, total_expenses)
    
    print("=" * 50)
    print("    BUDGET ANALYSIS")
    print("=" * 50)
    
    print(f"Annual Salary:           ${annual_salary:>10,.2f}")
    print(f"Monthly Take-Home:       ${monthly_take_home:>10,.2f}")
    print()
    print("MONTHLY EXPENSES:")
    print(f"  Rent/Mortgage:         ${rent:>10,.2f}")
    print(f"  Food:                  ${food_budget:>10,.2f}")
    print(f"  Other Expenses:        ${other_expenses:>10,.2f}")
    print(f"  ----------------------{'':>10}")
    print(f"  Total Expenses:        ${total_expenses:>10,.2f}")
    print()
    print(f"Money Left Over:         ${leftover:>10,.2f}")
    print()
    
    display_budget_recommendations(is_balanced, leftover, monthly_take_home, rent, 
                                 food_budget, suggest_food_budget)


def display_budget_recommendations(is_balanced: bool, leftover: float, monthly_take_home: float,
                                 rent: float, food_budget: float, suggest_food_budget_func) -> None:
    """
    Display budget recommendations based on analysis results.
    
    Arguments:
        is_balanced (bool): Whether budget is balanced
        leftover (float): Amount of money left over
        monthly_take_home (float): Monthly take-home pay
        rent (float): Monthly rent amount
        food_budget (float): Monthly food budget
        suggest_food_budget_func: Function to get suggested food budget
    """
    if is_balanced:
        if leftover > LEFT_OVER_GOOD:
            print("✅ EXCELLENT! You have a healthy budget with good savings potential.")
            print(f"   Consider saving ${leftover * 0.8:.2f} and using ${leftover * 0.2:.2f} for fun!")
        elif leftover > NO_LEFT_OVER:
            print("✅ GOOD! Your budget is balanced, but there's little room for savings.")
            print("   Consider reducing expenses to build an emergency fund.")
        else:
            print("✅ BALANCED! You're breaking even, but any unexpected expense could be problematic.")
            print("   Try to reduce some expenses to create a safety buffer.")
    else:
        print("❌ WARNING! You're spending more than you earn!")
        print(f"   You need to reduce expenses by ${abs(leftover):,.2f} per month.")
        print()
        print("SUGGESTIONS:")
        if rent > monthly_take_home * HOUSING_RULE:
            print(f"   • Housing costs ${rent:,.2f} exceed 30% rule (${monthly_take_home * 0.3:.2f})")
        suggested_moderate = suggest_food_budget_func(1, "MODERATE")  # Assume 1 person for comparison
        if food_budget > suggested_moderate * 1.2:
            print(f"   • Food budget seems high - consider reducing costs")
        print("   • Review 'other expenses' for items you can reduce or eliminate")


def display_closing_message() -> None:
    """Display closing message and tips."""
    print()
    print("=" * 50)
    print("Thank you for using the Personal Budget Planner!")
    print("Remember: A good budget is a living document - review it monthly!")
    print("=" * 50)


def main() -> None:
    """Main function to run the budget planner application."""
    print("=" * 50)
    print("    PERSONAL BUDGET PLANNER")
    print("=" * 50)
    print()
    
    # Gather all user input
    annual_salary = get_salary_information()
    monthly_take_home = display_take_home_pay(annual_salary)
    rent = get_housing_costs()
    food_budget = get_food_budget()
    other_expenses = get_other_expenses()
    
    # Display analysis and recommendations
    display_budget_analysis(annual_salary, monthly_take_home, rent, food_budget, other_expenses)
    display_closing_message()


if __name__ == "__main__":
    main()