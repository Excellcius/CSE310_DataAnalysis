import pandas as pd

# Load the dataset
file_path = 'healthcare_data.csv'
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())

# Analyze patient demographics
print("\nPatient Demographics:")
# Calculate demographics statistics
demographics_summary = data[['Age', 'Gender', 'Region']].describe()
print(demographics_summary)

# Analyze disease patterns
print("\nDisease Patterns:")
# Count occurrences of different diseases
disease_counts = data['Disease'].value_counts()
print(disease_counts)

# Analyze healthcare resource utilization
print("\nHealthcare Resource Utilization:")
# Calculate mean and max values of healthcare resource columns
utilization_stats = data[['Visits', 'Medications', 'LabTests']].agg(['mean', 'max'])
print(utilization_stats)
