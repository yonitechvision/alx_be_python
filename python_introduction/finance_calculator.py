#!/bin/bash
monthlyIncome = float(input("Enter your monthly income:"))
monthlyExpenses = float(input("Enter your monthly expenses:"))
monthlySavings = monthlyIncome - monthlyExpenses
projectedSavings = monthlySavings*12 + monthlySavings*12*0.05
print(f"Your monthly savings are ${monthlySavings}")
print(f"Your Projected Savings after one year, with interest, is : {projectedSavings}")
