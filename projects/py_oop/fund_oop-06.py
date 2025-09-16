'''
Materi OOP => Decorator
Sebelum masuk ke OOP attribut & decorator, kita selami lebih dalam mengenai
decorator tanpa OOP dulu

 A. Penjelasan :
    Decorator adalah fungsi yang membungkus fungsi lain, untuk menambahkan fitur tanpa mengubah fungsi asli.
    Sintaks Pythonic: @decorator_name di atas fungsi yang ingin dibungkus.

 B. Tujuan :
    cara menambahkan fitur ekstra (misalnya logging, keamanan, caching, validasi) tanpa harus 
    menyentuh isi fungsi asli → cukup bungkus aja.
    ............ start logging ............     mulai bungkus (wrapper)
        .... tambahkan fungsi lain ....         fungsi apa yang mau dibungkus ?
    ............ end logging .............      tutup bungkus (return wrapper)
    
 C. Hierarki/Struktur wajib decorator (sederhana):
    ============ penulisan sederhana ============
    def nama_decorator(attr_func):   # nama_decorator (wajib) + attribut function (sunnah)
        def nama_wrapper()           # nama_wrapper (wajib) + attribut function (sunnah)
            attr_func()              # mengambil attribut function decoration sebagai function (wajib)
        return nama_wrapper          # mengembalikan nama_wrapper (wajib)
        
    # bungkus fungsi lain (kendaraan) dalam decorator    
    @nama_decorator                  # panggil nama fungsi decoratornya (tambahkan @ itu wajib)
    def kendaraan():
        print("Mobil sedang berjalan 🚙")
        
    # Panggil fungsi
    kendaraan()

'''

def decorator(fdecorator):
    def wrapper():
        print("persiapan berkendara...")
        fdecorator()
        print("berkendara selesai...")
    return wrapper

@decorator
def mobil():
    print("Kendaraan Mobil")

@decorator
def motor():
    print("Kendaraan Motor")
    
#mobil()
#print("\n")
#motor()

'''
 D. Hierarki/Struktur wajib decorator (advance):
'''
def kendaraan_decorator(fdecorator):
    def kendaraan_wrapper(jenis):
        print("mulai berkendara...")
        fdecorator(jenis)
        print("selesai berkendara...")
    return kendaraan_wrapper

@kendaraan_decorator
def other_mobil(jenis):
    print(f"mobil {jenis}")
    
other_mobil("Sedan SUV")