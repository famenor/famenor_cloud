from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'email': 'armando.n90@gmail.com',
    'start_date': datetime(2021, 4, 21),
    'email_on_failure': True,
}

dag = DAG('games', default_args=default_args, schedule_interval='* * * * *')

t1 = BashOperator(task_id='sklearn_pipeline', bash_command='sudo docker run sklearn_pipeline', dag=dag)