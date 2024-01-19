import os
import csv
from collections import defaultdict

# Set working directory
file_path = '/content/Student_Marks.csv'
if os.path.isfile(file_path):
    os.chdir(os.path.dirname(file_path))
else:
    raise ValueError('The file "Student_Marks.csv" does not exist.')

# Read data from CSV files
data = defaultdict(list)
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for header, value in row.items():
                    data[header].append(value)

# Check if the data set is empty
if len(data['number_courses']) == 0:
    raise ValueError('The data set is empty.')

# Perform some calculations
total_records = len(data['number_courses'])
total_Marks = 0
for value in data['Marks']:
    try:
        total_Marks += float(value)
    except ValueError:
        print(f"Error: Could not convert value '{value}' to a float.")

if total_Marks == 0:
    raise ValueError('The data set does not contain any numeric values for Marks.')

average_value = total_Marks / total_records

# Generate report
report = f'Total records: {total_records}\n'
report += f'Average value: {average_value}\n'

# Write report to file
with open('report.txt', 'w') as f:
    f.write(report)

print('Report generated.')