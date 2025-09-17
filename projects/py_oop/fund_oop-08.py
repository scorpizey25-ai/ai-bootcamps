
'''
Materi OOP => Class Attributes & Class Methods / Static Methods

Fondasi dasar (self, class-method, static-method)
Perbedaan :
    --------------------------------------------------------------------------------------
    Jenis            Decorator          akses attribut      akses method
    --------------------------------------------------------------------------------------
    self             default / self     construct           harus buat object
                                                            (instance)
    class-method     @classmethod       class               langsung panggil class name 
                                                            atau lewat object   
    static-method    @staticmethod      tidak tergantung    langsung panggil class name
                                                            atau lewat object
Kesimpulan :
    1. self         → butuh object.
    2. cls          → butuh class.
    3. staticmethod → tidak butuh keduanya.
'''

class Mobil:
    jenis_bbm1 = "pertamax"     # class attribute milik class dan semua object
    
    # self diisi otomatis dengan object yang memanggil.
    # mob = Mobil("Sedan", "Pertalite")
    def __init__(self, nama, jenis_bbm2):        
        self.nama = nama                
        self.jenis_bbm2 = jenis_bbm2
        
    def spek_mobil(self):   # self butuh object untuk bisa mengakses
        return f"Mobil {self.nama} menggunakan bbm jenis {self.jenis_bbm2}"
    
    @classmethod        #decoration class method
    def upgrade_spek(cls):        
        print (f"Upgrade bbm menjadi {cls.jenis_bbm1}")
    
    @staticmethod
    def Roda(rodaDepan, rodaBelakang):
        return rodaDepan + rodaBelakang
        
mob = Mobil("Sedan", "Pertalite")
# panggil menggunakan self
print(mob.spek_mobil())

# panggil menggunakan class method
Mobil.upgrade_spek()

# panggil menggunakan static method
print(f"Jumlah Roda {Mobil.Roda(2,2)}")