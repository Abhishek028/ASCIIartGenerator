from PIL import Image


def crop(path, height, width):
    mean = []
    im = Image.open(path)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, width):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            a = a.convert('LA')
            total = 0
            crowidth, croheight = a.size
            for k in range(0, crowidth):
                for j in range(0, height):
                    total += a.getpixel((k, j))[0]
            mean = total / (crowidth * croheight)
            f = open("picture.txt", "a+")
            if mean <= 150:
                f.write("@")
            else:
                f.write(" ")
        f.write("\n")
    f.close()


crop("deathReaper.png", 2, 2)
