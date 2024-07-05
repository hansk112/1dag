from airflow.decorators import dag, task
from airflow.hooks.base import BaseHook
from airflow.sensors.base import PokeReturnValue
from datetime import datetime
import requests



@dag (

    start_date=datetime(2023, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['new_stock_market']     
)

def stock_market():
    @task.sensor(poke_interval=30, timeout=300,mode='poke')
    def is_api_available() -> PokeReturnValue:
        api = BaseHook.get_connection('stock_api')
        url = f"{api.host}{api.extra_dejson['endpoint']}"
        response = requests.get(url,headers=api.extra_dejson['headers'])
        # condition = response.json()['chart']['result'] is None

        condition = response.json()['finance']['error']['description'] == "HTTP 404 Not Found"



        # condition = response.json()

        return PokeReturnValue(is_done= condition, xcom_value=url )
    
    is_api_available()
    
# https://query1.finance.yahoo.com/v8/finance/chart
stock_market()