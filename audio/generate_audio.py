import os
import numpy as np
import soundfile as sf

os.makedirs("audio", exist_ok=True)

sr = 16000
duration = 3.0

t = np.linspace(0, duration, int(sr * duration), endpoint=False)
signal = 0.4 * np.sin(2 * np.pi * 220 * t)

sf.write("audio/input.wav", signal, sr, subtype="PCM_16")

print("CREATED:", os.path.abspath("audio/input.wav"))
print("SIZE:", os.path.getsize("audio/input.wav"), "bytes")
