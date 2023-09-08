import json

# Specify the path to your JSON file
json_file_path = 'data.json'

# Load JSON data from the file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)["dataset"]["data"]

# Initialize a dictionary to store the yearly sums
yearly_sums = {}

# Iterate through the data and calculate yearly sums
for entry in data:
    date = entry[0]
    value = entry[1]
    year, month, _ = date.split("-")

    if year in yearly_sums:
        yearly_sums[year][int(month) - 1] += value
    else:
        yearly_sums[year] = [0] * 12
        yearly_sums[year][int(month) - 1] = value

# Print the yearly sums
for year, monthly_values in yearly_sums.items():
    print(f"{year} = {monthly_values}")