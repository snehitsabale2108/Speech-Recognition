import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as s:
    print("Speak")
    audio = r.listen(s)
    t = r.recognize_google(audio)
    print("you said: ", t)
