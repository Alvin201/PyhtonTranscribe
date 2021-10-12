# importing libraries
import Language
import LibraryClass
from moviepy.editor import AudioFileClip
import wave, math, contextlib
import tkinter as tk
from  tkinter import messagebox

def getLanguage(argument):
    switcher  = {
        1: "id-ID",
        2: "en-US"
    }
    return switcher.get(argument,0)


def YesNo():
    while True:
        user_input = input(LibraryClass.bcolors.OKBEIGE +"Process Complete, Try Again? (y \ n)")
        if (user_input.lower() == 'y'):
            continue
        elif (user_input.lower() == 'n'):
            print("Thank you")
            break
        else:
            print("Enter either y/n")


#variabel
format_audio = ".wav"
format_video = ".mp4"

print("Please select type")
print("1. Video")
print("2. Audio")

type = int(input('Enter a type : '))
for case in LibraryClass.switch(type):
    if case(1):
        print("Enter Filename Video (.mp4) : ")
        Vpath = input()
        transcribed_audio_file_name = Vpath+format_audio
        video_file_name = Vpath+format_video

        audioclip = AudioFileClip(video_file_name)
        audioclip.write_audiofile(transcribed_audio_file_name)
        with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            total_duration = math.ceil(duration / 60)

        print("Please select language")
        print("1. INDONESIAN")
        print("2. ENGLISH")
        ##Convert Audio
        try:
            print("Select number : ")
            languageselection = getLanguage(LibraryClass.selection.getSelection(self=""))
            print(LibraryClass.bcolors.OKVIOLET + "Your was choice " + languageselection)

            text = Language.get_large_audio_transcription(transcribed_audio_file_name, languageselection)
            print("\nFull text:", text)
            YesNo()
        except:
            print("An exception occurred")

        break
    if case(2):
        print("Please select language")
        print("1. INDONESIAN")
        print("2. ENGLISH")
        try:
            print("Select number : ")
            languageselection = getLanguage(LibraryClass.selection.getSelection(self=""))
            print(LibraryClass.bcolors.OKVIOLET + "Your was choice "+ languageselection)

            print("Enter Filename Audio ("+format_audio+") : ")
            path = input()
            text = Language.get_large_audio_transcription(path+format_audio,languageselection)
            print("\nFull text:", text)
            YesNo()
        except:
            print("An exception occurred")
        break
