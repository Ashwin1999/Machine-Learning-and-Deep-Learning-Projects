import speech_recognition as sr
from textblob import TextBlob

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk to me: ")
    audio = r.listen(source)

    try:
        txt = r.recognize_google(audio)
        polar = TextBlob(txt).sentiment.polarity
        if polar > 0:
            if polar > 0.3:
                print("Positive")
            else:
                print("Neutral")
        elif polar < 0:
            if polar < -0.3:
                print("Negative")
            else:
                print("Neutral")
    except:
        print("An exception occured")
