# pip install tika
# pip install gtts
# pip install googletrans==3.1.0a0

import gtts
from googletrans import Translator
from tika import parser

pdf = parser.from_file('b7.pdf')
print(pdf['content'])

translator = Translator()
translated = translator.translate(pdf['content'], dest='ru')
translated_2 = translated.text

tts = gtts.gTTS(translated_2, lang='ru')
tts.save('audiobook3.mp3')

