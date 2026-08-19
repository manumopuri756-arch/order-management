import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MANOHAR@12345",
        database="ecommerce_db"
    )