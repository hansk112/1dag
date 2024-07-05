# Importing necessary libraries from Airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Defining the DAG
dag = DAG(
    'bash_operator_example',  # DAG ID
    default_args=default_args,
    description='A simple tutorial DAG with BashOperator',
    schedule_interval=timedelta(days=1),  # This DAG will run daily
)

# Task 1: Print the current date and time
task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task 2: Print the current date in YYYY-MM-DD format
task2 = BashOperator(
    task_id='print_formatted_date',
    bash_command='date "+%Y-%m-%d"',
    dag=dag,
)

# Task 3: Print the current time in HH:MM:SS format
task3 = BashOperator(
    task_id='print_time',
    bash_command='date "+%H:%M:%S"',
    dag=dag,
)

# Setting up the task dependencies
task1 >> task2 >> task3