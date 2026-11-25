class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif
        self.__ijarada = False 

    def ijaraga_ber(self):
        if self.__ijarada==False:
            self.__ijarada = True
            print(f"'{self.nomi}' kitobi ijaraga berildi.")
        else:
            print(f"Kechirasiz, '{self.nomi}' kitobi allaqachon ijarada!")

    def qaytarish(self):
        if self.__ijarada==True:
            self.__ijarada = False
            print(f"'{self.nomi}' kitobi kutubxonaga qaytarildi.")
        else:
            print(f"Bu kitob allaqachon kutubxonada edi.")

    def holat(self):
        if self.__ijarada==True:
            print(f"'{self.nomi}' kitobi hozirgi holati: Ijarada")
        else:
            print(f"'{self.nomi}' kitobi hozirgi holati: Kutubxonada mavjud")

kitob = Kitob("O‘tkan kunlar", "Abdulla Qodiriy")
kitob.ijaraga_ber()
kitob.holat()
kitob.qaytarish()
kitob.holat()
