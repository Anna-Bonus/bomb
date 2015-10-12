from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import time

MAX_TIME = 5


def text_into_image(old_image, text):
    image = old_image.copy()
    txt = Image.new('RGBA', image.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    font = ImageFont.truetype('BOOKOS.TTF', 120)
    d.text((50,20), text, fill=(255, 0, 0, 250), font=font)
    image.paste(txt, (0, 0), txt)
    return image

class App():
    def __init__(self):
        self.main_window = Tk()
        self.label = Label()
        self.label.pack()
        self.image_bomb = Image.open('bomb.jpg').convert('RGBA')
        self.now = MAX_TIME + 1
        self.make_boom()
        self.main_window.minsize(width=300, height=300)


    def start_boom(self):
        title = 'Boom at ' + str(time.ctime(time.time()+MAX_TIME))
        self.main_window.title(title)
        self.main_window.mainloop()

    def set_image(self):
        self.photo_image = ImageTk.PhotoImage(self.new_pict)
        self.label['image'] = self.photo_image
        self.label.image = self.photo_image

    def make_boom(self):
        if self.now >= 0:
            self.now -= 1
            self.new_pict = text_into_image(self.image_bomb, str(self.now))
            self.set_image()
            self.main_window.after(1000, self.make_boom)
        if self.now < 0:
            self.image_bomb = Image.open('boom.jpg')
            self.new_pict = self.image_bomb
            self.set_image()

app = App()
#app.start_boom()