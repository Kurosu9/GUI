from PIL import Image, ImageFilter, ImageDraw, ImageFont


def res(self):
    i = Image.open(self)
    res = i.convert('L')
    res1 = res.filter(ImageFilter.DETAIL)
    res2 = res1.resize((1080, 1080))
    width, height = res2.size

    draw = ImageDraw.Draw(res2)
    text = "KUROSU9"
    title = "white"
    font = ImageFont.truetype("arial.ttf", 80)
    textwidth, textheight = draw.textsize(text, font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, title, font=font)

    res2.show()
