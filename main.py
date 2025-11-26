# main.py
from controllers.controller import BengkelController
from models.model import Bengkel, Mekanik, Pelanggan
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def tampilkan_menu():
    console.print(Panel.fit("[bold magenta]SISTEM MANAJEMEN BENGKEL B_MEKANIK[/bold magenta]",
                            border_style="bright_blue"))

    table = Table(title="📋 Menu Utama", header_style="bold magenta")
    table.add_column("No", justify="center", style="bold cyan")
    table.add_column("Menu", style="white")

    table.add_row("1", "Tambah Mekanik Baru")
    table.add_row("2", "Tambah Pelanggan Baru")
    table.add_row("3", "Tampilkan Daftar Mekanik")
    table.add_row("4", "Tampilkan Daftar Pelanggan")
    table.add_row("5", "Proses Servis (Demo)")
    table.add_row("6", "Keluar")

    console.print(table)

    pilihan = console.input("[bold green]Pilih menu (1-6): [/bold green]")
    return pilihan

if __name__ == "__main__":
    # Inisialisasi Model dan Controller
    bengkel = Bengkel("B_Mekanik")
    controller = BengkelController(bengkel)

    # Inisialisasi data demo
    # mekanik_demo = Mekanik("Dek adi", "Mesin")
    # pelanggan_demo = Pelanggan("Sumer", "Aerox")
    controller.tambah_mekanik(mekanik_demo)
    controller.tambah_pelanggan(pelanggan_demo)

    while True:
        pilihan = tampilkan_menu()

        if pilihan == '1':
            controller.tambah_mekanik_dari_input()

        elif pilihan == '2':
            controller.tambah_pelanggan_dari_input()

        elif pilihan == '3':
            controller.tampilkan_daftar_mekanik()

        elif pilihan == '4':
            controller.tampilkan_daftar_pelanggan()

        elif pilihan == '5':
            print("\nProses Servis Demo (Mekanik 'Dek adi' servis 'Aerox' milik 'Sumer')...")
            controller.proses_servis(mekanik_demo, pelanggan_demo)

        elif pilihan == '6':
            print("\nTerima kasih, program berakhir.")
            break

        else:
            print("\n❌ Pilihan tidak valid. Silakan coba lagi.")
