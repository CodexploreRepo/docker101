import os

import mysql.connector

user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
db = os.environ['DB_NAME']

connection = mysql.connector.connect(
    user=user, password=password, host=host, port=port, database=db
)
print("DB connected")

cursor = connection.cursor()
cursor.execute("Select * FROM students")
students = cursor.fetchall()
connection.close()

print(students)

