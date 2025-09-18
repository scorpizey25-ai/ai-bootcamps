<div align="center">

# 🐍✨ Kurikulum 2 Minggu Pythonic untuk Machine Learning  
*(khusus untuk yang sudah menguasai OOP level medium)*  

🚀 Tujuan: Menjadikan gaya coding lebih **Pythonic, ringkas, elegan, dan siap dipakai di workflow ML**.

</div>

---

## 📅 Minggu 1 — Fondasi Pythonic
🎯 Fokus: memperkuat idiom dasar yang langsung berguna untuk data preprocessing & eksplorasi.

### 📌 Hari 1-2
- Built-in functions penting: `len`, `sum`, `max`, `min`, `sorted`, `enumerate`, `any`, `all`, `zip`
- Tuple unpacking → `(X_train, X_test, y_train, y_test)`
- F-strings → logging & print metric

### 📌 Hari 3-4
- List comprehension: transformasi & filtering data
- Dictionary comprehension → mapping label → kategori
- Set comprehension → unik data

### 📌 Hari 5-6
- Loop Pythonic (`for item in items` ketimbang `for i in range(len(items))`)
- `with` statement → open dataset/CSV/JSON lebih clean
- Pathlib untuk file dataset (`Path.glob`, `Path.iterdir`)

### 📌 Hari 7 (Project Mini)
- **Mini project**:  
  - Load dataset sederhana (CSV atau list of dicts)  
  - Bersihkan data pakai comprehension  
  - Mapping label dengan dict comprehension  
  - Print ringkasan data pakai f-string  

---

## 📅 Minggu 2 — Pythonic + OOP untuk ML
🎯 Fokus: menggabungkan idiom Pythonic dengan konsep OOP medium yang sudah kamu kuasai.

### 📌 Hari 8-9
- Packing & unpacking: `*args`, `**kwargs`
- Sorting dengan `key` + lambda → pilih model dengan skor terbaik
- Ternary expression → `status = "Pass" if acc > 0.8 else "Fail"`

### 📌 Hari 10-11
- Generators & yield → batch data loading hemat RAM
- Generator expressions `(x for x in data if ...)`
- Itertools (`chain`, `groupby`) untuk dataset besar

### 📌 Hari 12-13
- Integrasi Pythonic + OOP:  
  - Buat **CustomDataset class** (pakai OOP)  
  - Gunakan `zip`, `enumerate`, comprehension di dalam method class  
  - Implementasi `__getitem__` & `__len__` ala PyTorch  

### 📌 Hari 14 (Project Mini)
- **Mini project**:  
  - Buat custom `Dataset` class (OOP)  
  - Load data dengan generator (Pythonic)  
  - Lakukan transformasi data (comprehension, zip)  
  - Evaluasi sederhana dengan logging f-string  

---

## 🎓 Hasil Akhir
- Bisa menulis kode ML preprocessing & pipeline dengan **gaya Pythonic**.  
- OOP medium-mu jadi lebih kuat karena dipadu dengan Pythonic idiom.  
- Siap lanjut ke **NumPy, Pandas, Scikit-learn, lalu PyTorch/TensorFlow** dengan clean code.

---

✨ Dibuat untuk mempersiapkan kamu menjadi **ML Engineer yang Pythonic & profesional**.
