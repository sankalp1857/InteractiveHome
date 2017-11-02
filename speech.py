

import speech_recognition as sr


def recognise():
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
        print("System active...")

        with m as source:
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            print (value)
            return(value)
        except sr.UnknownValueError:
            print("Oops didn't catch that!")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass
