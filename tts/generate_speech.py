import pyttsx3
import os

os.makedirs("audio", exist_ok=True)

engine = pyttsx3.init()
engine.setProperty("rate", 170)     # speech speed
engine.setProperty("volume", 1.0)

text = "Hello, this is a real time talking avatar system with proper lip sync."

engine.save_to_file(text, "audio/tts.wav")
engine.runAndWait()

print("audio/tts.wav generated")
