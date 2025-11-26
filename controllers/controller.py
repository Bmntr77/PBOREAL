# controllers/controller.py
from models.model import Bengkel, Mekanik, Pelanggan
from views.view import View
from rich.console import Console
from rich.table import Table
from models.db import Database  

console = Console()

class BengkelController:
    def __init__(self, bengkel):
        self.bengkel = bengkel
        self.db = Database()  # koneksi ke database

        # Inisialisasi tabel jika belum ada
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
    def tambah_mekanik(self, mekanik):
        query = "INSERT INTO mekanik (nama, spesialisasi) VALUES (%s, %s)"
        self.db.execute(query, (mekanik._nama, mekanik._Mekanik__spesialisasi))
        console.print(f"[bold green]✅ Mekanik '{mekanik._nama}' berhasil ditambahkan ke database[/bold green]")

    def tambah_pelanggan(self, pelanggan):
        query = "INSERT INTO pelanggan (nama, kendaraan) VALUES (%s, %s)"
        self.db.execute(query, (pelanggan._nama, pelanggan._Pelanggan__kendaraan))
        console.print(f"[bold green]✅ Pelanggan '{pelanggan._nama}' berhasil ditambahkan ke database[/bold green]")

    # --- Input dari user ---
    def tambah_mekanik_dari_input(self):
        nama = input("Masukkan Nama Mekanik: ")
        spesialisasi = input("Masukkan Spesialisasi Mekanik (Mesin/Kelistrikan): ")
        mekanik_baru = Mekanik(nama, spesialisasi)
        self.tambah_mekanik(mekanik_baru)

    def tambah_pelanggan_dari_input(self):
        nama = input("Masukkan Nama Pelanggan: ")
        kendaraan = input("Masukkan Jenis Kendaraan Pelanggan: ")
        pelanggan_baru = Pelanggan(nama, kendaraan)
        self.tambah_pelanggan(pelanggan_baru)

    # --- Tampilkan daftar mekanik dari database ---
    def tampilkan_daftar_mekanik(self):
        query = "SELECT * FROM mekanik"
        mekanik_list = self.db.fetch_all(query)

        if not mekanik_list:
            console.print("[bold yellow]⚠ Belum ada mekanik yang terdaftar di database.[/bold yellow]")
            return

        table = Table(title="📋 Daftar Mekanik", header_style="bold magenta")
        table.add_column("No", justify="center", style="bold cyan")
        table.add_column("Nama Mekanik", style="white")
        table.add_column("Spesialisasi", style="green")

        for idx, m in enumerate(mekanik_list, start=1):
            table.add_row(str(idx), m['nama'], m['spesialisasi'])

        console.print(table)

    # --- Tampilkan daftar pelanggan dari database ---
    def tampilkan_daftar_pelanggan(self):
        query = "SELECT * FROM pelanggan"
        pelanggan_list = self.db.fetch_all(query)

        if not pelanggan_list:
            console.print("[bold yellow]⚠ Belum ada pelanggan terdaftar di database.[/bold yellow]")
            return

        table = Table(title="📋 Daftar Pelanggan", header_style="bold magenta")
        table.add_column("No", justify="center", style="bold cyan")
        table.add_column("Nama Pelanggan", style="white")
        table.add_column("Kendaraan", style="green")

        for idx, p in enumerate(pelanggan_list, start=1):
            table.add_row(str(idx), p['nama'], p['kendaraan'])

        console.print(table)

    # --- Proses servis ---
    def proses_servis(self, mekanik, pelanggan):
        hasil = mekanik.servis(pelanggan)
        View.tampilkan_servis(hasil)
