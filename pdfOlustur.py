from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from baslikOku import BaslikOku  # 'baslikOku' modülünden BaslikOku sınıfını içe aktar

def pdfOlustur():
    # PDF dosyasının adını ve yolu belirleyin
    hedef_pdf_adi = "yeni_pdf.pdf"

    # PDF dosyasını oluşturun
    doc = SimpleDocTemplate(hedef_pdf_adi, pagesize=letter)

    # PDF dosyasına eklenecek verileri al
    veri_listesi = BaslikOku.pdf_oku('klasor')

    # PDF dosyasına verileri eklemek için biçimlendirme yapın
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.alignment = TA_CENTER
    veri_para = [Paragraph(paragraf, style) for paragraf in veri_listesi]

    # PDF dosyasına verileri ekleyin
    contents = []
    contents.extend(veri_para)
    contents.append(Spacer(1, 12))  # Boşluk ekleyebilirsiniz.

    # PDF dosyasını oluşturun
    doc.build(contents)

    print(f"{hedef_pdf_adi} adlı PDF dosyası oluşturuldu.")
