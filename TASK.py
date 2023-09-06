def calculate_tax(income):
    if income <= 12500:
        tax_amount = 0
    elif income <= 14585:
        tax_amount = (income - 12500) * 0.19
    elif income <= 25158:
        tax_amount = (income - 14585) * 0.20 + (14585 - 12500) * 0.19
    elif income <= 43430:
        tax_amount = (income - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
    elif income <= 150000:
        tax_amount = (income - 43430) * 0.41 + (43430 - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
    else:
        tax_amount = (income - 150000) * 0.46 + (150000 - 43430) * 0.41 + (43430 - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19

    return tax_amount

# Get user input for income
income = float(input("Enter your income: "))

# Calculate the tax amount
tax_amount = calculate_tax(income)

# Print the tax amount
print("Your tax amount is:", tax_amount)
