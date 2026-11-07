import json
import os
import sys
import shutil

def get_app_dir():
    """Get the base application directory whether running as script or frozen exe."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        p = os.path.join(sys._MEIPASS, relative_path)
        if os.path.exists(p):
            return p
    return os.path.join(get_app_dir(), relative_path)

def get_data_dir():
    """Get user data directory for persistent settings and cache."""
    appdata = os.environ.get('APPDATA')
    if appdata:
        path = os.path.join(appdata, "LeetType")
    else:
        path = os.path.join(get_app_dir(), ".leetype_data")
    os.makedirs(path, exist_ok=True)
    return path

CONFIG_FILE = os.path.join(get_data_dir(), "settings.json")

def ensure_default_problems():
    """Ensure leetcode_problems exists in app directory for easy user access."""
    target_dir = os.path.join(get_app_dir(), "leetcode_problems")
    if not os.path.exists(target_dir):
        bundled_dir = get_resource_path("leetcode_problems")
        if os.path.exists(bundled_dir) and os.path.abspath(bundled_dir) != os.path.abspath(target_dir):
            try:
                shutil.copytree(bundled_dir, target_dir)
            except Exception as e:
                print(f"Could not copy bundled problems: {e}")
                return bundled_dir
    return target_dir

DEFAULT_SOLUTIONS_DIR = ensure_default_problems()

DEFAULT_CONFIG = {
    "solutions_dir": DEFAULT_SOLUTIONS_DIR,
    "llm_provider": "offline",  # 'offline', 'groq', 'gemini', 'openrouter', 'ollama'
    "groq_api_key": "",
    "groq_model": "llama-3.3-70b-versatile",
    "gemini_api_key": "",
    "gemini_model": "gemini-2.0-flash",
    "openrouter_api_key": "",
    "openrouter_model": "google/gemini-2.0-flash-lite:free",
    "ollama_url": "http://localhost:11434",
    "ollama_model": "llama3",
    "tts_engine": "edge",  # 'edge' or 'sapi'
    "edge_voice": "en-US-ChristopherNeural",
    "tts_speed": 1.0,
    "auto_play_audio": False,
    "click_sounds": True,
    "font_size": 14,
}

class Config:
    def __init__(self):
        self._data = dict(DEFAULT_CONFIG)
        self.load()

    def load(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                    self._data.update(saved)
            except Exception as e:
                print(f"Error loading config: {e}")
        
        # Verify solutions directory exists; if not, point to default
        if not os.path.exists(self._data.get("solutions_dir", "")):
            self._data["solutions_dir"] = ensure_default_problems()

    def save(self):
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key, default=None):
        return self._data.get(key, default if default is not None else DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self._data[key] = value
        self.save()

# Global config instance
config = Config()
