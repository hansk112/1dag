import requests
import json

# Set up the API URL and parameters
api_url = "https://services.api.business.govt.nz/insolvency-trustee-services/v1/insolvent-estates/"
api_key = "0883dbf5f9fe4e14adf060a2a5b08ec8"  # Replace <your_api_key_here> with your actual API key

api = "c242be494a7e4530a2d633554afcf049"

# It's important to replace "<your_api_key_here>" with your actual API key.
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Example query parameters
params = {
    "search": "CONEC LIMITED",  # Replace "company_name" with the actual company name you're searching for
    "pageSize": 10,  # Number of results to return<your_api_key_here>
    "pageNumber": 1  # Page number
}

# Make the API call
response = requests.get(api_url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Process the response
    data = response.json()
    
    # For demonstration, print the raw JSON data
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to fetch data: {response.status_code}")
    