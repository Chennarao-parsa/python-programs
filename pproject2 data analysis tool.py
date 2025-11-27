'''Project: data Analysis Tool
Which can perform
❖ Import and clean data
❖ Perform statistical analysis
❖ Visualize using matplotlib
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'diabetesclassification.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display basic information about the dataset
print("\nDataset info:")
print(data.info())

# Data Cleaning
# Drop rows with missing values
data_cleaned = data.dropna()
# Drop duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

print("\nDataset after cleaning:")
print(data_cleaned.info())

# Statistical Analysis
# Display summary statistics
print("\nSummary statistics:")
print(data_cleaned.describe())

# Select only numeric columns for correlation calculation
numeric_data = data_cleaned.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Data Visualization
# Histogram of a specified column
column_name = 'age'  # ← replace with your column name
plt.figure(figsize=(10, 6))
plt.hist(data_cleaned[column_name], bins=30, edgecolor='k', alpha=0.7)
plt.title(f'Histogram of {column_name}')
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.show()

# Scatter plot between two specified columns
x_column = 'bmi'   # ← replace with your x column name
y_column = 'blood_glucose_level'  # ← replace with your y column name
plt.figure(figsize=(10, 6))
plt.scatter(data_cleaned[x_column], data_cleaned[y_column], alpha=0.7)
plt.title(f'Scatter plot between {x_column} and {y_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.index)), correlation_matrix.index)
plt.title('Correlation Heatmap')
plt.show()
