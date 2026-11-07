import os
import winsound
from config import config, get_resource_path

class SoundFX:
    @staticmethod
    def play_click():
        if not config.get("click_sounds", True):
            return
        try:
            click_path = get_resource_path(os.path.join("assets", "sounds", "click.wav"))
            if os.path.exists(click_path):
                winsound.PlaySound(click_path, winsound.SND_ASYNC | winsound.SND_FILENAME)
        except Exception:
            pass

    @staticmethod
    def play_error():
        if not config.get("click_sounds", True):
            return
        try:
            error_path = get_resource_path(os.path.join("assets", "sounds", "error.wav"))
            if os.path.exists(error_path):
                winsound.PlaySound(error_path, winsound.SND_ASYNC | winsound.SND_FILENAME)
        except Exception:
            pass
