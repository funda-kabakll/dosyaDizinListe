import os
class KlasorOku:
    def okuHadi(self):
        klasorAdı = input("Klasörün yolunu giriniz: ")
        nedirbu = os.listdir(klasorAdı)
        for dosyalar in nedirbu:
            print(dosyalar)
