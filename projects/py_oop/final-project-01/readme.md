# Step by Step Penjelasan Project

## Student Class (`student.py`)
- `Person` punya **private `__name`** dan **protected `_age`** → Encapsulation
- `Student` **override `info()`** → Overriding + Polymorphism
- `grades` adalah **dynamic attribute** → Pythonic

## Analyzer Class (`analyzer.py`)
- Accepts any object dengan method `.average()` & `.get_age()` → Duck Typing
- Menghitung **overall average**, **age statistics**
- Menampilkan **text-based histogram** → Pythonic Visualization
- Analyzer menggunakan **composition** (list of Student)

## Main Script (`main.py`)
- Buat beberapa `Student` → test Polymorphism dan Overriding
- Pass ke `Analyzer` → test Duck Typing dan Composition
- Cetak info, statistik, dan histogram

## README.md
- Menjelaskan project, cara pakai, struktur folder, dan langkah-langkah OOP yang dipraktikkan