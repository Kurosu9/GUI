from PIL import Image


def con(self):
        # Convert Image to Black and White
        i = Image.open(self)
        ibw = i.convert('L')

        ibw.show()
