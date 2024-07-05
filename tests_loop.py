import requests
import csv

def fetch_and_save_data():
    # Path to the CSV file with stock symbols
    symbols_file_path = '/home/hans/1dag/financial_symbol.csv'
    # hhh
    # Open and read the stock symbols from the CSV file
    with open(symbols_file_path, mode='r', newline='') as symbols_file:
        reader = csv.reader(symbols_file)
        # next(reader)  # Skip the header
        for row in reader:
            symbol = row[0]  # Assuming the symbol is in the first column
            # Modify the URL to include the current symbol
            url_balance_sheet = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
            response = requests.get(url_balance_sheet)
            data = response.json()
            print(data)
            # ?apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A 
            # apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A
            # Define the CSV file path for the current symbol's data
            csv_file_path = f'/home/hans/1dag/financial_data_bs_{symbol}.csv'
            
            # Open the CSV file for writing the current symbol's data
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
                    print(f"Data for {symbol} is empty or not in the expected format")
print("cpmpleted")
fetch_and_save_data()