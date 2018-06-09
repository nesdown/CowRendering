from PIL import Image
import numpy as np


def make_array(pixs):
    return np.array(pixs, dtype=np.dtype('uint8, uint8, uint8'))


def make_bmp(pixels, resolution, filename):
    array = make_array(pixels)
    image = Image.Image()
    image = Image.fromarray(array, 'RGB')

    image.save(filename, 'BMP')

    return None
