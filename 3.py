class Avtomobil:
    def __init__(self, model):
        self.model = model
        self.__eshik_ochiq = False 

    def eshikni_och(self):
        if self.__eshik_ochiq==False:
            self.__eshik_ochiq = True
            print(f"'{self.model}' eshigi ochildi.")
        else:
            print(f"Kechirasiz, '{self.model}' eshigi allaqachon ochiq edi!")

    def eshikni_yop(self):
        if self.__eshik_ochiq == True:
            self.__eshik_ochiq = False
            print(f"'{self.model}' eshigi yopildi")
        else:
            print(f"Eshik allaqachon yopiq edi")

    def holat(self):
        if self.__eshik_ochiq==True:
            print(f"'{self.model}' hozirgi holati: eshiklari  ochiq")
        else:
            print(f"'{self.model}' hozirgi holati: eshiklari yopiq")


mashina = Avtomobil("Chevrolet Cobalt")
mashina.eshikni_och()
mashina.holat()
mashina.eshikni_yop()
