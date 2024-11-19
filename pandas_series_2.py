import pandas as pd
#Expenses categories
categories= ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
#monthly expenses data
expenses = [500, 200, 1200, 300, 150]
monthly_expenses = pd.Series(expenses, index = categories)
print(monthly_expenses)
