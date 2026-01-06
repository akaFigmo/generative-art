from PIL import Image
import numpy as np
import random


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
    print(arr.shape)
    # arr[:, :, 3] = 255


    for i in range(100):
        # Make a random rectangle
        rect = make_random_rectangle()
        
        # Get a random point on x, y for red channel
        point_x = int(random.uniform(0, 500))
        point_y = int(random.uniform(0, 500))
        print(f"Point: x={point_x}, y={point_y}")

        # Add the random rectangle to the image at the point
        # slice the arrayi
        print(rect.shape)
        dx = rect.shape[0]
        dy = rect.shape[1]
        print(f"dx={dx}, dy={dy}")
        slice_x = min(point_x+dx, 500)
        slice_y = min(point_y+dy, 500)

        # Truncate the rectangle
        # The rectangle can only be as big as
        # the minimum of 200-point_x and dx
        rect = rect[:min(dx, 500-point_x), :min(dy, 500-point_y)]
        print(f"Truncated Rectangle: h={rect.shape[0]}, w={rect.shape[1]}")

        color = int(random.uniform(0, 3))
        
        arr[point_x:slice_x, point_y:slice_y, color] = rect
        arr[point_x:slice_x, point_y:slice_y, 3] = 255

    print(arr[0, 0, 0])
    return arr

def make_random_rectangle():
    max_height = 100
    max_width = 100
    w = int(random.uniform(1, max_width))
    h = int(random.uniform(1, max_height))
    rectangle = np.zeros((h, w), dtype=np.uint8)
    print(f"Rectangle: w={w}, h={h}")
    color = random.uniform(50, 255)
    rectangle[:,:]=color
    return rectangle

if __name__ == "__main__":
    main()
