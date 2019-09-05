import speech_recognition as sr

rec = sr.Recognizer()

audio_file = sr.AudioFile('ishwar.wav')



with audio_file as source:

    rec.pause_threshold = 2
    voice = rec.listen(source)

    try:

        toTextHI = rec.recognize_google(voice, language= 'hi-IN')
        print(toTextHI)

    except:
        print("Voice Not Recognised..")

