import whisper

modelo = whisper.load_model("base")
resposta = modelo.transcribe("")
print(resposta["text"])
