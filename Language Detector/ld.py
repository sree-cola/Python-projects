import speech_recognition as sr
from langdetect import detect

def detect_language():
    # Record audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    
    try:
        # Transcribe the speech
        text = r.recognize_google(audio)
        print(f"Transcribed text: {text}")
        
        # Detect the language
        language = detect(text)
        print(f"Detected language: {language}")
        
    except sr.UnknownValueError:
        print("Unable to transcribe speech.")
    except sr.RequestError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    detect_language()
