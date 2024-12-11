# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display the results
print("Your monthly savings are:", monthly_savings)
print("Your projected annual savings after interest are:", projected_savings)
