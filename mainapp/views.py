from django.shortcuts import render
from gtts import gTTS
from django.http import HttpResponse, FileResponse


def text_to_speech(req, input):
    text = "Something went wrong. please try again later" if not input else input
    lang = "en"
    voice = gTTS(text=text, lang=lang, slow=False)
    voice.save("c:\\voice.mp3")
    return FileResponse(open("c:\\voice.mp3", "rb"))

