def calculate_tax(income):
  if income <= 12571:
      tax_amount = 0
    
  elif income <= 14876:
      tax_amount = (income - 12571) * 0.19
    
  elif income <= 26561:
      tax_amount = (income - 14876) * 0.20 + (14876 - 12571) * 0.19
    
  elif income <= 43662:
      tax_amount = (income - 26561) * 0.21 + (26561 - 14876) * 0.20 + (14876 - 12571) * 0.19
    
  elif income <= 75000:
      tax_amount = (income - 43662) * 0.41 + (43662 - 26561) * 0.21 + (26561 - 14876) * 0.20 + (14876 - 12571) * 0.19
    
  elif income <= 125140:
      tax_amount = (income - 75000) * 0.46 + (75000 - 43662) * 0.41 + (43662 - 26561) * 0.21 + (26561 - 14876) * 0.20 + (14876 - 12571) * 0.19
    
  elif income > 125140:
      tax_amount = (income - 125140) + (125140 - 75000) * 0.46 + (75000 - 43662) * 0.41 + (43662 - 26561) * 0.21 + (26561 - 14876) * 0.20 + (14876 - 12571) * 0.19
    

  return tax_amount

def calcBrackets(income):
  if income <= 12571:
    print("You are in the no tax bracket", )

  elif income <= 14876:
    print("You are in the 'Starter Rate' tax bracket", )

  elif income <= 26561:
    print("You are in the 'Scottish Basic Rate' tax bracket", )

  elif income <= 43662:
    print("You are in the 'Intermediate Rate' tax bracket", )

  elif income <= 75000:
    print("You are in the 'Higher Rate' tax bracket", )

  elif income <= 125140:
    print("You are in the 'Advanced Rate' tax bracket", )

  elif income > 125140:
    print("You are in the 'Top Rate' tax bracket", )

# Get user input for income
income = float(input("Enter your income: "))

# Calculate the tax amount
tax_amount = calculate_tax(income)

#calculate what tax bracket the user is in
calcBrackets(income)

# Print the tax amount
print("The tax you pay is: £", tax_amount)
print("Your take home pay is: £", income - tax_amount)
