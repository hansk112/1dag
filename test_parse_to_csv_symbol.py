import requests
import csv

def fetch_and_save_data():
    url = "https://financialmodelingprep.com/api/v3/search?query=AA&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
    # url_balance_sheet = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/0000320193?period=annual&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
    response = requests.get(url)
    data = response.json()
    print(data)    
    # Define the CSV file path
    csv_file_path = '/home/hans/1dag/financial_symbol.csv'
    
    # Open the CSV file for writing
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Check if data is not empty and is a list of dictionaries
        if data and isinstance(data, list) and all(isinstance(item, dict) for item in data):
            # Write the header based on keys of the first dictionary
            writer.writerow(data[0].keys())
            
            # Write the data rows
            for item in data:
                writer.writerow(item.values())
        else:
            print("Data is empty or not in the expected format")

fetch_and_save_data()