from django.test import TestCase
import pyodbc 
# Create your tests here.
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=lab_server\sqlexpress,49173;'
                      'DATABASE=test;'
                      'UID=cat_user;'
                      'PWD=P@ssw0rd;'
                      )

cursor = conn.cursor()
cursor.execute('select * from tasktable')

for row in cursor:
    print(row)
