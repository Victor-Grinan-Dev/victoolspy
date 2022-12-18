import PyPDF2 as p2
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os
from flask import Flask, render_template, make_response
import pdfkit
import math

fonts = ["Courier", "Courier-Bold", "Courier-BoldOblique", "Courier-Oblique", "Helvetica", "Helvetica-Bold",
         "Helvetica-BoldOblique", "Helvetica-Oblique", "Symbol", "Times-Bold", "Times-BoldItalic",
         "Times-Italic", "Times-Roman", "ZapfDingbats"]


def pdf_reader(name):
    with open(name, 'rb') as pdf:
        pdfread = p2.PdfFileReader(pdf)
        pages = pdfread.getNumPages()
        for page_number in range(pages):
            page = pdfread.getPage(page_number)
            content = page.extractText()
            print(content)
    return content


def draw_my_ruler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')


# draw_my_ruler(pdf)

def create_pdf_file(title='myDoc', subtitle=None, text=None,
                    title_font='Courier', title_size=36, text_font='Courier-Bold', text_size=24):
    pdf = canvas.Canvas(f'{title}.pdf')
    pdf.setTitle(title)

    # titlte set fonts
    # for font in pdf.getAvailableFonts():
    #     print(font)

    pdf.setFont(title_font, title_size)
    pdf.drawCentredString(300, 770, title)

    # sub title
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont(text_font, text_size)
    pdf.drawCentredString(290, 720, subtitle)

    # draw a line
    pdf.line(30, 710, 550, 710)

    # text
    '''make sure that each line is an word of a list (not done yet)'''
    text_lines = text.splitlines()
    pages = math.ceil(len(text_lines) / 30)
    pdf.addPage(pages)

    text = pdf.beginText(40, 680)
    text.setFont('Courier', 10)
    text.setFillColor(colors.black)
    # print(textLines)

    for line in text_lines:
        pdf.textLine(line)
        # print(line)

    pdf.drawText(text)

    pdf.save()


def generate_pdf_flask():
    pass


def pdf_merger(files_list, f_path, f_new_name):
    from PyPDF2 import PdfFileMerger
    pmerg = PdfFileMerger()
    for files in files_list:
        pmerg.append(f_path + '\\' + files)
    if not os.path.exists(f_path + '\\' + f_new_name):
        pmerg.write(f_path + '\\' + f_new_name)
    pmerg.close()


def pdf_last_blank_page_remover(f_name, new_name, path=None):
    with open(f'{path}\{f_name}', 'rb') as pdf:
        pdfRead = p2.PdfFileReader(pdf)
        pages = pdfRead.getNumPages()
        pdfWrite = p2.PdfFileWriter()
        for page in range(pages - 1):
            pdfWrite.addPage(pdfRead.getPage(page))
        with open(f'{path}\{new_name}', 'wb') as splited_file:
            pdfWrite.write(splited_file)


def change_raw_text_to_line_list(text):
    app = Flask(__name__)

    @app.route('/<name>/<location>')
    def pdf_template(name, location):
        render = render_template('pdf_template.html', name=name, location=location)
        pdf = pdfkit.from_string(render, False)

    if __name__ == '__main__':
        app.run(debug=True)
    return text.splitlines()

# pdf_reader('reportlab-userguide.pdf')

# path = r'C:\Users\victo\PycharmProjects\SDA_studies\Python_101'
# file_list = ['Hive_invitation.pdf', 'vicPDF.pdf']
#
# new_name = 'merged_test.pdf'
# pdf_merger(file_list, path, new_name)

# pdf_last_blank_page_remover('Victor Grinan CV.pdf', 'clean CV.pdf', r'C:\Users\victo\Desktop\victor 2020\2019
# papi\test pdf')

# pdf_reader(r'C:\Users\victo\Desktop\victor 2020\2019 papi\test pdf\Victor Grinan CV.pdf')


# def create_file(title="NewPDF", subtitle="", content=[], image=None):
#     pdf = canvas.Canvas(f'{title}.pdf')
#     pdf.setTitle(title)
#
#     pdf.setFillColor(colors.blueviolet)
#     pdf.setFont('Times-Bold', 36)
#     pdf.drawCentredString(300, 770, title)
#
#     pdf.setFillColor(colors.black)
#     pdf.setFont('Times-Bold', 20)
#     pdf.drawCentredString(300, 720, subtitle)
#
#     # cut the text in apropied chunks and put in list
#     texto = pdf.beginText(40, 680)
#     pdf.setFont('Times-Bold', 14)
#     pdf.setFillColor(colors.black)
#
#     for line in content:
#         texto.textLine(line)
#         # print(line)
#     pdf.drawText(texto)
#     pdf.save()
#
#
# if __name__ == "__main__":
#     text = ["hello pdf world", "how are you?"]
#
#     create_file("test1", "victor grinan", text)
#
#     # with open(r"C:\Users\victo\Desktop\victor 2020\2019 papi\email looking for kitchen work.txt", "r") as f:
#     #     content = f.readlines()
#     #
#     # create_file('Test_app', 'subtittle', content)
