import time
from klasorOku import klasor_oku
from baslikOku import BaslikOku
from pdfOlustur import pdf_olustur

print("~ Pdf Okuma Programına Hoş Geldiniz ~")
print(" |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("")
time.sleep(2)

while True:
    print("Menü: 0)Çıkış \n 1)Pdf adlarını listele \n 2)Pdf başlıklarını oku \n 3)Başlıklardan yeni pdf oluştur \n ")
    menuSecim = int(input("Tercihiniz: "))
    if menuSecim == 0:
        print("Program kapatılıyor...")
        time.sleep(1)
        break
    elif menuSecim == 1:
        klasor_oku()
    elif menuSecim == 2:
        klasor_yolu = 'klasor'
        basliklar = BaslikOku.pdf_oku(klasor_yolu)
        for baslik in basliklar:
            print(baslik)
    elif menuSecim == 3:
        pdf_olustur()
