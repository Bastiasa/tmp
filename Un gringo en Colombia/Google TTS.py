from gtts import gTTS

texto1 = "Quiero comerme a Brad."
texto2 = "Me gustaría comerme su arepa."

tts = gTTS(text=texto1, lang="es")
tts.save("Quiero comerme a Brad.mp3")

tts = gTTS(text=texto2, lang="es")
tts.save("Me gustaría comerme su arepa.mp3")

print("Finished.")
