'''
Pythonic : Built-in Functions
    
A.  Definisi ringkas & tujuan
    Alat dasar Python untuk bekerja dengan data, yang membuat kode kita lebih ringkas, cepat, dan Pythonic.
        1. len(obj) → panjang/ukuran koleksi.
        2. sum(iterable) → jumlah elemen numerik.
        3. max/min(iterable, key=...) → nilai terbesar/terkecil (dengan opsi key).
        4. sorted(iterable, reverse=False, key=...) → mengembalikan list terurut (tidak merubah input).
        5. enumerate(iterable, start=0) → iterator (index, value).
        6. zip(*iterables) → iterator pasangan tuple dari input (stop di terpendek).
        7. any(iterable) → True jika ada minimal 1 True (short-circuit).
        8. all(iterable) → True jika semua True (short-circuit).
'''
# Data siswa (nama + nilai ujian)
siswa = {
    "Ani" : [80, 90, 75],
    "Budi": [60, 70, 65],
    "Cici": [85, 88, 92],
    "Deni": [70, 75, 80]
}

print("\n====== Hitung Rata2 Nilai Setiap Siswa ======")

# soal : Hitung rata-rata tiap siswa
# combinasi pythonic = Looping dictionary(iterations) + built-in functions + f-string formatting.
for nama, nilai in siswa.items():       # (nama, nilai) => gunakan items() untuk mengambil key & values
    nilai_rerata = sum(nilai) / (len(nilai))          
    print(f"Nama {nama} dengan nilai rata-rata {nilai_rerata:.2f}")
    
print("\n====== Urutkan Nama Siswa Berdasarkan Nilai Rata2 Tertinggi ======")

# urutkan dulu nilainya, dengan
# mengubah menjadi list/tupple dulu sebelum di sort
# gunakan key=lambda bahwa x[1] mengambil element list/tuple ke-2 yaitu nilai, 
# memastikan sorting pakai nilai rata-rata, bukan nama.
# gunakan enumerate untuk memberikan urut nomor
# variabel i menyimpan index ke-n dimulai dari 1 (start=1)
list_rerata  = [(nama, sum(nilai_1) / len(nilai_1)) for nama, nilai_1 in siswa.items()]    
nilai_sorted = sorted(list_rerata, key=lambda x: x[1], reverse=True)  

for i, (nama, nilai) in enumerate(nilai_sorted, start=1):  
    print(f"Urutan ke-{i} Nama {nama} nilai rata-rata {nilai:.2f}")
    
print("\n====== Menentukan Nilai Terbaik ======")
# combinasi pythonic = Looping dictionary(iterations) + built-in functions + f-string formatting. + unpacking
# unpacking membongkar list => nama, rata2 = ("Cici", 88.33) menjadi nama = "Cici" dan nilai = 88,33
nilai_terbaik = max(list_rerata, key=lambda x:x[1])
nama, rata2 = nilai_terbaik     # mengunakan pythonic unpackage 
print(f"Nilai Terbaik : {rata2:.2f}")

print("\n====== Menentukan yang lulus (rata-rata ≥ 75) ======")
nilai_sorted = sorted(list_rerata, key=lambda x: x[1], reverse=True)  
for nama, nilai in nilai_sorted:
    kriteria = "Lulus" if nilai >= 75 else "Tidak Lulus"
    print(f"Nama {nama} dengan nilai rata-rata {nilai:.2f} dinyatakan {kriteria}")