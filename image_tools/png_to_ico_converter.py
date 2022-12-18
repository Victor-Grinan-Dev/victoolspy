from image_tools.PIL import Image


def change_ext(filename, ext='ico'):
    # filename = r'logo.png'
    img = Image.open(filename)

    img.save(f'{filename.split(".")[0]}.{ext}')


if __name__ == '__main__':

    rhino_annu = 'C:/Users/victo/Desktop/game resorces/rhino_annu.png'
    # change_ext(r'C:\Users\victo\PycharmProjects\study_timer\tomato.png')

    change_ext(rhino_annu, 'gif')
