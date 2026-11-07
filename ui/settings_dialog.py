from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QCheckBox, QTabWidget, QWidget, QFileDialog, QSpinBox, QMessageBox
)
from config import config, DEFAULT_SOLUTIONS_DIR
from core.tts_service import VOICES
from core.audio_player import audio_player

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings - LeetType")
        self.resize(550, 480)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        tabs = QTabWidget()

        # TAB 1: AI Provider & Free API
        tab_ai = QWidget()
        layout_ai = QVBoxLayout(tab_ai)
        layout_ai.setSpacing(12)

        lbl_prov = QLabel("AI Explanation Provider:")
        lbl_prov.setStyleSheet("font-weight: bold; color: #89b4fa;")
        layout_ai.addWidget(lbl_prov)

        self.provider_combo = QComboBox()
        self.provider_combo.addItem("Built-in Offline Analyzer (No API key needed)", "offline")
        self.provider_combo.addItem("Groq API (Free & ultra-fast Llama-3.3 70B)", "groq")
        self.provider_combo.addItem("Google Gemini API (Free tier Gemini 2.0 Flash)", "gemini")
        self.provider_combo.addItem("OpenRouter API (Free tier models)", "openrouter")
        self.provider_combo.addItem("Ollama (Local free LLM)", "ollama")
        
        cur_prov = config.get("llm_provider", "offline")
        for i in range(self.provider_combo.count()):
            if self.provider_combo.itemData(i) == cur_prov:
                self.provider_combo.setCurrentIndex(i)
                break
        layout_ai.addWidget(self.provider_combo)

        # Groq Settings
        layout_ai.addWidget(QLabel("Groq API Key (Free at console.groq.com):"))
        self.groq_key_input = QLineEdit(config.get("groq_api_key", ""))
        self.groq_key_input.setEchoMode(QLineEdit.Password)
        self.groq_key_input.setPlaceholderText("gsk_...")
        layout_ai.addWidget(self.groq_key_input)

        # Gemini Settings
        layout_ai.addWidget(QLabel("Google Gemini API Key (Free at aistudio.google.com):"))
        self.gemini_key_input = QLineEdit(config.get("gemini_api_key", ""))
        self.gemini_key_input.setEchoMode(QLineEdit.Password)
        self.gemini_key_input.setPlaceholderText("AIzaSy...")
        layout_ai.addWidget(self.gemini_key_input)

        # OpenRouter Settings
        layout_ai.addWidget(QLabel("OpenRouter API Key (Free at openrouter.ai):"))
        self.openrouter_key_input = QLineEdit(config.get("openrouter_api_key", ""))
        self.openrouter_key_input.setEchoMode(QLineEdit.Password)
        self.openrouter_key_input.setPlaceholderText("sk-or-...")
        layout_ai.addWidget(self.openrouter_key_input)

        # Ollama Settings
        layout_ai.addWidget(QLabel("Ollama Base URL:"))
        self.ollama_url_input = QLineEdit(config.get("ollama_url", "http://localhost:11434"))
        layout_ai.addWidget(self.ollama_url_input)

        layout_ai.addStretch()
        tabs.addTab(tab_ai, "🤖 AI & LLM")

        # TAB 2: Audio & TTS
        tab_audio = QWidget()
        layout_audio = QVBoxLayout(tab_audio)
        layout_audio.setSpacing(12)

        layout_audio.addWidget(QLabel("Default AI Voice:"))
        self.voice_combo = QComboBox()
        cur_voice = config.get("edge_voice", "en-US-ChristopherNeural")
        for idx, v in enumerate(VOICES):
            self.voice_combo.addItem(v["name"], v["id"])
            if v["id"] == cur_voice:
                self.voice_combo.setCurrentIndex(idx)
        layout_audio.addWidget(self.voice_combo)

        layout_audio.addWidget(QLabel("Playback Speed:"))
        self.speed_combo = QComboBox()
        speeds = [("0.75x Slow", 0.75), ("1.0x Normal", 1.0), ("1.25x Fast", 1.25), ("1.5x Very Fast", 1.5)]
        cur_spd = float(config.get("tts_speed", 1.0))
        for idx, (label, val) in enumerate(speeds):
            self.speed_combo.addItem(label, val)
            if abs(val - cur_spd) < 0.05:
                self.speed_combo.setCurrentIndex(idx)
        layout_audio.addWidget(self.speed_combo)

        self.cb_autoplay = QCheckBox("Auto-play explanation audio when loading problem")
        self.cb_autoplay.setChecked(config.get("auto_play_audio", False))
        layout_audio.addWidget(self.cb_autoplay)

        btn_test_audio = QPushButton("🔊 Test Voice Sample")
        btn_test_audio.clicked.connect(self._on_test_voice)
        layout_audio.addWidget(btn_test_audio)

        layout_audio.addStretch()
        tabs.addTab(tab_audio, "🎧 Speech & Audio")

        # TAB 3: Typing & Display
        tab_typing = QWidget()
        layout_typing = QVBoxLayout(tab_typing)
        layout_typing.setSpacing(12)

        layout_typing.addWidget(QLabel("Typing Code Font Size:"))
        self.spin_font_size = QSpinBox()
        self.spin_font_size.setRange(10, 26)
        self.spin_font_size.setValue(int(config.get("font_size", 14)))
        layout_typing.addWidget(self.spin_font_size)

        self.cb_sound = QCheckBox("Enable tactile mechanical keyboard typing sounds")
        self.cb_sound.setChecked(config.get("click_sounds", True))
        layout_typing.addWidget(self.cb_sound)

        layout_typing.addStretch()
        tabs.addTab(tab_typing, "⌨ Typing Arena")

        # TAB 4: Solutions Folder
        tab_folder = QWidget()
        layout_folder = QVBoxLayout(tab_folder)
        layout_folder.setSpacing(12)

        layout_folder.addWidget(QLabel("Solutions Folder Path:"))
        folder_row = QHBoxLayout()
        self.folder_input = QLineEdit(config.get("solutions_dir", DEFAULT_SOLUTIONS_DIR))
        folder_row.addWidget(self.folder_input, 1)

        btn_browse = QPushButton("Browse...")
        btn_browse.clicked.connect(self._on_browse_folder)
        folder_row.addWidget(btn_browse)
        layout_folder.addLayout(folder_row)

        btn_reset_folder = QPushButton("Reset to Default LeetCode Solutions")
        btn_reset_folder.clicked.connect(lambda: self.folder_input.setText(DEFAULT_SOLUTIONS_DIR))
        layout_folder.addWidget(btn_reset_folder)

        info_lbl = QLabel("The app reads all subfolders and .py files in this folder. You can add your own subfolders (e.g. Dynamic Programming, Graphs) anytime!")
        info_lbl.setWordWrap(True)
        info_lbl.setStyleSheet("color: #a6adc8; font-size: 11px;")
        layout_folder.addWidget(info_lbl)

        layout_folder.addStretch()
        tabs.addTab(tab_folder, "📁 Solutions Folder")

        main_layout.addWidget(tabs)

        # Bottom Buttons
        bottom_row = QHBoxLayout()
        bottom_row.addStretch()

        btn_cancel = QPushButton("Cancel")
        btn_cancel.clicked.connect(self.reject)
        bottom_row.addWidget(btn_cancel)

        btn_save = QPushButton("Save Settings")
        btn_save.setObjectName("primary_btn")
        btn_save.clicked.connect(self._on_save)
        bottom_row.addWidget(btn_save)

        main_layout.addLayout(bottom_row)

    def _on_test_voice(self):
        voice_id = self.voice_combo.currentData()
        speed_val = self.speed_combo.currentData()
        audio_player.play_text("Welcome to LeetType. This audio explanation will help you memorize algorithms while typing.", voice_id, speed_val)

    def _on_browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Solutions Directory", self.folder_input.text())
        if folder:
            self.folder_input.setText(folder)

    def _on_save(self):
        config.set("llm_provider", self.provider_combo.currentData())
        config.set("groq_api_key", self.groq_key_input.text().strip())
        config.set("gemini_api_key", self.gemini_key_input.text().strip())
        config.set("openrouter_api_key", self.openrouter_key_input.text().strip())
        config.set("ollama_url", self.ollama_url_input.text().strip())
        
        config.set("edge_voice", self.voice_combo.currentData())
        config.set("tts_speed", self.speed_combo.currentData())
        config.set("auto_play_audio", self.cb_autoplay.isChecked())
        
        config.set("font_size", self.spin_font_size.value())
        config.set("click_sounds", self.cb_sound.isChecked())
        config.set("solutions_dir", self.folder_input.text().strip())

        self.accept()

