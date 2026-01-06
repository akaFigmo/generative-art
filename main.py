from PIL import Image
import numpy as np


def create_image_array():
    h = 500
    w = 500
    arr = np.zeros((h, w, 4), dtype=np.uint8)
    return arr


def show_image_array(array):
    img = Image.fromarray(array, mode="RGBA")
    img.show()


def main():
    arr = create_image_array()
    arr = make_pretty(arr)
    show_image_array(arr)


def make_pretty(arr):
    return arr


if __name__ == "__main__":
    main()
