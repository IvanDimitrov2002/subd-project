import mysql.connector
from mysql.connector import Error


class DB:
    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='root')
            if self.conn.is_connected():
                print("Connection established... ")
                return self.conn

        except Error as e:
            print(e)

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()
