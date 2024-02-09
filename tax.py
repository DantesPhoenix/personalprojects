def calculate_tax(income):
  if income <= 12571:
      tax_amount = 0
  elif income <= 14876:
      tax_amount = (income - 12500) * 0.19
  elif income <= 26561:
      tax_amount = (income - 14585) * 0.20 + (14585 - 12500) * 0.19
  elif income <= 43662:
      tax_amount = (income - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
  elif income <= 75000:
      tax_amount = (income - 43430) * 0.42 + (43430 - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
  elif income <= 125140:
      tax_amount = (income - 75000) * 0.45 + (75000 - 43430) * 0.42 + (43430 - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
  else:
    tax_amount = (income - 125140) * 0.48 + (125140 - 75000) * 0.45 + (75000 - 43430) * 0.42 + (43430 - 25158) * 0.21 + (25158 - 14585) * 0.20 + (14585 - 12500) * 0.19
  

  return tax_amount

def calcBrackets(income):
    if income <= 12500:
      print("your ta")

# Get user input for income
income = float(input("Enter your income: "))

# Calculate the tax amount
tax_amount = calculate_tax(income)

#calculate what tax bracket the user is in
calcBrackets(income)

# Print the tax amount
print("The tax you pay is: £", tax_amount)
print("Your take home pay is: £", income - tax_amount)
print("your monthly pay is: ", income - tax_amount/12)
