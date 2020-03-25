from django.test import TestCase

import pyodbc
# Create your tests here.

def testdb():
    Database={
        'jimmy':{
            'server': 'tcp:commlabfortest.duckdns.org\SQLEXPRESS,49173',
            'database':'test',
            'username':'cat_user',
            'password':'P@ssw0rd',
        },
        'testdb':{
            'server': 'tcp:lab_server\SQLEXPRESS,49173',
            'database': 'test',
            'username': 'cat_user',
            'password': 'P@ssw0rd',
        }
    }
    server = 'tcp:lab_server\SQLEXPRESS,49173'
    database = 'test'
    username = 'cat_user'
    password = 'P@ssw0rd'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                        server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * from cat_info")
    row = cursor.fetchall()
    row = list(row)
    while row:
        print(row.pop())

testdb()
