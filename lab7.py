from PIL import Image
import cv2

def zadanie_1():
    print("задание 1")
    filename = "F:\picture.png"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, heith = img.size
    format = img.format
    mode = img.mode
    print("ширина:", width)
    print("высота:", heith)
    print("формат:", format)
    print("цветовая модель: ", mode)



def zadanie_2():
    print("задание2")
    filename = "F:\lab\p5.jpg"
    with Image.open(filename) as img:
        img.load()
    newimg = img.resize((img.width // 3, img.height // 3))
    newimg.save("resized_bee1.jpg")
    newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
    newimg.save("resized_and_rotated1_bee2.jpg")
    newimg1 = img.transpose(Image.ROTATE_180)
    newimg1.save("resized_and_rotated2_bee3.jpg")

def zadanie_3():
    print("задание3")
    filename = "F:\lab\pcat1.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_cat.jpg")

    filename = "F:\lab\p2.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p2.jpg")

    filename = "F:\lab\p3.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p3.jpg")

    filename = "F:\lab\p4.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p4.jpg")

    filename = "F:\lab\p5.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("black_and_white_p5.jpg")


def zadanie_4():
    print("задание4")
    filename = "F:\lab\pcat1.jpg"
    with Image.open(filename) as img:
        img.load()
    watermark = Image.open('F:\lab\watermark.png')

    img.paste(watermark, (450, 230), watermark)
    img.save("img_with_watermark.png")

zadanie_1(), zadanie_2(), zadanie_3(), zadanie_4()