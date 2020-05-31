from gtts import gTTS
import os
def convert_to_audio(data,name):
    language = 'en'
    audio_book = gTTS(text=data, lang=language, slow=False)
    audio_book.save('mp3_files/'+name+".mp3")