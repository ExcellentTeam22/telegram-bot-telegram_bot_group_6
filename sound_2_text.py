import speech_recognition as sr

def get_rec_text(idk):
    print("idk")

if __name__ == "__main__":
    # Initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone() as sound_file:
        r.adjust_for_ambient_noise(sound_file)
        print("recording")
        audio = r.listen(sound_file)
        print("stopped rec")
        try:
            text = r.recognize_google(audio, show_all=True)
            print(text)
        except:
            print('Sorry.. run again...')