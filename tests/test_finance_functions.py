import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import finance_functions # type: ignore

# This is a sample unit test library
# you can run this by going into the folder and running
# python3 test_finance_functions.py   
# or use python is on windows
# this will only work if you at least have each functions tub in place (or you will need to comment out functions)

class TestFinanceFunctions(unittest.TestCase):

    def round_to_nearest_ten(self, value: float) -> float:
        """Helper function to round to nearest $10"""
        return round(value / 10) * 10

    def round_to_tenth(self, value: float) -> float:
        """Helper function to round to 0.1 precision"""
        return round(value, 1)

    def test_calculate_tax_basic(self) -> None:
        """Tests calculate_tax with basic inputs."""
        self.assertEqual(finance_functions.calculate_tax(10000, 0.10), 1000.0, "calculate_tax(10000, 0.10) expected 1000.0. Tax calculation should multiply amount by rate correctly")
        self.assertEqual(finance_functions.calculate_tax(5000, 0.12), 600.0, "calculate_tax(5000, 0.12) expected 600.0. Check your multiplication: 5000 * 0.12")
        self.assertEqual(finance_functions.calculate_tax(1000, 0.25), 250.0, "calculate_tax(1000, 0.25) expected 250.0. Ensure you're returning amount * tax_rate")


    def test_hourly_to_annual_salary_basic(self) -> None:
        """Tests hourly_to_annual_salary with standard rates."""
        self.assertEqual(finance_functions.hourly_to_annual_salary(15.0), 31200.0, "hourly_to_annual_salary(15.0) expected 31200.0. Remember: hourly_rate * 40 hours * 52 weeks")
        self.assertEqual(finance_functions.hourly_to_annual_salary(25.50), 53040.0, "hourly_to_annual_salary(25.50) expected 53040.0. Check calculation: 25.50 * 40 * 52")
        self.assertEqual(finance_functions.hourly_to_annual_salary(20.0), 41600.0, "hourly_to_annual_salary(20.0) expected 41600.0. Annual salary = hourly * 2080 total hours per year")


    def test_calculate_state_tax_basic(self) -> None:
        """Tests calculate_state_tax with basic salaries."""
        self.assertEqual(finance_functions.calculate_state_tax(60000), 3300.0, "calculate_state_tax(60000) expected 3300.0. State tax should be 5.5% of annual salary")
        self.assertEqual(finance_functions.calculate_state_tax(40000), 2200.0, "calculate_state_tax(40000) expected 2200.0. Use your calculate_tax helper function with 0.055 rate")
        self.assertEqual(finance_functions.calculate_state_tax(50000), 2750.0, "calculate_state_tax(50000) expected 2750.0. Check: 50000 * 0.055 = 2750")


    def test_suggest_food_budget_basic(self) -> None:
        """Tests suggest_food_budget with standard plans."""
        self.assertEqual(finance_functions.suggest_food_budget(1, "THRIFTY"), 200, "suggest_food_budget(1, \"THRIFTY\") expected 200. THRIFTY plan costs $200 per person")
        self.assertEqual(finance_functions.suggest_food_budget(4, "MODERATE"), 1200, "suggest_food_budget(4, \"MODERATE\") expected 1200. 4 people * $300 MODERATE = $1200")
        self.assertEqual(finance_functions.suggest_food_budget(2, "LIBERAL"), 750, "suggest_food_budget(2, \"LIBERAL\") expected 750. Check LIBERAL rate: $375 per person")


    def test_calculate_total_expenses_basic(self) -> None:
        """Tests calculate_total_expenses with standard inputs."""
        self.assertEqual(finance_functions.calculate_total_expenses(1200, 400, 500), 2100, "calculate_total_expenses(1200, 400, 500) expected 2100. Simply add all three expense amounts together")
        self.assertEqual(finance_functions.calculate_total_expenses(800, 300, 200), 1300, "calculate_total_expenses(800, 300, 200) expected 1300. Total = rent + food + other_expenses")
        self.assertEqual(finance_functions.calculate_total_expenses(1000, 500, 300), 1800, "calculate_total_expenses(1000, 500, 300) expected 1800. Check your addition: 1000 + 500 + 300")


    def test_is_budget_balanced_basic(self) -> None:
        """Tests is_budget_balanced with clear cases."""
        self.assertTrue(finance_functions.is_budget_balanced(4000, 3500), "is_budget_balanced(4000, 3500) expected True. Budget is balanced when income >= expenses")
        self.assertFalse(finance_functions.is_budget_balanced(3000, 3200), "is_budget_balanced(3000, 3200) expected False. Budget is NOT balanced when expenses > income")
        self.assertTrue(finance_functions.is_budget_balanced(5000, 5000), "is_budget_balanced(5000, 5000) expected True. Exactly equal income and expenses should return True")


    def test_calculate_leftover_money_basic(self) -> None:
        """Tests calculate_leftover_money with basic scenarios."""
        self.assertEqual(finance_functions.calculate_leftover_money(4000.0, 3500.0), 500.0, "calculate_leftover_money(4000.0, 3500.0) expected 500.0. Leftover = income - expenses")
        self.assertEqual(finance_functions.calculate_leftover_money(3000.0, 3200.0), -200.0, "calculate_leftover_money(3000.0, 3200.0) expected -200.0. Negative result when expenses exceed income")
        self.assertEqual(finance_functions.calculate_leftover_money(2500.0, 2500.0), 0.0, "calculate_leftover_money(2500.0, 2500.0) expected 0.0. Should return 0 when income equals expenses")

    def test_annual_to_monthly_basic(self) -> None:
        """Tests annual_to_monthly with standard amounts."""
        self.assertEqual(finance_functions.annual_to_monthly(60000), 5000.0, "annual_to_monthly(60000) expected 5000.0. Monthly = annual / 12")
        self.assertEqual(finance_functions.annual_to_monthly(48000), 4000.0, "annual_to_monthly(48000) expected 4000.0. 48000 ÷ 12 = 4000")
        self.assertEqual(finance_functions.annual_to_monthly(36000), 3000.0, "annual_to_monthly(36000) expected 3000.0. Check division: annual_amount / 12")

    
    def test_calculate_federal_tax_standard_values(self) -> None:
        """Tests calculate_federal_tax with standard salary amounts."""
        self.assertEqual(finance_functions.calculate_federal_tax(60000), 8817.0, "calculate_federal_tax(60000) expected 8817.0. Check your tax bracket logic for $60,000 salary")
        self.assertEqual(finance_functions.calculate_federal_tax(40000), 4594.5, "calculate_federal_tax(40000) expected 4594.5. Verify progressive tax calculation for $40,000")


    def test_calculate_federal_tax_edge_cases(self) -> None:
        """Tests calculate_federal_tax with bracket boundaries and edge cases."""
        # Test at exact bracket boundaries
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_federal_tax(10275)), 1030.0, "calculate_federal_tax(10275) should round to 1030.0. Income exactly at first bracket boundary should be 10% tax")
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_federal_tax(41775)), 4810.0, "calculate_federal_tax(41775) should round to 4810.0. Check calculation at second bracket boundary")
        
        # Test very low income
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_federal_tax(5000)), 500.0, "calculate_federal_tax(5000) should round to 500.0. Low income should only use 10% bracket")
        
        # Test zero income
        self.assertEqual(finance_functions.calculate_federal_tax(0), 0.0, "calculate_federal_tax(0) expected 0.0. Zero income should result in zero tax")

    def test_calculate_total_taxes_comprehensive(self) -> None:
        """Tests calculate_total_taxes with standard values and edge cases."""
        self.assertEqual(finance_functions.calculate_total_taxes(60000), 12117.0, "calculate_total_taxes(60000) expected 12117.0. Total should be federal + state tax")
        self.assertEqual(finance_functions.calculate_total_taxes(40000), 6794.5, "calculate_total_taxes(40000) expected 6794.5. Ensure you're adding federal and state taxes correctly")
        
        # Test very high salary - updated with correct calculation
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_total_taxes(150000)), 38080.0, "calculate_total_taxes(150000) should round to 38080.0. High salary test - check your tax bracket implementation")
        
        # Test minimal salary - corrected calculation: $20k = $1,890 fed + $1,100 state = $2,990 total
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_total_taxes(20000)), 3290.0, "calculate_total_taxes(20000) should round to 3290.0. Low salary should use early tax brackets")

    def test_calculate_monthly_take_home_comprehensive(self) -> None:
        """Tests calculate_monthly_take_home with various scenarios."""
        self.assertEqual(finance_functions.calculate_monthly_take_home(60000), 3990.25, "calculate_monthly_take_home(60000) expected 3990.25. Take-home = (salary - total_taxes) / 12")
        self.assertEqual(round(finance_functions.calculate_monthly_take_home(40000), 1), 2767.1, "calculate_monthly_take_home(40000) should round to 2767.1. Check your calculation chain: taxes -> after-tax -> monthly")
        
        # Test edge cases - updated with correct calculation
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_monthly_take_home(100000)), 6390.0, "calculate_monthly_take_home(100000) should round to 6390.0. High salary monthly calculation")
        # For $25k: total tax ~$3,265, after-tax ~$21,735, monthly ~$1,811 -> rounds to $1,810
        self.assertEqual(self.round_to_nearest_ten(finance_functions.calculate_monthly_take_home(25000)), 1740.0, "calculate_monthly_take_home(25000) should round to 1740.0. Low salary monthly take-home")

    def test_suggest_food_budget_edge_cases(self) -> None:
        """Tests suggest_food_budget with edge cases and invalid inputs."""
        # Test all plan types
        self.assertEqual(finance_functions.suggest_food_budget(3, "LOW"), 750, "suggest_food_budget(3, \"LOW\") expected 750. LOW plan costs $250 per person")
        self.assertEqual(finance_functions.suggest_food_budget(5, "THRIFTY"), 1000, "suggest_food_budget(5, \"THRIFTY\") expected 1000. 5 people * $200 THRIFTY = $1000")
        
        # Test invalid plan (should default to MODERATE)
        self.assertEqual(finance_functions.suggest_food_budget(2, "INVALID"), 600, "suggest_food_budget(2, \"INVALID\") expected 600. Invalid plan should default to MODERATE ($300/person)")
        self.assertEqual(finance_functions.suggest_food_budget(1, ""), 300, "suggest_food_budget(1, \"\") expected 300. Empty string should default to MODERATE")
        
        # Test single person all plans
        self.assertEqual(finance_functions.suggest_food_budget(1, "THRIFTY"), 200, "suggest_food_budget(1, \"THRIFTY\") expected 200. Single person THRIFTY = $200")
        self.assertEqual(finance_functions.suggest_food_budget(1, "LOW"), 250, "suggest_food_budget(1, \"LOW\") expected 250. Single person LOW = $250")
        self.assertEqual(finance_functions.suggest_food_budget(1, "MODERATE"), 300, "suggest_food_budget(1, \"MODERATE\") expected 300. Single person MODERATE = $300")
        self.assertEqual(finance_functions.suggest_food_budget(1, "LIBERAL"), 375, "suggest_food_budget(1, \"LIBERAL\") expected 375. Single person LIBERAL = $375")

    def test_hourly_to_annual_edge_cases(self) -> None:
        """Tests hourly_to_annual_salary with edge cases."""
        # Test minimum wage scenarios
        self.assertEqual(finance_functions.hourly_to_annual_salary(7.25), 15080.0, "hourly_to_annual_salary(7.25) expected 15080.0. Minimum wage calculation: 7.25 * 40 * 52")
        
        # Test very high hourly rate
        self.assertEqual(finance_functions.hourly_to_annual_salary(100.0), 208000.0, "hourly_to_annual_salary(100.0) expected 208000.0. High rate: 100 * 40 * 52 = 208000")
        
        # Test fractional rates - using round to 0.1 precision
        self.assertEqual(finance_functions.hourly_to_annual_salary(12.75), 26520.0, "hourly_to_annual_salary(12.75) expected 26520.0. Handle decimal hourly rates correctly")
        self.assertEqual(self.round_to_tenth(finance_functions.hourly_to_annual_salary(18.33)), 38126.4, "hourly_to_annual_salary(18.33) should round to 38126.4. Calculation with decimals: 18.33 * 40 * 52")

    def test_calculate_tax_edge_cases(self) -> None:
        """Tests calculate_tax with edge cases including zero values."""
        # Test zero tax rate
        self.assertEqual(finance_functions.calculate_tax(10000, 0.0), 0.0, "calculate_tax(10000, 0.0) expected 0.0. Zero tax rate should result in zero tax")
        
        # Test zero amount
        self.assertEqual(finance_functions.calculate_tax(0, 0.25), 0.0, "calculate_tax(0, 0.25) expected 0.0. Zero amount should result in zero tax")
        
        # Test high tax rates
        self.assertEqual(finance_functions.calculate_tax(10000, 0.50), 5000.0, "calculate_tax(10000, 0.50) expected 5000.0. 50% tax rate: 10000 * 0.50 = 5000")
        
        # Test small amounts
        self.assertEqual(finance_functions.calculate_tax(100, 0.10), 10.0, "calculate_tax(100, 0.10) expected 10.0. Small amount calculation: 100 * 0.10 = 10")


    def test_budget_analysis_complex_scenarios(self) -> None:
        """Tests budget functions with complex real-world scenarios."""
        # High income, high expenses
        monthly_income = 8000.0
        total_expenses = 7500.0
        self.assertTrue(finance_functions.is_budget_balanced(monthly_income, total_expenses), "is_budget_balanced(8000.0, 7500.0) expected True. 8000 income vs 7500 expenses should be balanced")
        self.assertEqual(finance_functions.calculate_leftover_money(monthly_income, total_expenses), 500.0, "calculate_leftover_money(8000.0, 7500.0) expected 500.0. Leftover should be 8000 - 7500 = 500")
        
        # Low income, exactly balanced
        monthly_income = 2500.0
        total_expenses = 2500.0
        self.assertTrue(finance_functions.is_budget_balanced(monthly_income, total_expenses), "is_budget_balanced(2500.0, 2500.0) expected True. Equal income and expenses should be balanced")
        self.assertEqual(finance_functions.calculate_leftover_money(monthly_income, total_expenses), 0.0, "calculate_leftover_money(2500.0, 2500.0) expected 0.0. Equal amounts should result in zero leftover")
        
        # Complex expense calculation
        rent = 1500.0
        food = 600.0
        other = 1200.0
        total = finance_functions.calculate_total_expenses(rent, food, other)
        self.assertEqual(total, 3300.0, "calculate_total_expenses(1500.0, 600.0, 1200.0) expected 3300.0. Total expenses: 1500 + 600 + 1200 = 3300")



if __name__ == '__main__':
    unittest.main()