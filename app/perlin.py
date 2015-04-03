from color_helpers import create_hsv, get_rgb
from interpolation import bilerp, cos_interp
from math import sin, cos, pi, sqrt, floor


def create_perlin_data(img_sz,
                       split,
                       fn_create_color=create_hsv,
                       fn_get_rgb=get_rgb):

    basis = [[fn_create_color() for x in range(split[0] + 1)]
             for x in range(split[1] + 1)]

    seglen = (img_sz[0] / split[0], img_sz[1] / split[1])

    def getPxColor(pxIdx):
        x = pxIdx % img_sz[0]
        y = pxIdx // img_sz[1]
        bx0 = (x * split[0]) // img_sz[0]
        by0 = (y * split[1]) // img_sz[1]
        bx1 = bx0 + 1
        by1 = by0 + 1
        wx = (x % seglen[0]) / seglen[0]
        wy = (y % seglen[1]) / seglen[1]
        b00 = basis[bx0][by0]
        b01 = basis[bx1][by0]
        b10 = basis[bx0][by1]
        b11 = basis[bx1][by1]

        h = bilerp(b00[0], b01[0], b10[0], b11[0], wx, wy, cos_interp)
        s = bilerp(b00[1], b01[1], b10[1], b11[1], wx, wy, cos_interp)
        v = bilerp(b00[2], b01[2], b10[2], b11[2], wx, wy, cos_interp)

        rgb = fn_get_rgb((h, s, v))

        return rgb

    pxCnt = img_sz[0] * img_sz[1]
    data = bytes(b for i in range(pxCnt) for b in getPxColor(i))
    return data

if __name__ == "__main__":
    from PIL import Image, ImageDraw
    from perlin import create_perlin_data
    import os

    size = (512, 512)
    split = (4, 4)

    # data = create_perlin_data(size, split)
    data = create_perlin_data(size, split)

    im = Image.frombytes("RGB", size, data)

    filepath = os.path.dirname(os.path.abspath(__file__))

    im.save(os.path.join(filepath, "test.png"), "png")
