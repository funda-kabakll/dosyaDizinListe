import os
class KlasorOku:
    @staticmethod
    def oku_hadi():
        klasor_adi = input("Klasörün yolunu giriniz: ").encode('utf-8')
        nedir_bu = os.listdir(klasor_adi.decode('utf-8'))

        for dosyalar in nedir_bu:
            print(dosyalar)
