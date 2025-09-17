'''
    Coverage => Encapsulation + Polymorphism + Overriding
        - Encapsulation : Modifier private & protected, dimana perlindungan atribut ini
                          agar tidak bisa diakses di luar class
          Karakteristik : setter dan getter / __attr : private dan _attr : protected
          
        - Mengubah perilaku method didalam class turunannya pada method parentnya
'''
# student.py
class Person:
    def __init__(self, name, age):
        self.__name = name  # private
        self._age = age     # protected

    def get_name(self):
        return self.__name

    def get_age(self):
        return self._age

    def info(self):
        return f"Name: {self.__name}, Age: {self._age}"


class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades  # Pythonic dynamic attribute

    def average(self):
        return sum(self.grades)/len(self.grades)

    def info(self):  # Overriding
        return f"{super().info()}, Grades: {self.grades}, Average: {self.average():.2f}" # floating, 2 digit belakang angka
    
         
person = Person("Johnson", 26)
# print(person.info())

student = Student("Maria", 30, [100, 200, 50, 150, 30])
print(student.info())