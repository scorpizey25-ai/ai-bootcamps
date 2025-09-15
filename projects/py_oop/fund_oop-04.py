'''
Materi OOP => Polymorphism
Dalam OOP, ini memungkinkan satu interface/metode memiliki banyak implementasi tergantung objek yang memanggilnya.

Ada dua tipe utama:
    1. Polymorphism pada method (Method Overriding / Overloading)
    2. Polymorphism pada objek (Interface/Abstract class)
'''
class Kendaraan :
    def __init__(self, nama, kecepatan):
        self.__nama = nama
        self.__kecepatan = kecepatan
        
    def getNama(self):       
        return self.__nama
    
    def getKecepatan(self):
        return self.__kecepatan
    
    def suara(self):
        return f"suara kendaraan {self.getNama()} dengan kecepatan {self.getKecepatan()} km/jam"
    
class Mobil(Kendaraan) :
    def __init__(self, nama, kecepatan, merk):
        super().__init__(nama, kecepatan)
        self.merk = merk
    
    def suara(self):
        return f"{super().suara()} berbunyi woooozzz..." 

class Motor(Kendaraan) :
    def __init__(self, nama, kecepatan, merk):
        super().__init__(nama, kecepatan)
        self.merk = merk
    
    def suara(self):
        return f"{super().suara()} berbunyi broooommm..." 
        
mobil = Mobil("Avanza", "150", "veloz")
motor = Motor("Ducati", "250", "sport")

print("\n========== Menggunakan Enkasulapsi ==========\n");
print(mobil.suara())
print(motor.suara())

print("\n========== Menggunakan Polymorphism ==========\n");
kendaraan_list = [mobil, motor]
for k in kendaraan_list:
    print(k.suara())