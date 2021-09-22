import datetime as dt
import pandas as pd
import csv
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector as msql
from mysql.connector import Error

def load_data(data):
    df = pd.read_csv(data)
    return df

def to_sql():
    new_df = load_data('richards.csv')
    try:
        conn = msql.connect(host='localhost', database='davisdb', user='root', password='bo2108luwatife@1')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database:", record)
            cursor.execute('DROP TABLE IF EXISTS sensor_data;')
            print('Creating table....')
# in the below line please pass the create table statement which you want #to create
            cursor.execute("CREATE TABLE sensor_data(Date varchar(255), flow1 int(6), occupancy1 varchar(255), flow2 varchar(255), occupancy2 varchar(255), flow3 varchar(255),occupancy3 varchar(255),totalflow int, weekday int, hour int,minute int,second int)")
            print("Table is created....")
            #loop through the data frame
            for i,row in new_df.iterrows():
            #here %S means string values 
                sql = "INSERT INTO davis2.sensor_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)

# DAG's arguments
default_args = {
        'owner': 'Mubarak',
        'start_date':dt.datetime(2021, 22, 9, 9, 0, 0),
        'concurrency': 1,
        'retries': 0
        }

# DAG's operators, or bones of the workflow
with DAG('Loading data into Database',
        catchup=False, # To skip any intervals we didn't run
        default_args=default_args,
        schedule_interval='* 1 * * * *', # 's m h d mo y'; set to run every minute.
        ) as dag:

    load_csv = PythonOperator(
            task_id='Load CSV',
            python_callable=load_data,
            )

    upload_csv_to_sql = PythonOperator(
            task_id='CSV to Database',
            python_callable=to_sql
            )

# The actual workflow
load_csv >> upload_csv_to_sql