from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from baslikOku import BaslikOku  # 'baslikOku' modülünden BaslikOku sınıfını içe aktar

def pdf_olustur():
    hedef_pdf_adi = "yeni_pdf.pdf"

    # PDF dosyası oluşturur, standart sayfa boyutu ile
    doc = SimpleDocTemplate(hedef_pdf_adi, pagesize=letter)

    # PDF dosyasına eklenecek verileri al
    veri_listesi = BaslikOku.pdf_oku('klasor')

    # PDF dosyasına verileri eklemek için biçimlendirme yapın, ta center metni ortalar
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.alignment = TA_CENTER
    veri = [Paragraph(paragraf, style) for paragraf in veri_listesi]

    # PDF dosyasına verileri ekler
    contents = []
    contents.extend(veri)
    contents.append(Spacer(1, 12))  # Boşluk ekleyebilirsiniz.

    # PDF dosyasını oluşturur
    doc.build(contents)

    print(f"{hedef_pdf_adi} adlı PDF dosyası oluşturuldu.")
