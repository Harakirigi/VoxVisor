import speech_recognition as sr

def transcribe_audio(audio_bytes):
    recognizer = sr.Recognizer()

    # Преобразуем байты в формат, который принимает SpeechRecognition
    audio_data = sr.AudioData(audio_bytes, 16000, 2)

    # Используем Google API для транскрипции
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError:
        return "Ошибка запроса к серверу для транскрибации"
