from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.http_sensor import HttpSensor
import requests

def get_and_print_data():
    url = "https://financialmodelingprep.com/api/v3/search?query=AA&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed to retrieve data")

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
    'financial_data_retrieval',
    default_args=default_args,
    description='A simple DAG to retrieve financial data',
    schedule_interval=timedelta(days=1),
)

check_api_availability = HttpSensor(
    task_id='check_api_availability',
    http_conn_id='financialmodelingprep_api',
    endpoint='api/v3/search?query=AA&apikey=vBBIxKRAIIQv9qw7FD2o3ds2fFl7JR1A',
    request_params={},
    response_check=lambda response: "symbol" in response.text,
    poke_interval=5,
    timeout=20,
    dag=dag
)

retrieve_and_print_data = PythonOperator(
    task_id='retrieve_and_print_data',
    python_callable=get_and_print_data,
    dag=dag,
)

check_api_availability >> retrieve_and_print_data