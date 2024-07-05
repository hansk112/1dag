import requests
import csv

def fetch_and_save_data():
    symbols_file_path = '/home/hans/1dag/financial_data.csv'
    
    with open(symbols_file_path, mode='r', newline='') as symbols_file:
        reader = csv.reader(symbols_file)
        try:
            next(reader)  # Attempt to skip the header
        except StopIteration:
            print("CSV file is empty or only contains a header.")
            return  # Exit the function
        
        for row in reader:
            symbol = row[0]
            url_balance_sheet = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
            response = requests.get(url_balance_sheet)
            data = response.json()
            
            csv_file_path = f'/home/hans/1dag/financial_data_bs_{symbol}.csv'
            # The rest of your code to process and save the data

fetch_and_save_data()