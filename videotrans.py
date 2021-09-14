import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from datetime import datetime

format_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
transcribed_audio_file_name = "audio_only_ind_video.wav"
zoom_video_file_name = "tsdt.mp4"


audioclip = AudioFileClip(zoom_video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    total_duration = math.ceil(duration / 60)

try:
    r = sr.Recognizer()
    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i*60, duration=60)
        f = open("transcription_ind_video" + format_date + ".txt", "a")
        # f.write(r.recognize_google(audio, language="en-US"))
        f.write(r.recognize_google(audio, language="id-ID"))
        f.write(" ")
except Exception as e:
        print (e)
f.close()
