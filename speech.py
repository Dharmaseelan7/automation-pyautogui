import speech_recognition as sr


recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    print('say something')
    audio = recognizer.listen(mic)
    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(text)

    except:
        recognizer = sr.Recognizer()
