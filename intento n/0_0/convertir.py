from wand.image import Image as wi

class pdf2jpg:
    def __init__(self):
        self.convertir
    def convertir(self):

        pdf = wi(filename="example.pdf", resolution=300)
        pdfimage = pdf.convert("jpeg")
        i=1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename=str(i)+".jpg")
            i +=1