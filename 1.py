class Foydalanuvchi:
    def __init__(self, ism, username, parol):
        self.ism = ism
        self.username = username
        self.__parol = parol  

    def parolni_ozgartir(self, eski_parol, yangi_parol):
        if self.__parol == eski_parol:
            self.__parol = yangi_parol
            print("Parol muvaffaqiyatli o'zgartirildi")
        else:
            print("Eski parol noto'g'ri kiritildi!")

    def tekshir(self, parol):
        if self.__parol == parol:
            print("Parol to'g'ri")
            return True
        else:
            print("Parol noto'g'ri!")
            return False


user1 = Foydalanuvchi("Dilnuraxon", "@dilnura0520", "dilnuraxon2010")
user1.tekshir("dilnuraxon2010")
user1.parolni_ozgartir("dilnuraxon2010", "td0520")

user2 = Foydalanuvchi("Madina", "madina_99", "secret789")
user2.tekshir("wrong_password")
user2.parolni_ozgartir("secret789", "newpass123")
