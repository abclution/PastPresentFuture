import json

# Specify the path to your JSON file
# json_file_path = 'data.json'
json_file_path = 'MIREV-Bitcoin Miners Revenue.json'

# Load JSON data from the file
with open(json_file_path, 'r') as json_file:
    loadedJsonData = json.load(json_file)["dataset"]["data"]

# Initialize a dictionary to store the yearly sums
yearly_sums = {}

# Iterate through the data and calculate yearly sums
for entry in loadedJsonData:
    date = entry[0]
    value = entry[1]
    year, month, day = date.split("-")

    if year in yearly_sums:
        yearly_sums[year][int(month) - 1] += value
    else:
        yearly_sums[year] = [0] * 12  #  initialize a list of 12 zeros within the yearly_sums dictionary for a specific year. 
        yearly_sums[year][int(month) - 1] = value  #  lists in Python are zero-indexed, so January is represented as 0, February as 1,

# Print the yearly sums
for year, monthly_values in yearly_sums.items():
    print(f"{year} = {monthly_values}")