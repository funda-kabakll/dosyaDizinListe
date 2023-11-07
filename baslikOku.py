import os
from pdfminer.high_level import extract_text

class BaslikOku:
    @staticmethod
    def pdf_oku(klasor_yolu):
        pdf_dosyalar = [dosya for dosya in os.listdir(klasor_yolu) if dosya.endswith('.pdf')]

        basliklar = []  # PDF başlıklarını saklayacak bir liste

        for pdf_dosya in pdf_dosyalar:
            pdf_yol = os.path.join(klasor_yolu, pdf_dosya)

            metin = extract_text(pdf_yol, page_numbers=[0])  # İlk sayfa metnini al

            # İlk sayfa başlıkları None değeri olarak atanır
            satirlar = metin.split('\n')
            ilk_sayfa_baslik = None

            for satir in satirlar:
                # İstenmeyen karakterleri veya soyisimleri filtrele
                if "-" in satir or "(" in satir or "/" in satir or "Tonta" in satir or "Şencan" in satir:
                    continue
                if satir.strip():
                    ilk_sayfa_baslik = satir
                    break

            if ilk_sayfa_baslik:
                basliklar.append(f"PDF Başlığı ({pdf_dosya}):\n{ilk_sayfa_baslik}\n")
            else:
                basliklar.append(f"{pdf_dosya} Başlık bulunamadı\n\n")

        return basliklar
