# pip install tika
# pip install gtts
# pip install googletrans==3.1.0a0

import gtts
from googletrans import Translator
from tika import parser

pdf = parser.from_file('b7.pdf')
print(pdf['content'])

tts = gtts.gTTS(pdf['content'], lang='en')
tts.save('audiobook2.mp3')

