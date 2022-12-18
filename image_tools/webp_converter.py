from PIL import Image


def convert_to_webp(path_to_image):
    destination = path_to_image.with_suffix(".webp")
    image = Image.open(path_to_image)
    image.save(destination, format="webp")

    return destination
