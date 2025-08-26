"""
Finance Functions.

Add each function, then run the file to execute doctests. 

Name: 
Semester: 
    
"""
## the following have define and document done as examples

def calculate_tax(amount: float, tax_rate: float) -> float:
    """
    Calculate tax on a given amount at a given rate.
    
    Examples:
        >>> calculate_tax(10000, 0.10)
        1000.0
        >>> calculate_tax(5000, 0.12)
        600.0
    
    Arguments:
        amount (float): Amount to calculate tax on
        tax_rate (float): Tax rate as decimal (0.10 = 10%)
    
    Returns:
        float: Tax owed on the amount
    """
    return 0  # replace with your own implementation


def hourly_to_annual_salary(hourly_rate: float) -> float:
    """
    Convert hourly wage to annual salary (40 hrs/week, 52 weeks/year).
    
    Examples:
        >>> hourly_to_annual_salary(15.0)
        31200.0
        >>> hourly_to_annual_salary(25.50)
        53040.0
    
    Arguments:
        hourly_rate (float): Hourly wage
    
    Returns:
        float: Annual salary
    """
    return 0.0 #  replace with your own implementation


def annual_to_monthly(annual_amount: float) -> float:
    """
    Convert annual amount to monthly amount.
    
    Examples:
        >>> annual_to_monthly(60000)
        5000.0
        >>> round(annual_to_monthly(12372.5), 2)
        1031.04
    
    Arguments:
        annual_amount (float): Annual amount
    
    Returns:
        float: Monthly amount
    """
    return 0.0 # replace


def calculate_federal_tax(annual_salary: float) -> float:
    """
    Calculate federal tax owed using 2025 tax brackets.
    
    2025 Federal Tax Brackets (Single):
    - 10% on income up to $10,275
    - 12% on income $10,276 to $41,775  
    - 22% on income $41,776 to $89,450
    - 24% on income $89,451 to $190,750
    - 32% on income $190,751 to $243,725
    - 35% on income $243,726 to $609,350
    - 37% on income over $609,350
    
    Examples:
        >>> calculate_federal_tax(60000)
        8817.0
        >>> calculate_federal_tax(40000)
        4594.5
    
    Arguments:
        annual_salary (float): Annual salary before taxes
    
    Returns:
        float: Federal tax owed
    """
    return 0.0 # replace


def suggest_food_budget(num_people: int, plan_id: str) -> int:
    """
    Suggest monthly food budget based on household size and USDA plan.
    
    Plan options:
    "THRIFTY" = Thrifty Plan ($200/person/month)
    "LOW" = Low-Cost Plan ($250/person/month) 
    "MODERATE" = Moderate Plan ($300/person/month)
    "LIBERAL" = Liberal Plan ($375/person/month)
    
    Examples:
        >>> suggest_food_budget(1, "THRIFTY")
        200
        >>> suggest_food_budget(4, "MODERATE")
        1200
        >>> suggest_food_budget(2, "LIBERAL")
        750
    
    Arguments:
        num_people (int): Number of people in household
        plan_id (str): Plan type ("THRIFTY", "LOW", "MODERATE", "LIBERAL")
    
    Returns:
        int: Suggested monthly food budget
    """
    return 0.0 # replace


## add your other functions below this line, but above the main


# put your functions above this line
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
