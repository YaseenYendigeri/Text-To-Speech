from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()


def textTOSpeech(a):
    t = a
    o = gTTS(text=t, lang="en", slow=False)
    o.save("op2.mp3")
    os.system("start op2.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)
b = Button(text="Start", command=lambda:textTOSpeech(entry.get()))
canvas.create_window(200, 230, window=b)


root.mainloop()

