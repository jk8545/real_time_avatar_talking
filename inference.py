import moviepy as mp
from motion.audio_to_motion import extract_audio_features, audio_to_motion
from renderer.face_renderer import render_face

AUDIO_PATH = "audio/tts.wav"
OUTPUT_PATH = "demo/final_avatar.mp4"
FPS = 30

# 1. Audio → motion
energy, zcr = extract_audio_features(AUDIO_PATH, fps=FPS)
motion = audio_to_motion(energy, zcr)

# 2. Motion → frames
frames = render_face(motion, fps=FPS)

# 3. Frames → video
video_clip = mp.ImageSequenceClip(frames, fps=FPS)

# 4. Load audio
audio_clip = mp.AudioFileClip(AUDIO_PATH)

# 5. Combine audio + video
final_clip = video_clip.with_audio(audio_clip)

# 6. Export single MP4
final_clip.write_videofile(
    OUTPUT_PATH,
    codec="libx264",
    audio_codec="aac",
    fps=FPS
)

print("FINAL VIDEO CREATED:", OUTPUT_PATH)
