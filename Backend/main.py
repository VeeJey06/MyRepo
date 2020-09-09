from gtts import gTTS


class Voice:
    def __init__(self):
        self.text = "Something went wrong. please try again later"
        self.lang = "en"

    def text_to_speech(self):
        voice = gTTS(text=self.text, lang=self.lang, slow=False)
        voice.save("voice.mp3")

    # def

if __name__ == '__main__':
    a = Voice()
    a.text_to_speech()