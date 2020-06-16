from gtts import gTTS

google_voice = gTTS(text="Hello Avraham", lang='ru')
google_voice.save('sound.mp3')
