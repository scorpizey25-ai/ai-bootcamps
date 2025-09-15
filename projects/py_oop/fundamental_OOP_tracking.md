# 📘 Ringkasan Materi OOP Python – Checklist Belajar

## 🟢 Beginner (Dasar)
Materi ini cukup untuk memahami OOP **dasar**, membuat class, objek, dan pemanggilan method sederhana.

### ✅ Sudah Dipelajari
- [x] **Class & Object**  
  - **Penjelasan:** Blueprint untuk membuat objek. Class mendefinisikan atribut dan method, objek adalah instansiasi class.

- [x] **Constructor (`__init__`)**  
  - **Penjelasan:** Method khusus yang dijalankan saat objek dibuat, untuk menginisialisasi atribut.

- [x] **Inheritance (Pewarisan)**  
  - **Penjelasan:** Membuat subclass menurunkan properti dan method dari parent class, sehingga kode bisa digunakan ulang.

- [x] **Overriding**  
  - **Penjelasan:** Mengganti perilaku method parent di subclass sesuai kebutuhan spesifik.

- [x] **`super()`**  
  - **Penjelasan:** Memanggil method parent dari subclass, berguna untuk menggunakan logika parent tanpa menulis ulang.

- [x] **Encapsulation (Enkapsulasi)**  
  - **Penjelasan:** Menyembunyikan atribut internal agar tidak diubah sembarangan.
  - **Private:** `__attr` → hanya bisa diakses dalam class.
  - **Protected:** `_attr` → sebaiknya hanya diakses internal/subclass.
  - **Public:** `attr` → bebas diakses dari luar.
  - **Getter/Setter:** method untuk membaca atau mengubah atribut private secara aman.

---

## 🟡 Medium (Menengah)
Materi ini mengkombinasikan beberapa konsep OOP untuk membuat program **lebih fleksibel dan Pythonic**.

### ✅ Sudah Dipelajari
- [x] **Encapsulation + Overriding + super()**  
  - **Penjelasan:** Gabungan praktik nyata, subclass menggunakan getter parent dan memodifikasi method dengan `super()`.

- [x] **Polymorphism sederhana**  
  - **Penjelasan:** Objek berbeda dapat memanggil method yang sama tapi menghasilkan perilaku berbeda.

- [x] **Duck Typing (Pythonic Polymorphism)**  
  - **Penjelasan:** Python memanggil method yang sama pada objek berbeda tanpa peduli inheritance formal. Filosofi: "If it walks like a duck and it quacks like a duck, it must be a duck".

---

## 🔴 Advance (Lanjutan / Profesional)
Materi ini diperlukan untuk **proyek nyata, sistem besar, atau library/framework**.  

### ⬜ Belum Dipelajari / Masih Kurang
- [ ] **Property & Decorator (`@property`)**  
  - **Penjelasan:** Versi Pythonic dari getter/setter, memungkinkan atribut diakses seperti properti tanpa method eksplisit.

- [ ] **Class Attributes & Class Methods / Static Methods**  
  - **Penjelasan:** Atribut dan method yang terkait class, bukan objek. Berguna untuk shared data atau utilitas class.

- [ ] **Multiple Inheritance (Multi-parent)**  
  - **Penjelasan:** Class mewarisi lebih dari satu parent. Penting memahami Method Resolution Order (MRO) agar super() memanggil parent yang tepat.

- [ ] **Special Methods / Dunder Methods**  
  - **Penjelasan:** Method khusus Python seperti `__str__`, `__repr__`, `__add__` memungkinkan objek berperilaku seperti tipe built-in.

- [ ] **Abstract Class & Interface**  
  - **Penjelasan:** Kontrak method wajib untuk subclass menggunakan modul `abc`. Menjamin semua subclass memiliki method yang konsisten.

- [ ] **Polymorphism kompleks / Design Patterns**  
  - **Penjelasan:** Polymorphism yang dipadukan dengan abstract class, interface, atau pattern desain skala besar untuk membuat sistem fleksibel dan terstruktur.

---

## 💡 Catatan:
- Materi **Beginner + Medium** cukup untuk membuat **program OOP dasar sampai menengah**.  
- Materi **Advance** akan memperkuat **struktur proyek nyata, Pythonic coding, dan design pattern**.  
- Urutan belajar disarankan:  
  1. Property & Decorator  
  2. Class/Static Method  
  3. Abstract Class / Interface  
  4. Special Methods / Dunder Methods  
  5. Polymorphism kompleks / Design Patterns
