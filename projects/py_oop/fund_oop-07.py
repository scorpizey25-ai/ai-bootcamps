'''
Materi OOP => Decorator II

 A. Point Utama :
    Ini semua adalah decorator dalam OOP untuk enkapsulasi & kontrol penuh terhadap atribut.
        1. @property            = ubah method jadi atribut → memudahkan akses.
        2. @kecepatan.setter    = validasi atau logika sebelum ubah nilai.
        3. @kecepatan.deleter   = logika saat hapus atribut.

 B. Perbedaan :   
    1. Cara lama (tanpa property): harus panggil method dengan tanda ()
        mob.get_nama_old()
        mob.set_nama_old("Bus Kota")
        
    2. Cara baru (pakai @property): akses seperti variabel biasa
        mob.get_nama_new
        mob.get_nama_new = "Mobil Sedan"
'''
class Mobil :
    
    def __init__(self, nama):
        self.__nama = nama
    
    # cara lama tanpa menggunakan decorator properties
    def get_nama_old(self):     
        return self.__nama
    
    def set_nama_old(self, nilai):
        self.__nama = nilai
    
    # cara baru menggunakan decorator properties
    @property
    def get_nama_new(self):     
        return self.__nama
    
    @get_nama_new.setter
    def set_nama_new(self, nilai):
        self.__nama = nilai
        
mob = Mobil("Kendaraan Umum Jenis Mobil ")

# pemanggilan fungsi menggunakan ()
mob.set_nama_old("Jeep")
print(mob.get_nama_old())       

# pemanggilan fungsi tanpa () 
mob.set_nama_new = "Sedan"
print(mob.get_nama_new)         