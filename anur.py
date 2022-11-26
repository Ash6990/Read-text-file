from gtts import gTTS
import os
fh=open("test.txt","r")
my=fh.read().replace("\n"," ")
lng="en"
output = gTTS(text=my,lang=lng,slow=False)
output.save("output.mp3")
fh.close()
os.system("start output.mp3")

