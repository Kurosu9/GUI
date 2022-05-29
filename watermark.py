from PIL import Image, ImageDraw, ImageFont


def mark(self):
        # Watermark
        w = Image.open(self)
        width, height = w.size
        draw = ImageDraw.Draw(w)
        text = "KUROSU9"
        title = "blue"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        w.show()
