from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Editor")
root.iconbitmap("Ala-Too.png")

class logo():
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.Im = ImageTk.PhotoImage(Image.open("Ala-Too.png"))
        self.my_label = Label(image=self.Im)
        self.my_label.pack()

        self.button_quit = Button(master, text="Exite", command=master.quit)
        self.button_quit.pack()


k = logo(root)
root.mainloop()