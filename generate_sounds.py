import os
import math
import struct
import wave

ASSETS_SOUNDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sounds")
os.makedirs(ASSETS_SOUNDS_DIR, exist_ok=True)

def generate_click():
    """Generates a subtle, tactile mechanical switch sound (15ms)."""
    sample_rate = 44100
    duration = 0.018  # 18ms
    num_samples = int(sample_rate * duration)
    path = os.path.join(ASSETS_SOUNDS_DIR, "click.wav")
    
    with wave.open(path, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for i in range(num_samples):
            t = i / sample_rate
            # Decaying frequency click
            envelope = math.exp(-t * 220.0)
            freq = 1200.0 - (t / duration) * 600.0
            val = math.sin(2.0 * math.pi * freq * t) * envelope * 0.25
            sample = int(val * 32767.0)
            wav_file.writeframes(struct.pack("<h", sample))

def generate_error():
    """Generates a soft low thump for typos (25ms)."""
    sample_rate = 44100
    duration = 0.035
    num_samples = int(sample_rate * duration)
    path = os.path.join(ASSETS_SOUNDS_DIR, "error.wav")
    
    with wave.open(path, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        
        for i in range(num_samples):
            t = i / sample_rate
            envelope = math.exp(-t * 120.0)
            freq = 180.0
            val = math.sin(2.0 * math.pi * freq * t) * envelope * 0.35
            sample = int(val * 32767.0)
            wav_file.writeframes(struct.pack("<h", sample))

if __name__ == "__main__":
    generate_click()
    generate_error()
    print("Generated sound assets successfully.")

