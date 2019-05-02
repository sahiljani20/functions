
# from gtts import gTTS
# import pyglet
# import time, os

# def tts(text, lang):
#     file = gTTS(text = text, lang = lang)
#     filename = '/home/sahil/input.mp3'
#     file.save(filename)

#     music = pyglet.media.load(filename, streaming = False)
#     music.play()

#     time.sleep(music.duration)
#     os.remove(filename)

from gtts import gTTS
import os

# tts = gTTS(text='hello world', lang='en')
# tts.save("world.mp3")
os.system("mpg321 '/home/sahil/input.mp3'")