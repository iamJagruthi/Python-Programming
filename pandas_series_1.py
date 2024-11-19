import pandas as pd
#student scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]
scores_series = pd.Series(scores, index = students)
print(scores_series)
