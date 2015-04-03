if __name__ == "__main__":
    from PIL import Image, ImageDraw
    from perlin import create_perlin_data, create_simplex_data
    import os

    size = (512, 512)
    split = (2, 2)

    data = create_perlin_data(size, split)

    im = Image.frombytes("RGB", size, data)

    filepath = os.path.dirname(os.path.abspath(__file__))

    im.save(os.path.join(filepath, "test.png"), "png")
