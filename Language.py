import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from datetime import datetime

# create a speech recognition object
r = sr.Recognizer()
format_date = datetime.today().strftime('%Y-%m-%d')



# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path, lang='en-US'):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub

    sound = AudioSegment.from_wav(path)

    dBFS = sound.dBFS

    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=700,
                              # adjust this per requirement
                              silence_thresh=dBFS - 22,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    print("Please Wait...")
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = folder_name + "/" + "chunk{0}.wav".format(i)
        # chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        print("exporting", chunk_filename)
        audio_chunk.export(chunk_filename, bitrate='396k', format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language=lang)
                # export to file
                f = open("result.txt", "a")
                f.write(chunk_filename + ":" + text + "\n")
                f.write("")

            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text
