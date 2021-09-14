# import speech_recognition as sr
#
#
#
#
# def main():
#     sound = "output.wav"
#
#     r = sr.Recognizer()
#
#
#     with sr.AudioFile(sound) as source:
#         r.adjust_for_ambient_noise(source)
#
#
#         print("Converting Audio To Text ..... ")
#
#
#         audio = r.listen(source)
#
#
#
#     try:
#         print("Converted Audio Is : \n" + r.recognize_google(audio))
#
#
#     except Exception as e:
#         print("Error {} : ".format(e) )
#
#
#
# if __name__ == "__main__":
#     main()


import speech_recognition as sr

r = sr.Recognizer()

audio = 'output.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio,language="en-EN")
    f = open("demofile2.txt", "a")
    f.write(text)
    f.close()

    f = open("demofile2.txt", "r")
    print(f.read())
    #print (text)

except Exception as e:
    print (e)