'''
Materi OOP => Polymorphism Pythonix
menggunakan Polymorphism tanpa harus mendefinisikan tipe atau interface formal, 
memanfaatkan duck typing dan fleksibilitas Python.

kuncinya >>>
ducktype ini tidak perlu mewarisi (inhiretence) kelas dari parentnya, selama
setiap class memiliki nama fungsi yang sama, maka bisa digabungkan dalam 1 fungsi pemanggilnya
'''
class Manusia :
    def __init__(self, gender):
        self.__gender = gender
        
    def gender(self):
        return f"Manusia dengan gender {self.__gender}"
    
class Wanita:
    def __init__(self, perilaku):
        self.perilaku = perilaku
        
    def gender(self):
        return f"Wanita dengan perilaku {self.perilaku}"


def cetak_gender(object):
    return f"{object.gender()}"
    
wanita = Wanita("Menyusui")

manusia_list = [wanita]

for i in manusia_list:
    print(cetak_gender(i))