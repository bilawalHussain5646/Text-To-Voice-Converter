# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
mytext = '''Halo semua, perkenalkan saya fitri nabila. Saya baru saja berhenti bekerja dikarenakan calon suami saya meminta saya untuk berhenti bekerja dikarenakan cemburu dengan rekan kerja saya, sekian dan terima kasih'''

# Language in which you want to convert
language = 'id'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")