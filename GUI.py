from tkinter import *  # pip install tkinter
from PIL import Image, ImageTk, ImageSequence  # pip install Pillow
import time

root = Tk()
root.geometry("1000x500")
root.title("Sapphire")  # Add the title "Sapphire"


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global vid
    vid = vid.open("original-3b009b0c0dccfa3891b49158bb3dbd81")  # Enter the gif address
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0

    for vid in ImageSequence.Iterator(vid):
        vid = vid.resize((1000, 500))
        vid = ImageTk.PhotoImage(vid)
        lbl.config(video=vid)
        root.update()
        time.sleep()


play_gif()
root.mainloop()
