'''
Materi OOP => Inhiretences
    - Penggunaan Overiding 
    - Penggunaan Super()
'''

class Kendaraan :
    def __init__(self, nama):
        self.nama = nama
        
    def jenis(self):
        return f"Ini adalah : {self.nama}"  
    
class Mobil(Kendaraan):
    def jenis(self):
        return f"Ini adalah : {self.nama}"  # tanpa super, label "ini adalah..." harus di tulis lagi
    
class Motor(Kendaraan):
    def jenis(self):
        return f"Ini adalah : {self.nama}"  # tanpa super, label "ini adalah..." harus di tulis lagi
 
class Skuter(Kendaraan):
    def jenis(self):
        # dengan super, label "ini adalah..." tetap ditulis di parent, tidak perlu ditulis ulang di turunan.
        # ditimpah oleh kelas turunan
        return f"{super().jenis()} model matic" 
    
ken = Kendaraan("Kendaraan Umum")
mob = Mobil("Mobil")
mot = Motor("Motor")
sku = Skuter("Skuter")

print(ken.jenis())
print(mob.jenis())
print(mot.jenis())
print(sku.jenis())