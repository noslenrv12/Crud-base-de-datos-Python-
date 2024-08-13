import mysql.connector
from mysql.connector import Error

class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        if self._connection is None:
            try:
                self._connection = mysql.connector.connect(
                    host='localhost',
                    database='northwind',
                    user='root',
                    password='Ale12345'
                )
                if self._connection.is_connected():
                    print("Connected to MySQL database.")
                else:
                    self._connection = None  # Ensure the connection is None if failed
            except Error as e:
                print(f"Error connecting to MySQL database: {e}")
                self._connection = None
        return self._connection

    def disconnect(self):
        if self._connection is not None and self._connection.is_connected():
            self._connection.close()
            self._connection = None
