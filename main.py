# pip install tika
# pip install gtts
# pip install googletrans==3.1.0a0

import gtts
from googletrans import Translator
from tika import parser

pdf = parser.from_file('b77.pdf')
print(pdf['content'])
# #Перевод сразу на русский-----------------------------------------
# translator = Translator()
# translated = translator.translate(pdf['content'], dest='ru')
# translated_2 = translated.text
# print(translated_2)
#
# tts = gtts.gTTS(translated_2, lang='ru')
# tts.save('audiobook3.mp3')
# -------------------------------------------------------
tts = gtts.gTTS(pdf['content'], lang='en')
tts.save('audiobook2.mp3')
