import mysql.connector
from mysql.connector import Error

# replace the strings in user and password with your personal mysql server datas
def connect_to_DB():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       user='',
                                       password='')
        if conn.is_connected():
            print("Connection established...")
            return conn
    except Error as e:
        print(e)
    finally:
        # con.close()
        pass