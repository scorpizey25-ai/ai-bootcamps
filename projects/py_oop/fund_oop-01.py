'''
Materi OOP => Class
    Penggunaan Class, Attribut, dan akses object class
    Penggunaan __str__ dan __repr__
'''
class Buku:
    penerbit = "gramedia"
    
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        
    def get_info(self):
        return f"{self.judul} | {self.penulis} | {self.penerbit} | {self.tahun_terbit}"
        
    # gunakan untuk lingkungan users
    def __str__(self):
        return f"{self.judul} | {self.penulis} | {self.penerbit} | {self.tahun_terbit}"
    
    # gunakan untuk lingkungan developer guna debugging / console 
    def __repr__(self):
        return f"Buku('{self.judul}', '{self.penulis}', '{self.penerbit}',  '{self.tahun_terbit}')"
    
buku = Buku("belajar python oop", "novan surya ardani", 2025)
print(f"*** Menggunakan metode get_info => {buku.get_info()}")
print(f"*** Menggunakan metode __str__  => {str(buku)}")
print(f"*** Menggunakan metode __repr__ => {repr(buku)}")
