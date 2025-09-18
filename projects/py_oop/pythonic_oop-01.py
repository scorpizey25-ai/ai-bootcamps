
nilai_siswa = [80, 55, 90, 70, 60]

'''
# Pythonic: built-in
nilai_max, nilai_min, nilai_avg = (
    max(nilai_siswa), 
    min(nilai_siswa),  
    sum(nilai_siswa) / len(nilai_siswa)  
)
print(f"Nilai Tertinggi : {nilai_max} \nNilai Terendah : {nilai_min} \nNilai Rata-Rata : {nilai_avg}")
'''

'''
# Pythonic: list comprehension
data_lulus = [nilai for nilai in nilai_siswa if(nilai>=70)]
rerata_lulus = sum(data_lulus) / len(data_lulus) if data_lulus else 0
print(f"Nilai Kelulusan : {data_lulus} \ndengan rata-rata : {rerata_lulus}")
'''

'''
# Pythonic: tupple unpacking
siswa = [("Andi", 15, 160), ("Budi", 16, 170), ("Citra", 15, 165)]

for nama_list, umur_list, tinggi_list in siswa:
    print(f"Nama Siswa : {nama_list}")
    
rerata = sum(tinggi for _, _,tinggi in siswa) / len(siswa)
print(f"Tinggi Rerata : { rerata }")
'''

# Pythonic: Dictionary & Zip
