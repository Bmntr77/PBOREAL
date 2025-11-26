# views/view.py
class View:
    @staticmethod
    def tampilkan_daftar(bengkel, mekanik_list, pelanggan_list):
        print(f"\n=== {bengkel} ===")
        print("\n-- Daftar Mekanik --")
        for m in mekanik_list:
            print(m)
        print("\n-- Daftar Pelanggan --")
        for p in pelanggan_list:
            print(p)
    
    @staticmethod
    def tampilkan_servis(proses_servis):
        print("\nProses Servis")
        print(proses_servis)
