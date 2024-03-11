import whisper

modelo = whisper.load_model("base")
resposta = modelo.transcribe("D:\Desktop\Imersion HUB\ime1.mp3")
print(resposta["text"])
