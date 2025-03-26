from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def run_kafka_producer():
    subprocess.run(["python", "data_pipeline/kafka_producer.py"])

def run_spark_streaming():
    subprocess.run(["python", "data_pipeline/spark_streaming.py"])

def run_redshift_loader():
    subprocess.run(["python", "data_pipeline/redshift_loader.py"])

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Define DAG
dag = DAG('fraud_detection_pipeline', default_args=default_args, schedule_interval='@hourly')

# Define tasks
t1 = PythonOperator(task_id='run_kafka_producer', python_callable=run_kafka_producer, dag=dag)
t2 = PythonOperator(task_id='run_spark_streaming', python_callable=run_spark_streaming, dag=dag)
t3 = PythonOperator(task_id='run_redshift_loader', python_callable=run_redshift_loader, dag=dag)

# Set task dependencies
t1 >> t2 >> t3