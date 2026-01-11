🧑‍💻 Open-Source Text-Driven Talking Avatar (Prototype)
Overview

This repository contains a fully open-source prototype of a real-time talking avatar system that converts text input into a lip-synchronized talking avatar video.

The project is designed as a minimal but complete proof-of-concept for an end-to-end pipeline:

Text → Speech → Audio-Driven Motion → Avatar Rendering → Video with Audio

The focus is on temporal consistency, synchronization, modularity, and reproducibility, rather than photorealism.

Key Features

✅ Text-to-speech (offline, no cloud APIs)

✅ Audio-driven facial motion

✅ Lip-sync based on speech dynamics

✅ Head motion and blinking for realism

✅ Combined audio + video output (single MP4)

✅ Fully open-source dependencies

✅ No model training required

✅ Runs on CPU (GPU optional)

System Architecture
Text Input
   ↓
Text-to-Speech (pyttsx3)
   ↓
Speech Audio (.wav)
   ↓
Audio Feature Extraction
   ↓
Temporal Motion Model
   ↓
Avatar Renderer (2D)
   ↓
Video Frames
   ↓
Audio + Video Muxing
   ↓
Final MP4 Output


Each stage is implemented as a separate module, making the system easy to extend (e.g., neural TTS, 3D avatars, learned motion models).

Project Structure
audio_to_avatar/
├── audio/
│   ├── tts.wav
│   └── generate_audio.py
├── motion/
│   └── audio_to_motion.py
├── renderer/
│   └── face_renderer.py
├── demo/
│   └── final_avatar.mp4
├── inference.py
├── requirements.txt
├── LICENSE
└── README.md

Installation
Requirements

Python 3.9+

Windows / Linux / macOS

FFmpeg available in PATH

Install dependencies
pip install -r requirements.txt


requirements.txt

numpy
scipy
soundfile
opencv-python
moviepy
pyttsx3


No C++ compiler or GPU is required.

Usage
1️⃣ Generate speech from text

Edit the text inside:

tts/generate_speech.py


Then run:

python tts/generate_speech.py


This creates:

audio/tts.wav

2️⃣ Generate the talking avatar video
python inference.py


Output:

demo/final_avatar.mp4


This video contains both audio and animated avatar, fully synchronized.

Motion Model Details

The prototype uses audio-driven heuristics instead of learned models:

Energy → mouth openness & jaw drop

Spectral variation → lip width / rounding

Energy gradient → head nodding

Independent signal → eye blinking

All motion signals are temporally smoothed to prevent jitter and flicker.

This approach provides:

Stable animation

Real-time performance

Deterministic behavior

Easy extensibility

Performance

Runs at 30 FPS on CPU

Real-time capable for short utterances

Low memory footprint

GPU not required (but compatible)

Open-Source Compliance

All components are open-source:

Component	Purpose	License
pyttsx3	Text-to-Speech	MPL
NumPy	Numerical ops	BSD
SciPy	Signal processing	BSD
SoundFile	Audio I/O	BSD
OpenCV	Rendering	Apache 2.0
MoviePy	Video muxing	MIT

❌ No proprietary models
❌ No cloud APIs
❌ No restricted assets

Limitations (Intentional)

This is a research prototype, not a production avatar engine.

Fixed 2D avatar

Heuristic viseme approximation

No emotion classification

No identity customization

These design choices prioritize clarity, reproducibility, and system explainability.

Extensibility

The system is intentionally modular. Possible extensions include:

Neural TTS (VITS, FastSpeech, etc.)

Phoneme-level viseme prediction

3D mesh-based avatars

Diffusion-based face rendering

GPU-accelerated inference

Multi-avatar concurrency



Demo

A short demo video is included in:

demo/final_avatar.mp4
