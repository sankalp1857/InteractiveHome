# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

def feedback(mode,feed):
    myobj = gTTS(text=feed, lang='hi', slow=False)
    myobj.save("feedback.mp3")
    os.system(" feedback.mp3")