from gtts import gTTS
import os

t = open("demo.txt", "r").read()
o = gTTS(text=t, lang="en", slow=False)
o.save("op2.mp3")

os.system("start op2.mp3")