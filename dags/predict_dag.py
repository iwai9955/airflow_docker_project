from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.insert(0, "/opt/airflow/scripts")
from predict_model import predict_ev_demand

default_args = {
    'owner': 'soobok',
    'depends_on_past': False,
    'start_date': datetime(2025, 6, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG(
    dag_id='predict_ev_demand_daily',
    default_args=default_args,
    description='Daily EV demand prediction DAG',
    schedule='0 8 * * *',
    catchup=False,
)

predict_task = PythonOperator(
    task_id='predict_ev_demand',
    python_callable=predict_ev_demand,
    dag=dag,
)

# Airflow pipeline (ELT+ML) complete!