import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Kwindaipfi071??',
    )

cursorObject =dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print('All good')
