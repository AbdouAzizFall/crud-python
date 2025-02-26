import mysql.connector

from mysql.connector import Error
def Creer_une_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mabasepython"
            )
        if conn.is_connected():
            print("Connexion réussie")
        return conn
    except Error as e:
        print(f"Erreur de connexion : {e}")
        return None
