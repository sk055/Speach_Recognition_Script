import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone() as source:

    print("Speak Now...")
    # voice = rec.record(source, duration=3)
    voice = rec.record(source,duration=3)
    try:
        toText = rec.recognize_google(voice)
        print(toText)
        print("")

    except:
        print("Voice Not Recognised..")

