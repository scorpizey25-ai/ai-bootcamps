'''
Materi OOP => Encapsulation
Encapsulation = menyembunyikan detail internal objek agar tidak bisa diubah sembarangan dari luar.
    - self.x	→ Public      → bisa diakses/ubah langsung dari luar
    - self._x	→ Protected   → seharusnya hanya diakses internal/subclass
    - self.__x	→ Private     → hanya bisa diakses di dalam kelas
    
Penggunaan => Encapsulation + Overriding + super()
'''

class Kendaraan:
    def __init__(self, nama, kecepatan):
        self.__nama = nama              # __nama private
        self.__kecepatan = kecepatan    # __kecepatan private
        
    def getNama(self):
        return self.__nama
    
    def getKecepatan(self):
        return self.__kecepatan
    
    def jenis(self):
        return f"{self.getNama()} bergerak dengan kecepatan {self.getKecepatan()} km/jam"
        
class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan, tipe):
        super().__init__(nama, kecepatan)   # memanggil parent constructor
        self.__tipe = tipe  # atribut tambahan turunan
            
    def jenis(self):
        return f"{super().jenis()} dan tipe mobil : {self.__tipe}"
    
class Motor(Kendaraan):
    def __init__(self, nama, kecepatan, mesin):
        super().__init__(nama, kecepatan)
        self.__mesin = mesin
        
    def jenis(self):
        return f"{super().jenis()} dan mesin : {self.__mesin}"
        
mobil = Mobil("Avanza", 120, "SUV");
print(mobil.jenis())

motor = Motor("Ninja", 100, "250cc");
print(motor.jenis())