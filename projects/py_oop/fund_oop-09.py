'''
    OOP -> Composition I
    Composition adalah teknik OOP di mana satu class memiliki objek class lain sebagai atribut, 
    sehingga atribut dan method class tersebut dapat digunakan melalui objek tersebut, 
    tanpa melakukan inheritance.
    
    Singkatnya :
        “Composition adalah cara class menggunakan objek class lain untuk mengakses 
        atribut dan methodnya tanpa mewarisinya.”
'''
class Mesin :
    def start(self):
        print("Hidupkan Mesin....")
    
    def stop(self):
        print("Matikkan Mesin....");
        
class Motor :
    def __init__(self):
        self.mesin = Mesin()    # Compositions
        
    def drive(self):
        self.mesin.start()  # gunakan fitur engine start pada class Mesin
        print("Mengemudi Motor...")
        
    def parking(self):
        self.mesin.stop()  # gunakan fitur engine stop pada class Mesin
        print("Parkir Motor...")
        
motor = Motor()
motor.drive()
motor.parking()