import json
from datetime import datetime
import pandas as pd
import timeit
json_file_path = "MKPRU_Bitcoin_Market_Price_USD_(DAILY).json"


def read_json_file_and_filter(file_path, start_date=None, end_date=None):
    # Read the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)["dataset"]["data"]

    if isinstance(data, list):  # Check if the JSON data is a list
        # Check if date range is provided
        if start_date and end_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            filtered_data = [entry for entry in data if start_date <= datetime.strptime(entry[0], "%Y-%m-%d") <= end_date]
            return filtered_data
        else:
            return data
    else:
        raise ValueError("Invalid JSON data format. The data should be a list.")


def sum_second_values(table_of_tables):
    total = 0
    for inner_table in table_of_tables:
        for entry in inner_table:
            if isinstance(entry, (int, float)):
                total += entry
            elif isinstance(entry, list):
                if len(entry) > 1:
                    total += entry[1]
    return total



# * Example usage:


start_date = "2023-09-05"
end_date = "2023-09-15"

# ! Load the JSON file into a list
data_list = read_json_file_and_filter(json_file_path)

# ! To filter data by date range, provide start_date and end_date (format: "YYYY-MM-DD")
filtered_data = read_json_file_and_filter(json_file_path, start_date="2023-09-05", end_date="2023-09-07")


print(len(read_json_file_and_filter(json_file_path)))
print(read_json_file_and_filter(json_file_path, start_date="2023-09-05", end_date="2023-09-10"))

print(sum_second_values(read_json_file_and_filter(json_file_path, start_date, end_date)))

table  = read_json_file_and_filter(json_file_path, start_date, end_date)
df = pd.DataFrame(table, columns=["column1", "column2"])






# Find the minimum value in "column2"
min_value_column2 = df["column2"].min()
# Find the maximum value in "column2"
max_value_column2 = df["column2"].max()


# Find the minimum value in "column2" and get its index
min_index = df["column2"].idxmin()
# Find the maximum value in "column2" and get its index
max_index = df["column2"].idxmax()

# Get the values from "column1" at the respective indices
min_value_column1 = df.loc[min_index, "column1"]
max_value_column1 = df.loc[max_index, "column1"]

min_value_column2 = df.loc[min_index, "column2"]
max_value_column2 = df.loc[max_index, "column2"]


print("Minimum Value in column2:", min_value_column2)
print("Corresponding Value in column1:", min_value_column1)
print("Maximum Value in column2:", max_value_column2)
print("Corresponding Value in column1:", max_value_column1)


# Find the minimum and maximum values in "column2"
min_value_column2 = df["column2"].min()
max_value_column2 = df["column2"].max()



print("Minimum Value in column2:", min_value_column2)
print("Corresponding Value in column1:", min_value_column1)
print("Maximum Value in column2:", max_value_column2)
print("Corresponding Value in column1:", max_value_column1)









print(df, min_value_column2, max_value_column2)