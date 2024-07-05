import requests
import csv

# Define the URL for the GET request
url = "https://api.stats.govt.nz/opendata/v1"

# Send a GET request to the URL
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Specify the CSV file name
    csv_file_name = "stats_nz_data.csv"
    
    # Open a new CSV file for writing
    with open(csv_file_name, mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        
        # Assuming 'data' is a list of dictionaries, write the headers
        if data and isinstance(data, list) and isinstance(data[0], dict):
            writer.writerow(data[0].keys())  # Write headers
        
        # Iterate over the data
        for item in data:
            # Assuming each item is a dictionary, write the values
            if isinstance(item, dict):
                writer.writerow(item.values())
                
    print(f"Data successfully written to {csv_file_name}")
else:
    print("Failed to fetch data from the API")