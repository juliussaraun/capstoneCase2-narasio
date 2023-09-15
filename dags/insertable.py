# importing psycopg2 module
import psycopg2
from data import data_final
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime

def ingest():
    # establishing the connection
    conn = psycopg2.connect(
        database="capstone_Project",
        user='airflow',
        password='airflow',
        host='172.19.0.3',
        port='5432'
    )

    # creating a cursor object
    cursor = conn.cursor()

    # list that contain records to be inserted into table
    data = [data_final]

    # inserting record into employee table
    for d in data:
        cursor.execute("INSERT into current_price(disclaimer,chart_name,time_updated,time_updated_iso,bpi_usd_code,bpi_usd_description,bpi_usd_rate_float,bpi_gbp_code,bpi_gbp_description,bpi_gbp_rate_float,bpi_eur_code,bpi_eur_description,bpi_eur_rate_float,bpi_idr_rate_float,last_update) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", d)

    print("List has been inserted to employee table successfully...")

    # Commit your changes in the database
    conn.commit()

    # Closing the connection
    conn.close()

# ingest()
# establishing the connection

default_args = {
    'owner': 'noname',
    'start_date': datetime.now(),
    'retries': 3,
}

dag = DAG(
    'case_2',
    default_args=default_args,
    description='How to use the Python Operator?',
    schedule_interval='@hourly',
)

t1 = PythonOperator(
    task_id='narasio',
    python_callable= ingest,
    dag=dag,
)

t1