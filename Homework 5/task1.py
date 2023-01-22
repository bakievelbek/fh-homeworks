import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV file and transfer it into DataFrame.

data = pd.read_csv('data.csv')

# 2. Transfer object Series into index column of the dataframe.

data = data.set_index("PassengerId")

data.index.name = "index"

# 3. Change the data in the column of DataFrame according to some condition.

data.loc[pd.isna(data['Cabin']), 'Cabin'] = 'null'

column_names = data.columns

# 4. Get names of the DataFrame columns and sum of listed values DF.

print(f"Column names: {column_names}")

data_sum = data[column_names].sum(numeric_only=True)

print(f"Sum of listed values: {data_sum}")

# 5. Sort column by name.

data = data.sort_values(by=['Name'])

# 6. Delete upper and lowe 5% in object DataFrame.

q1, q3 = data['Age'].quantile([.05, .95])

data = data[(data['Age'] > q1) & (data['Age'] < q3)]

# 7. Fill missed values in the Column with average values.

data['Age'].fillna(data['Age'].mean(), inplace=True)

# 8.Create two data frames using the two Dicts, Merge two data frames, and append
# the second data frame as a new column to the first data frame.


# create two sample dataframes
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 30, 35, 40],
                    'Salary': [50000, 60000, 70000, 80000]})

df2 = pd.DataFrame({'Name': ['Eve', 'Frank', 'George', 'Harry'],
                    'Age': [20, 22, 28, 32],
                    'City': ['New York', 'London', 'Paris', 'Berlin']})

# merge the two dataframes using a common column
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)

# append the second dataframe as a new column to the first dataframe
appended_df = df1.assign(City=df2['City'])
print(appended_df)
#
appended_df['Name'].hist()
plt.xlabel('Name')

appended_df['Age'].hist()
plt.xlabel('Age')

appended_df['Salary'].hist()
plt.xlabel('Salary')

appended_df['City'].hist()
plt.xlabel('City')

# 10. Create Correlation Matrix for any column


corr_matrix = appended_df.corr()
print(corr_matrix)
