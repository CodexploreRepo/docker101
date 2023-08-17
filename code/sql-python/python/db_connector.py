import os

import mysql.connector
import psycopg2

user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
host = os.environ["DB_HOST"]
port = os.environ["DB_PORT"]
db = os.environ["DB_NAME"]

postgres_port = os.environ["POSTGRES_PORT"]

if host == "mysql":
    connection = mysql.connector.connect(
        user=user, password=password, host=host, port=port, database=db
    )
    print(f"{host} DB connected")

    cursor = connection.cursor()
    cursor.execute("Select * FROM students")
    students = cursor.fetchall()
    connection.close()

    print(students)
if host == "postgres":
    connection = psycopg2.connect(
        host=host, dbname=db, user=user, password=password, port=postgres_port
    )
    print(f"{host} DB connected")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    cursor.execute("select * from students")
    # Fetch result
    record = cursor.fetchall()
    print(record)

    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
