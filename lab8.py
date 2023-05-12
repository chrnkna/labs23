from PIL import Image, ImageFont, ImageDraw
def z1():
    filn= "postcard.jpg"
    with Image.open(filn) as img:
        img.load()
    cropp_img= img.crop((110, 210, 640, 470))
    cropp_img.save("crop.postc.jpg")

def z2():
    from PIL import Image
    g = {1: "postcard.jpg", 2: "8m.jpg", 3: "23f.jpg", 4: "dr.jpg"}

    print("1-НГ"
          "2-8 марта"
          "3-23 февраля"
          "4-др")
    a= int(input("Для открытия открытки введите число, соответсвующее номеру праздника: "))

    filename = g[a]
    with Image.open(filename) as img:
        img.load()
    img.show()
def z3():
  i=Image.open('Z:\Чернейкина Юлия\lab8\postcard.jpg')
  name=input("Введите имя получателя- ")
  font = ImageFont.truetype("Z:\Чернейкина Юлия\lab8/arial_bold.ttf",35)
  d=ImageDraw.Draw(i)
  d.text((20,20), name + ", поздравляю!", font=font, fill='white')
  i.show()
  i.save(name+"_postcard.png")

z3()