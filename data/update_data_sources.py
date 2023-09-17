import os
import requests
import json


def get_api_key(keyname):
    # Replace 'API_KEY' with the name of your environment variable
    try:
        api_key = os.environ.get(keyname)
    except KeyError:
        api_key = None
    return api_key


def save_json_to_file(json_data, file_path):
    try:
        with open(file_path, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON data saved to {file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")


def get_and_save_json(url, save_path):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content
            json_data = response.json()

            # Save the JSON data to the specified location
            save_json_to_file(json_data, save_path)
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to retrieve JSON data. Status code {response.status_code}"
            )
    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")


# Example usage:
# url = "https://example.com/api/data.json"  # Replace with the URL of the JSON file
# save_path = "/path/to/save/data.json"       # Replace with the desired save path and filename


baseURL = "https://data.nasdaq.com/api/v3/datasets/BCHAIN/"

dataURLs = [
    "TRFEE.json",
    "TRFUS.json",
    "MIREV.json",
    "NTRBL.json",
    "HRATE.json",
    "AVBLS.json",
    "CPTRA.json",
    "CPTRV.json",
    "MKPRU.json",
    "DIFF.json",
    "TRVOU.json",
    "ATRCT.json",

]


dataURLsName = [
    "TRFEE_Bitcoin_Total_Transaction_Fees_USD_(DAILY)",
    "TRFUS_Bitcoin_Total_Transaction_Fees_BTC_(DAILY)",
    "MIREV_Bitcoin_Miners_Revenue_USD_(DAILY)",
    "NTRBL_Bitcoin_Number_of_Transaction_per_Block_(DAILY)",
    "HRATE_Bitcoin Hash Rate_Terrahashes_(DAILY)",
    "AVBLS_Bitcoin_Average_Block_Size_(DAILY)",
    "CPTRA_Bitcoin_Cost_Per_Transaction_(DAILY)",
    "CPTRV_Bitcoin_Cost_PCT_of_Transaction_Volume_(DAILY)",
    "MKPRU_Bitcoin_Market_Price_USD_(DAILY)",
    "DIFF_Bitcoin_Difficulty_(DAILY)",
    "TRVOU_Bitcoin_Exchange_Trade_Volume_USD_(DAILY)",
    "ATRCT_Bitcoin_Median_Transaction_Confirmation_Time_in_Minutes",

]

basepath = "./dl/"

for file, filename in zip(dataURLs, dataURLsName):
# for url for url in dataURLs and name for name in dataURLsName:
    url = f"{baseURL}{file}?api_key={get_api_key('NASDAQ_API_KEY')}"
    save_path = f"{basepath}{filename}.json"
    get_and_save_json(url, save_path)
    print(url, save_path)
