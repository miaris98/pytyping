import os
import sys
import hashlib
import asyncio
from typing import Optional, List, Dict
from config import config, get_data_dir

AUDIO_CACHE_DIR = os.path.join(get_data_dir(), "cache", "audio")
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

VOICES = [
    {"id": "en-US-ChristopherNeural", "name": "Christopher (US Male, Warm & Clear)"},
    {"id": "en-US-GuyNeural", "name": "Guy (US Male, Professional)"},
    {"id": "en-US-JennyNeural", "name": "Jenny (US Female, Natural)"},
    {"id": "en-US-AriaNeural", "name": "Aria (US Female, Studio)"},
    {"id": "en-GB-RyanNeural", "name": "Ryan (UK Male, Crisp)"},
    {"id": "en-GB-SoniaNeural", "name": "Sonia (UK Female, Polite)"},
    {"id": "sapi", "name": "Windows System Voice (Offline SAPI)"}
]

class TTSService:
    @staticmethod
    def get_cache_path(text: str, voice: str, speed_str: str) -> str:
        key_raw = f"{voice}_{speed_str}_{text}"
        key = hashlib.sha256(key_raw.encode("utf-8")).hexdigest()[:16]
        return os.path.join(AUDIO_CACHE_DIR, f"{key}.mp3")

    @classmethod
    def synthesize_to_file(cls, text: str, voice: Optional[str] = None, speed: float = 1.0) -> Optional[str]:
        """
        Synthesizes text to an MP3 file using edge-tts or Windows SAPI.
        Returns the absolute file path, or None on failure.
        """
        if not text:
            return None

        if voice is None:
            voice = config.get("edge_voice", "en-US-ChristopherNeural")

        # Map speed float (0.75, 1.0, 1.25, 1.5) to edge-tts rate format
        pct = int(round((speed - 1.0) * 100))
        rate_str = f"{'+' if pct >= 0 else ''}{pct}%"

        cache_path = cls.get_cache_path(text, voice, rate_str)
        if os.path.exists(cache_path) and os.path.getsize(cache_path) > 100:
            return cache_path

        # If user explicitly selected SAPI or offline fallback
        if voice == "sapi" or config.get("tts_engine") == "sapi":
            return cls._synthesize_sapi_to_file(text, cache_path)

        # Try edge-tts
        try:
            import edge_tts
            
            async def run_edge():
                communicate = edge_tts.Communicate(text, voice, rate=rate_str)
                await communicate.save(cache_path)

            asyncio.run(run_edge())
            if os.path.exists(cache_path) and os.path.getsize(cache_path) > 100:
                return cache_path
        except Exception as e:
            print(f"edge-tts synthesis failed, falling back to SAPI: {e}")

        # Fallback to SAPI
        return cls._synthesize_sapi_to_file(text, cache_path.replace(".mp3", ".wav"))

    @classmethod
    def _synthesize_sapi_to_file(cls, text: str, output_path: str) -> Optional[str]:
        """Generate audio file via Windows SAPI SpVoice and SpFileStream."""
        try:
            import win32com.client
            voice = win32com.client.Dispatch("SAPI.SpVoice")
            stream = win32com.client.Dispatch("SAPI.SpFileStream")
            
            # File format: 39 is 44kHz 16Bit Stereo
            stream.Format.Type = 39
            # Open mode: 3 is SSFMCreateForWrite
            stream.Open(output_path, 3, False)
            voice.AudioOutputStream = stream
            voice.Speak(text)
            stream.Close()
            return output_path
        except Exception as e:
            print(f"SAPI file synthesis failed: {e}")
            return None

# Global instance
tts_service = TTSService()

