class Orang:
    def __init__(self, nama):
        self._nama = nama  # atribut private(encapsulation)
    
    def info(self):
        return f"Nama: {self._nama}"


# Kelas Turunan dari class Orang
class Pelanggan(Orang):
    def __init__(self, nama, kendaraan):
        super().__init__(nama)
        self.__kendaraan = kendaraan  
    
    def info(self):  # polymorphism method info di tulis ulang di kelas turunan
        return f"Pelanggan: {self._nama}, Kendaraan: {self.__kendaraan}"

    def get_kendaraan(self):
        return self.__kendaraan


# Kelas Turunan dari class orang Mekanik 
class Mekanik(Orang):
    def __init__(self, nama, spesialisasi):
        super().__init__(nama)
        self.__spesialisasi = spesialisasi
    
    def info(self):  # polymorphism
        return f"Mekanik: {self._nama}, Spesialisasi: {self.__spesialisasi}"

    def servis(self, pelanggan):
        print(f"{self._nama} sedang memperbaiki {pelanggan.get_kendaraan()} milik {pelanggan._nama}")


class Bengkel:
    def __init__(self, nama_bengkel):
        self.__nama_bengkel = nama_bengkel
        self.__pelanggan = []
        self.__mekanik = []
    
    def tambah_pelanggan(self, pelanggan):
        self.__pelanggan.append(pelanggan)
    
    def tambah_mekanik(self, mekanik):
        self.__mekanik.append(mekanik)
    
    def daftar(self):
        print(f"\n=== {self.__nama_bengkel} ===")
        print("\n-- Daftar Mekanik --")
        for m in self.__mekanik:
            print(m.info())
        print("\n-- Daftar Pelanggan --")
        for p in self.__pelanggan:
            print(p.info())


if __name__ == "__main__":
    bengkel = Bengkel("B_Mekanik")

    mekanik1 = Mekanik("Dek adi", "Mesin")
    mekanik2 = Mekanik("Sugeng", "Kelistrikan")
    pelanggan1 = Pelanggan("Sumer", "Aerox")
    pelanggan2 = Pelanggan("Panji", "Blar Blar")

    bengkel.tambah_mekanik(mekanik1)
    bengkel.tambah_mekanik(mekanik2)
    bengkel.tambah_pelanggan(pelanggan1)
    bengkel.tambah_pelanggan(pelanggan2)

    bengkel.daftar()

    print("\nProses Servis")
    mekanik1.servis(pelanggan1)
