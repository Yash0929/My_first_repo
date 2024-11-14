#Reading CSV files
# Using pandas library

import pandas

df = pandas.read_csv('Data.csv')
#print(dataframe)
# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Filter rows where Age is greater than 30
print("\nEmployees older than 30:")
print(df[df['Age'] > 30])

# Group by Department and calculate average Salary
print("\nAverage salary by department:")
print(df.groupby('Department')['Salary'].mean())

# Save a filtered dataset to a new CSV
filtered_df = df[df['Gender'] == 'Female']
filtered_df.to_csv('female_employees.csv', index=False)