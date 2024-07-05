from datetime import datetime, timedelta
import requests
import csv



def fetch_and_save_data():
    url = "https://financialmodelingprep.com/api/v3/search?query=AA&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
    response = requests.get(url)
    data = response.json()
    print(data)


fetch_and_save_data()