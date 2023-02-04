import csv
import json

csv_file_path = "sample.csv"
json_file_path = "sample.json"

# Read the CSV file
data = {}
appender = []
with open(csv_file_path) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        key = row['student']
        data[key] = row

# Add csv data to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
