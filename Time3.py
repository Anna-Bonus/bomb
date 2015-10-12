from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import time
import winsound
import threading

MAX_TIME = 4


def text_into_image(old_image, text):
    image = old_image.copy()
    txt = Image.new('RGBA', image.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    font = ImageFont.truetype('BOOKOS.TTF', 120)
    d.text((0, 0), text, fill=(255, 0, 0, 250), font=font)
    image.paste(txt, (image.size[0]//4, image.size[1]//4), txt)
    return image


class App():
    def __init__(self):
        self.main_window = Tk()
        self.label = Label()
        self.label.pack()
        self.image_bomb = Image.open('bomb.jpg').convert('RGBA')
        self.image_boom = Image.open('boom.jpg')
        self.main_window.minsize(width=500, height=300)

    def plante_bomb(self):
        self.boom_time_in_seconds = time.time()+MAX_TIME
        title = 'Boom at ' + time.ctime(self.boom_time_in_seconds)
        self.main_window.title(title)
        self.make_boom(MAX_TIME)
        self.main_window.mainloop()

    def set_image(self, img):
        photo_image = ImageTk.PhotoImage(img)
        self.label['image'] = photo_image
        self.label.image = photo_image

    def make_boom(self, counter):
        if counter > 0:
            # winsound.MessageBeep()
            new_pict = text_into_image(self.image_bomb, str(counter))
            self.set_image(new_pict)
            threading.Thread(target=winsound.PlaySound, args=('1.mp3', winsound.SND_FILENAME)).start()
            self.main_window.after(3000, lambda: self.make_boom(counter-1))
        if counter == 0:
            self.set_image(self.image_boom)

app = App()
app.plante_bomb()