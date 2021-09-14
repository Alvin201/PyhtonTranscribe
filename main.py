# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyaudio
import speech_recognition as sr


#print(sr.Microphone.list_microphone_names())
microphone = sr.Microphone()
recognizer = sr.Recognizer()
#dir(sr.Recognizer)

import googletrans
import speech_recognition as sr

translator = googletrans.Translator()

try:
    with sr.Microphone() as source:
        print('Speak Now')
        microphone.adjust_for_ambient_noise(source,duration=1)
        voice= recognizer.listen(source)
        text= recognizer.recognize_google(voice)
        print(text)
        translated = translator.translate(text, src='id_ID')
        print(translated.text)
except:
     pass

# try:
#     translated = translator.translate(text, src='en')
#     print(translated.text)
# except:


# print("Let's speak!!")
# with sr.Microphone() as source:
#     microphone.adjust_for_ambient_noise(source,duration=1)
#     # r.energy_threshold()
#     print("say anything : ")
#     audio= recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         print(text)
#     except:
#         print("sorry, could not recognise")

# with microphone as micro_audio:
#     print("Start Speaking ...")
#
#     recognizer.adjust_for_ambient_noise(micro_audio)
#     audio = recognizer.listen(micro_audio)
#
#     print("Converting your speech to text...")
#     print("Did you say: " + recognizer.recognize_google(audio) + "?")

#Transcribing Text from Audio Files
# audio_data = sr.AudioFile('E:/audio_file.wav')
# recognizer = sr.Recognizer()
# with audio_data as file_audio:
#     print("Start transcribing file ...")
#
#     recognizer.adjust_for_ambient_noise(file_audio)
#
#     audio = recognizer.record(file_audio)
#
#     print(recognizer.recognize_google(audio))
