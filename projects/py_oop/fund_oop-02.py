'''
Materi OOP => Inhiretences
Penjelasan: Membuat subclass menurunkan properti dan method dari parent class, sehingga kode bisa digunakan ulang.
    - Penggunaan Overiding 
        Mengganti perilaku method parent di subclass sesuai kebutuhan spesifik.
    - Penggunaan Super()
        Memanggil method parent dari subclass, berguna untuk menggunakan logika parent tanpa menulis ulang.
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