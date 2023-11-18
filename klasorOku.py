import os
def klasor_oku():
        klasor_adi = input("Klasörün yolunu giriniz: ").encode('utf-8')
        nedir_bu = [dosya for dosya in os.listdir(klasor_adi.decode('utf-8')) if dosya.endswith('.pdf')]

        for dosyalar in nedir_bu:
            print(dosyalar)
