import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
from watermark import mark
from style import con
from size import re
from mix import res


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Menu)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.title = master.title("IMAGE EDITOR")
        self.im = PhotoImage(file="Ala-Too.png")
        self.iconphoto = master.iconphoto(False, self.im)
        # self.resizable = master.resizable(0, 0)

        self.logo = ImageTk.PhotoImage(Image.open("Ala-Too.png"))
        tk.Label(self, image=self.logo).pack(side="top")
        tk.Label(self, text="IMAGE EDITOR", font="Times_New_Roman"
                 ).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Add Watermark", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Watermark)).pack(pady=10)
        tk.Button(self, text="Black and White", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Style)).pack(pady=10)
        tk.Button(self, text="Resize", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Resize)).pack(pady=10)
        tk.Button(self, text="MIX", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Mix)).pack(pady=10)
        tk.Button(self, text="Copyright Section", font="Comic_Sans_MS",
                  command=self.txt).pack(pady=10)
        tk.Button(self, text="Exit", font="Comic_Sans_MS",
                  command=self.exit).pack()

    def txt(self):
        messagebox.showinfo("Copyright", '''Thank you for using this'''
                            ''' IMAGE EDITOR. @KUROSU9''')
        self.master()

    def exit(self):
        choice = messagebox.askyesno("Quit", "Do you want to quit?")
        if choice:
            self.master.destroy()


class Watermark(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Select Image", font="Comic_Sans_MS",
                  command=self.open).pack()
        tk.Button(self, text="Return to Menu", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Menu)).pack()

    def open(self):
        self.filename = filedialog.askopenfilename(initialdir="*",
                                                   title="Select a file",
                                                   filetypes=(("png files",
                                                              "*.png"), (
                                                              "jpg files",
                                                              "*.jpg"), (
                                                              "all files",
                                                              "*.*")))
        tk.Label(self, text=self.filename).pack()
        self.s_im = ImageTk.PhotoImage(mark(self.filename))
        tk.Label(self, image=self.s_im).pack()


class Style(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Select Image", font="Comic_Sans_MS",
                  command=self.open).pack()
        tk.Button(self, text="Return to Menu", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Menu)).pack()

    def open(self):
        self.filename = filedialog.askopenfilename(initialdir="*",
                                                   title="Select a file",
                                                   filetypes=(("png files",
                                                              "*.png"), (
                                                              "jpg files",
                                                              "*.jpg"), (
                                                              "all files",
                                                              "*.*")))
        tk.Label(self, text=self.filename).pack()
        self.s_im = ImageTk.PhotoImage(con(self.filename))
        tk.Label(self, image=self.s_im).pack()


class Resize(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Select Image", font="Comic_Sans_MS",
                  command=self.open).pack()
        tk.Button(self, text="Return to Menu", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Menu)).pack()

    def open(self):
        self.filename = filedialog.askopenfilename(initialdir="*",
                                                   title="Select a file",
                                                   filetypes=(("png files",
                                                              "*.png"), (
                                                              "jpg files",
                                                              "*.jpg"), (
                                                              "all files",
                                                              "*.*")))
        tk.Label(self, text=self.filename).pack()
        self.s_im = ImageTk.PhotoImage(re(self.filename))
        tk.Label(self, image=self.s_im).pack()


class Mix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Select Image", font="Comic_Sans_MS",
                  command=self.open).pack()
        tk.Button(self, text="Return to Menu", font="Comic_Sans_MS",
                  command=lambda: master.switch_frame(Menu)).pack()

    def open(self):
        self.filename = filedialog.askopenfilename(initialdir="*",
                                                   title="Select a file",
                                                   filetypes=(("png files",
                                                              "*.png"), (
                                                              "jpg files",
                                                              "*.jpg"), (
                                                              "all files",
                                                              "*.*")))
        tk.Label(self, text=self.filename).pack()
        self.s_im = ImageTk.PhotoImage(res(self.filename))
        tk.Label(self, image=self.s_im).pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
