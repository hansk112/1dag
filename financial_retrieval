from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.http_sensor import HttpSensor
import requests
import csv

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fetch_and_parse_financial_data',
    default_args=default_args,
    description='Fetch data from API and parse into CSV',
    schedule_interval=timedelta(days=1),
)

def fetch_and_save_data():
    url = "https://financialmodelingprep.com/api/v3/search?query=AA&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
    response = requests.get(url)
    data = response.json()
    
    # Define CSV file name and write mode
    csv_file = "/path/to/your/directory/financial_data.csv"
    
    # Writing data to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Assuming the data is a list of dictionaries, write the header based on keys of the first item
        if data:
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())

fetch_data = PythonOperator(
    task_id='fetch_and_save_data',
    python_callable=fetch_and_save_data,
    dag=dag,
)

fetch_data