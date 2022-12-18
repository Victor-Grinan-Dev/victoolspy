from PIL import Image
from pdf2image import convert_from_path


import os

all_files = [
    r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates\2015 kokki todistus.pdf",
    r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates\2015 yrittaja todistus.pdf",
    r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates\Bachelor.pdf",
    r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates\python_fundamentals_victor_grinan.pdf",
    r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates\toefl_english_scores.pdf",
]
directory = r"C:\Users\victo\Desktop\projects\Victools(p)\victors_certificates"


def precess_img(img):
    basewidth = 300
    img = Image.open(img)  # 'somepic.jpg'
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(img)  # 'somepic.jpg'


def pdf_2_img(pdf_file): # not working
    pages = convert_from_path(pdf_file, 500)

    # get a new name
    full_path = pdf_file.split("\\")
    print(full_path)
    new_name, _ = full_path[-1].split(".")
    print(new_name)
    # Saving pages in jpeg format
    for page in pages:
        page.save(f'{new_name}.jpg', 'JPEG')


def pdf_2_loose_imgs(pdf_file):
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page' + str(i) + '.jpg', 'JPEG')


def many_docs_to_process(directorio, ext: str = "pdf", pdf_to_img: bool = True):
    for filename in os.listdir(directorio):
        if filename.endswith(f".{ext}"):
            print(os.path.join(directorio, filename))
            pdf_file = os.path.join(directorio, filename)

            if pdf_to_img:
                pdf_2_img(pdf_file)
            else:
                # TODO: give option of processing the pdfs
                pass

        else:
            continue


file = all_files[0]
pdf_2_img(file)
# many_docs_to_process(carpeta)
