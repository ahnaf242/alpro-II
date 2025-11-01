#import package untuk mengakses mysql
import mysql.connector

#membuat fungsi yangdigunakan untuk mengakses database dari mysql
def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="mahasiswa"
)

#membuat fungsi yang digunakan untuk mengambil dataset dari database
def mahasiswa():
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM tsd"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
