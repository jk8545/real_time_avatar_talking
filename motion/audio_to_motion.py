import os
import numpy as np
import soundfile as sf
from scipy.ndimage import gaussian_filter1d

def extract_audio_features(audio_path, fps=30):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(audio_path)

    y, sr = sf.read(audio_path)
    if y.ndim > 1:
        y = y.mean(axis=1)

    hop = sr // fps

    # Energy (loudness → mouth openness)
    energy = np.array([
        np.sqrt(np.mean(y[i:i+hop] ** 2))
        for i in range(0, len(y), hop)
    ])

    # Spectral centroid proxy (brightness → lip width)
    centroid = np.array([
        np.mean(np.abs(np.fft.rfft(y[i:i+hop])))
        for i in range(0, len(y), hop)
    ])

    energy = gaussian_filter1d(energy, 1.2)
    centroid = gaussian_filter1d(centroid, 1.2)

    # Normalize
    energy = (energy - energy.min()) / (np.ptp(energy) + 1e-6)
    centroid = (centroid - centroid.min()) / (np.ptp(centroid) + 1e-6)

    return energy, centroid


def audio_to_motion(energy, centroid):
    n = len(energy)
    t = np.linspace(0, 1, n)

    mouth_open = energy ** 0.8
    lip_width = 0.5 + centroid * 0.6

    jaw_drop = mouth_open * 1.3
    head_nod = gaussian_filter1d(np.gradient(mouth_open), 2) * 12
    head_sway = np.sin(2 * np.pi * t * 0.6) * 4

    # Eye blink (periodic, not audio-driven)
    blink = (np.sin(2 * np.pi * t * 0.9) > 0.95).astype(float)

    return {
        "mouth_open": mouth_open,
        "lip_width": lip_width,
        "jaw_drop": jaw_drop,
        "head_nod": head_nod,
        "head_sway": head_sway,
        "blink": blink
    }
