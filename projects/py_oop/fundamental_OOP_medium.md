
# Python OOP Level Medium – Ringkas & Jelas

## 1. Encapsulation Lanjutan
- **Private**: `__attr` → hanya bisa diakses dalam class.
- **Protected**: `_attr` → sebaiknya hanya diakses internal/subclass.
- **Getter/Setter**: method untuk membaca/mengubah atribut private.
- Tujuan: menjaga atribut tetap aman dan kontrol akses.

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # private
        self._age = age      # protected

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

## 2. Overriding + super()
- Subclass bisa mengubah perilaku method parent.
- Gunakan `super()` untuk memanggil method parent.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # panggil method parent
        print("Dog barks")
```

## 3. Polymorphism Sederhana
- Objek berbeda bisa memanggil method dengan nama sama, hasil berbeda.

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

animals = [Cat(), Dog()]
for a in animals:
    a.speak()
```

## 4. Duck Typing / Pythonic Polymorphism
- Tidak perlu inheritance formal.
- Fokus pada **method yang dipanggil ada di objek**.

```python
class Duck:
    def speak(self):
        print("Quack")

class Person:
    def speak(self):
        print("Hello")

def make_sound(obj):
    obj.speak()

make_sound(Duck())
make_sound(Person())
```

## 5. Class Composition (Opsional tapi Berguna)
- Gabungkan class daripada multi-inheritance.

```python
class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is ready")
```

## 6. Praktik Pythonic
- Dynamic attributes dan comprehension untuk efisiensi.

```python
class Numbers:
    def __init__(self, nums):
        self.nums = nums

    def squares(self):
        return [x**2 for x in self.nums]
```