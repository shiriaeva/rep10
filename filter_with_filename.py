from PIL import Image
import numpy as np


def get_mid_bright(block, element_side, step):
    midBright = block[:element_side, :element_side].sum() // (element_side * element_side)
    return int(midBright // step) * step / 3


def transform_img(arr, element_side, step):
    length = len(arr)
    width = len(arr[1])
    for row in range(0, length, element_side):
        for col in range(0, width, element_side):
            arr[row: row + element_side, col: col + element_side] = get_mid_bright(
                arr[row: row + element_side, col: col + element_side], element_side, step
            )

    return arr


def main():
    img = Image.open("img.jpg")
    arr = np.array(img)
    element_side = 10
    gradation = 50
    step = 255 // (gradation - 1)

    res = Image.fromarray(transform_img(arr, element_side, step))
    res.save("result.jpg")


if __name__ == '__main__':
    main()