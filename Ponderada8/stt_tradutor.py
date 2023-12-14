import speech_recognition as sr
from googletrans import Translator

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    # Carrega o arquivo de áudio
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    # Reconhece o texto do áudio
    try:
        text = recognizer.recognize_google(audio_data, language="pt-BR")
        return text
    except sr.UnknownValueError:
        return "Não foi possível entender a fala"
    except sr.RequestError:
        return "Não foi possível se comunicar com o serviço de reconhecimento de fala"

def translate_text(text, target_language="en"):
    translator = Translator()

    # Traduz o texto para o idioma desejado
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Caminho do arquivo de áudio
audio_file_path = "manda-foto-na-moral.wav"

# Transcreve o áudio para texto
transcribed_text = transcribe_audio(audio_file_path)

# Traduz o texto reconhecido para o idioma desejado (inglês por padrão)
translated_text = translate_text(transcribed_text)

print("Transcrição do áudio:", transcribed_text)
print("Tradução:", translated_text)