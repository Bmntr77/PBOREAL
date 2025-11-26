# models/model.py
from models.db import Database

class Orang:
    def __init__(self, nama):
        self._nama = nama
    
    def info(self):
        return f"Nama: {self._nama}"

class Pelanggan(Orang):
    def __init__(self, nama, kendaraan):
        super().__init__(nama)
        self.__kendaraan = kendaraan
    
    def info(self):
        return f"Pelanggan: {self._nama}, Kendaraan: {self.__kendaraan}"
    
    def get_kendaraan(self):
        return self.__kendaraan

class Mekanik(Orang):
    def __init__(self, nama, spesialisasi):
        super().__init__(nama)
        self.__spesialisasi = spesialisasi
    
    def info(self):
        return f"Mekanik: {self._nama}, Spesialisasi: {self.__spesialisasi}"
    
    def servis(self, pelanggan):
        return f"{self._nama} sedang memperbaiki {pelanggan.get_kendaraan()} milik {pelanggan._nama}"

class Bengkel:
    def __init__(self, nama_bengkel):
        self.__nama_bengkel = nama_bengkel
        self.db = Database()  # koneksi database

        # inisialisasi tabel jika belum ada
        self._init_db()

    def _init_db(self):
        # Tabel mekanik
        query_mekanik = """
        CREATE TABLE IF NOT EXISTS mekanik (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            spesialisasi VARCHAR(50) NOT NULL
        )
        """
        self.db.execute(query_mekanik)

        # Tabel pelanggan
        query_pelanggan = """
        CREATE TABLE IF NOT EXISTS pelanggan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            kendaraan VARCHAR(50) NOT NULL
        )
        """
        self.db.execute(query_pelanggan)

    # --- Tambah data ke database ---
    def tambah_mekanik(self, mekanik: Mekanik):
        query = "INSERT INTO mekanik (nama, spesialisasi) VALUES (%s, %s)"
        self.db.execute(query, (mekanik._nama, mekanik._Mekanik__spesialisasi))

    def tambah_pelanggan(self, pelanggan: Pelanggan):
        query = "INSERT INTO pelanggan (nama, kendaraan) VALUES (%s, %s)"
        self.db.execute(query, (pelanggan._nama, pelanggan._Pelanggan__kendaraan))

    # --- Ambil daftar dari database ---
    def get_daftar_mekanik(self):
        query = "SELECT * FROM mekanik"
        mekanik_list = self.db.fetch_all(query)
        # kembalikan format info string untuk kompatibilitas controller/view
        return [f"Mekanik: {m['nama']}, Spesialisasi: {m['spesialisasi']}" for m in mekanik_list]

    def get_daftar_pelanggan(self):
        query = "SELECT * FROM pelanggan"
        pelanggan_list = self.db.fetch_all(query)
        return [f"Pelanggan: {p['nama']}, Kendaraan: {p['kendaraan']}" for p in pelanggan_list]

    def get_nama_bengkel(self):
        return self.__nama_bengkel
