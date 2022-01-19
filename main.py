import speech_recognition as sr
import os

r = sr.Recognizer()
folder_name = "c:\Temp"
whole_text = ""


def init(name):
    print(name)
    listaMic = sr.Microphone.list_microphone_names()
    print(listaMic.__sizeof__())
    print(listaMic)
    chunk_filename = os.path.join(folder_name, f"chunk.wav")

    with sr.Microphone() as source:
        whole_text = ""
        text = ""
        # read the audio data from the default microphone
        print("Listening ...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        try:
            text = r.recognize_google(audio_data)
            #text = r.recognize_bing(audio_data, "en-US",False)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text


if __name__ == '__main__':
    init('Speach recognition v 1.0')


