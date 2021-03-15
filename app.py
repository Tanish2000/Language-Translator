import googletrans
import gtts 
from googletrans import Translator
import playsound
import speech_recognition as sr
import os
import pyttsx3

# recogniser
recognizer = sr.Recognizer() 

# Languages
input_lang = 'en'
output_lang = 'hi'


#pyttsx3
engine = pyttsx3.init()

# Listening
try:
    with sr.Microphone() as source:
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-20)
        engine.say('Listening wait for a while')
        engine.runAndWait()
        print("Listening......")
        voice = recognizer.listen(source)
        words = recognizer.recognize_google(voice, language=input_lang)
        print(words)
except:
    print("Please make sure your microphone is working properly..")

#Translating
translator = Translator()
my_translation = translator.translate(words, src=input_lang ,dest=output_lang)
print("Translated words: ",my_translation.text)

#Converting to audio
converted_audio = gtts.gTTS(my_translation.text, lang=output_lang)
converted_audio.save('translated.mp3')
playsound.playsound('translated.mp3')
os.remove('translated.mp3')
