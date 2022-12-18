import os
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader as read
from PyPDF2 import PdfFileWriter as write
import pdfkit


class Pdf_Tools:

    @staticmethod
    def rotate_page(path, page, side="clockwise", angle=90):
        """takes the file and the wanted page as argument. modifies the file itself"""
        pdf_writer = write()
        pdf_reader = read(path)

        if side == "clockwise":
            # Rotate page 90 degrees to the right
            page = pdf_reader.getPage(page).rotateClockwise(angle)
            pdf_writer.addPage(page)
            # Rotate page 90 degrees to the left
        elif side == "counterclockwise":
            page = pdf_reader.getPage(page).rotateCounterClockwise(angle)
            pdf_writer.addPage(page)

        with open('rotate_pages.pdf', 'wb') as fh:
            pdf_writer.write(fh)

    @staticmethod
    def rotate_all(path, side="clockwise", angle=90):
        """takes a file as argument and modifies all its pages to be rotated"""
        pdf_reader = read(path)
        for page in range(pdf_reader.getNumPages()):
            Pdf_Tools.rotate_page(path, page, side, angle)

    @staticmethod
    def merge_pdfs(paths, output):
        """takes a list of path of all the pages that want to be merget in order and modifies them as one document"""
        pdf_writer = write()

        for path in paths:
            pdf_reader = read(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    @staticmethod
    def split(path, name_of_file="new file"):

        pdf = read(path)
        for page in range(pdf.getNumPages()):
            pdf_writer = write()
            pdf_writer.addPage(pdf.getPage(page))

            output = f'{name_of_file}{page}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

    # no ready
    @staticmethod
    def create_watermark(self, input_pdf, output, watermark):
        watermark_obj = read(watermark)
        watermark_page = watermark_obj.getPage(0)

        pdf_reader = read(input_pdf)
        pdf_writer = write()

        # Watermark all the pages
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        with open(output, 'wb') as out:
            pdf_writer.write(out)

    # no ready
    @staticmethod
    def add_encryption(self, input_pdf, output_pdf, password):  # not working
        pdf_writer = write()
        pdf_reader = read(input_pdf)

        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        pdf_writer.encrypt(user_pwd=password, owner_pwd="",
                           use_128bit=True)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)


class Pdf_creator:
    """TODO: everything"""

    # TASK: create a function to turn pdf page in .png/ or other images tipes
    def __init__(self, filename):  # def create_file(title="NewPDF", subtitle="", content=[], image=None):

        self.ext = filename.split(".")[-1]

        if "C:" in filename:
            self.filepath = filename

            if self.ext == "pdf":
                with open(self.filepath, 'rb') as f:
                    pdf = read(f)
                    self.information = pdf.getDocumentInfo()
                    self.number_of_pages = pdf.getNumPages()

                    self.author = self.information.author
                    self.creator = self.information.creator
                    self.producer = self.information.producer
                    self.subject = self.information.subject
                    self.title = self.information.title

            elif self.ext == "txt":

                with open(filename, "r") as f:
                    self.content = f.readlines()

            else:
                print("WTF you did, nigga?")
        else:
            self.filepath = os.path.join("C:\Users\Default\Documents", f"{filename}.pdf")

            self.title = filename
            self.pdf = canvas.Canvas(f'{self.title}.pdf')
            self.pdf.setTitle(self.title)
            self.available_colors = [color for color in self.pdf.setFillColor(colors)]

            with open(self.filepath, 'rb') as f:
                pdf = read(f)
            self.number_of_pages = pdf.getNumPages()

            self.available_fonts = ["Courier", "Courier-Bold", "Courier-BoldOblique", "Courier-Oblique", "Helvetica",
                                    "Helvetica-Bold", "Helvetica-BoldOblique", "Helvetica-Oblique", "Symbol",
                                    "Times-Bold", "Times-BoldItalic", "Times-Italic", "Times-Roman", "ZapfDingbats"]

        self.save_pdf()

    def write_title(self):
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Times-Bold', 36)
        self.pdf.drawCentredString(300, 770, self.title)

        self.save_pdf()

    def write_subtitle(self, subtitle):
        self.pdf.setFillColor(colors.black)
        self.pdf.setFont('Times-Bold', 20)
        self.pdf.drawCentredString(300, 720, subtitle)

        self.save_pdf()

    def write_text_block(self):
        # IMPORTANT:
        # cut the text in apropied chunks and put in a list of lines

        texto = self.create_text_list()

        texto = self.pdf.beginText(40, 680)
        self.pdf.setFont('Times-Bold', 14)
        self.pdf.setFillColor(colors.black)

        for line in self.content:
            texto.textLine(line)
            # print(line)
        self.pdf.drawText(texto)

        self.save_pdf()

    # def add_page(self):
    #     pdf_writer = write()
    #     pdf_writer.addPage(self.page)

    def create_text_list(self, content):
        pass

    def save_pdf(self):
        self.pdf.save()

    def extract_information(self):
        return self.author, self.creator, self.producer, self.subject, self.title

    def create_file(self, title="New file", subtitle=None, text=None):
        pdf = canvas.Canvas(f'{title}.pdf')
        pdf.setTitle(title)
        pdf.setFont('Courier', 36)
        pdf.drawCentredString(300, 770, title)

        if subtitle:
            pdf.setFillColorRGB(0, 0, 255)
            pdf.setFont('Courier-Bold', 20)
            pdf.drawCentredString(290, 720, subtitle)

        if text:
            # cut the text in apropied chunks and put in list
            if list(text):
                content_text = pdf.beginText(40, 680)
                text.setFont('Courier', 14)
                text.setFillColor(colors.red)

            for line in text:
                text.textLine(line)
                print(line)

            pdf.drawText(text)
        pdf.save()

    def text_from_string(self, filename, content):
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }
        pdfkit.from_string(content, filename, options=options)

    # def add_page(self, filename, page):
    #     pdf_writer = write()
    #     pdf_reader = read(filename)
    #
    #     # Add a page in normal orientation
    #     pdf_writer.addPage(pdf_reader.getPage(page))


if __name__ == '__main__':
    pass
