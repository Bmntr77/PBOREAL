import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",      # ganti sesuai host
                user="root",           # ganti sesuai username
                password="",           # ganti sesuai password
                database="db_bengkel_bimo"
            )
            if self.conn.is_connected():
                print("✅ Berhasil terkoneksi ke database")
                self.cursor = self.conn.cursor(dictionary=True)
        except Error as e:
            print(f"❌ Gagal koneksi ke database: {e}")
            self.conn = None
            self.cursor = None

    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Error as e:
            print(f"❌ Error saat eksekusi query: {e}")

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
