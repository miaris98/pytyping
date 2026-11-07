from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QComboBox, QSlider, QCheckBox, QTabWidget
)
from core.llm_service import llm_service
from core.audio_player import audio_player
from core.tts_service import VOICES
from config import config


class LLMWorker(QThread):
    finished_signal = pyqtSignal(dict)
    error_signal = pyqtSignal(str)

    def __init__(self, code: str, problem_name: str, force_refresh: bool = False):
        super().__init__()
        self.code = code
        self.problem_name = problem_name
        self.force_refresh = force_refresh

    def run(self):
        try:
            data = llm_service.get_explanation(self.code, self.problem_name, self.force_refresh)
            self.finished_signal.emit(data)
        except Exception as e:
            self.error_signal.emit(str(e))


class ExplanationPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_code = ""
        self.current_name = ""
        self.current_data = {}
        self.active_track = "walkthrough"  # 'walkthrough' or 'bigo'
        self.llm_worker = None

        self._init_ui()
        self._connect_audio_player()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Header with Title and Regenerate button
        header_row = QHBoxLayout()
        self.title_lbl = QLabel("Algorithm Mentor")
        self.title_lbl.setStyleSheet("font-size: 16px; font-weight: bold; color: #89b4fa;")
        header_row.addWidget(self.title_lbl, 1)

        self.btn_refresh = QPushButton("⚡ Refresh AI")
        self.btn_refresh.setToolTip("Regenerate explanations using selected LLM")
        self.btn_refresh.clicked.connect(self._on_regenerate_clicked)
        header_row.addWidget(self.btn_refresh)

        main_layout.addLayout(header_row)

        # Dual Audio Player Card (Supports both Walkthrough Audio & Big O Audio)
        self.audio_card = self._create_audio_controls()
        main_layout.addWidget(self.audio_card)

        # Two Separate Tabs:
        # Tab 1: Code Walkthrough & Why It's Optimal
        # Tab 2: Big O Runtime & Memory Complexity
        self.tabs = QTabWidget()

        # --- TAB 1: Walkthrough, Understanding & Efficiency ---
        tab_walkthrough = QWidget()
        wt_outer = QVBoxLayout(tab_walkthrough)
        wt_outer.setContentsMargins(4, 8, 4, 4)

        wt_scroll = QScrollArea()
        wt_scroll.setWidgetResizable(True)
        wt_scroll.setFrameShape(QFrame.NoFrame)
        wt_scroll.setStyleSheet("background: transparent;")

        wt_content = QWidget()
        wt_layout = QVBoxLayout(wt_content)
        wt_layout.setContentsMargins(0, 0, 6, 0)
        wt_layout.setSpacing(10)

        # Core Understanding Card
        self.understanding_card = self._create_card(
            "🧠 CORE UNDERSTANDING & INTUITION",
            "Select a problem to learn the core mental model.",
            "#89b4fa"
        )
        self.understanding_text = self.understanding_card.findChild(QLabel, "content")
        wt_layout.addWidget(self.understanding_card)

        # Why Most Efficient Card
        self.efficiency_card = self._create_card(
            "🚀 WHY THIS IS THE MOST EFFICIENT SOLUTION",
            "Comparison against brute-force and why this approach is optimal.",
            "#a6e3a1"
        )
        self.efficiency_text = self.efficiency_card.findChild(QLabel, "content")
        wt_layout.addWidget(self.efficiency_card)

        # Step-by-Step Code Walkthrough Card
        self.walkthrough_card = self._create_card(
            "🔍 STEP-BY-STEP CODE WALKTHROUGH",
            "Line-by-line explanation of the code.",
            "#f9e2af"
        )
        self.walkthrough_text = self.walkthrough_card.findChild(QLabel, "content")
        wt_layout.addWidget(self.walkthrough_card)

        wt_layout.addStretch()
        wt_scroll.setWidget(wt_content)
        wt_outer.addWidget(wt_scroll)

        self.tabs.addTab(tab_walkthrough, "💡 Walkthrough & Intuition")

        # --- TAB 2: Separate Big O Runtime & Memory Analysis ---
        tab_bigo = QWidget()
        bigo_outer = QVBoxLayout(tab_bigo)
        bigo_outer.setContentsMargins(4, 8, 4, 4)

        bigo_scroll = QScrollArea()
        bigo_scroll.setWidgetResizable(True)
        bigo_scroll.setFrameShape(QFrame.NoFrame)
        bigo_scroll.setStyleSheet("background: transparent;")

        bigo_content = QWidget()
        bigo_layout = QVBoxLayout(bigo_content)
        bigo_layout.setContentsMargins(0, 0, 6, 0)
        bigo_layout.setSpacing(10)

        # Big O Badges Row
        badges_row = QHBoxLayout()
        self.time_badge = QLabel("⏱ Time: O(?)")
        self.time_badge.setObjectName("time_badge")
        badges_row.addWidget(self.time_badge)

        self.space_badge = QLabel("💾 Space: O(?)")
        self.space_badge.setObjectName("space_badge")
        badges_row.addWidget(self.space_badge)
        badges_row.addStretch()
        bigo_layout.addLayout(badges_row)

        # Time Complexity Card
        self.time_card = self._create_card(
            "⏱ RUNTIME COMPLEXITY (TIME BIG O)",
            "Runtime analysis will appear here.",
            "#89b4fa"
        )
        self.time_text = self.time_card.findChild(QLabel, "content")
        bigo_layout.addWidget(self.time_card)

        # Space Complexity Card
        self.space_card = self._create_card(
            "💾 MEMORY COMPLEXITY (SPACE BIG O)",
            "Memory analysis will appear here.",
            "#cba6f7"
        )
        self.space_text = self.space_card.findChild(QLabel, "content")
        bigo_layout.addWidget(self.space_card)

        # Big O Deep Dive Card
        self.bigo_dive_card = self._create_card(
            "📊 COMPLEXITY DEEP DIVE & TRADE-OFFS",
            "Best/Worst case bounds and memory trade-offs.",
            "#94e2d5"
        )
        self.bigo_dive_text = self.bigo_dive_card.findChild(QLabel, "content")
        bigo_layout.addWidget(self.bigo_dive_card)

        bigo_layout.addStretch()
        bigo_scroll.setWidget(bigo_content)
        bigo_outer.addWidget(bigo_scroll)

        self.tabs.addTab(tab_bigo, "📊 Big O Complexity")

        main_layout.addWidget(self.tabs, 1)

        # Provider tag at bottom
        self.provider_lbl = QLabel("")
        self.provider_lbl.setStyleSheet("color: #585b70; font-size: 11px; font-style: italic;")
        main_layout.addWidget(self.provider_lbl)

    def _create_card(self, title: str, initial_text: str, accent_color: str = "#a6adc8") -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        lbl_t = QLabel(title)
        lbl_t.setStyleSheet(f"color: {accent_color}; font-size: 11px; font-weight: bold; letter-spacing: 0.5px;")
        layout.addWidget(lbl_t)

        lbl_c = QLabel(initial_text)
        lbl_c.setObjectName("content")
        lbl_c.setWordWrap(True)
        lbl_c.setStyleSheet("color: #cdd6f4; font-size: 13px; line-height: 1.45;")
        layout.addWidget(lbl_c)

        return card

    def _create_audio_controls(self) -> QFrame:
        card = QFrame()
        card.setObjectName("card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(8)

        # Header line: title + auto play checkbox
        top_h = QHBoxLayout()
        audio_title = QLabel("🎧 Dual Audio Playbacks (Listen While Typing)")
        audio_title.setStyleSheet("color: #89b4fa; font-weight: bold; font-size: 13px;")
        top_h.addWidget(audio_title)

        top_h.addStretch()

        self.cb_autoplay = QCheckBox("Auto-play")
        self.cb_autoplay.setToolTip("Automatically play Walkthrough audio when a problem opens")
        self.cb_autoplay.setChecked(config.get("auto_play_audio", False))
        self.cb_autoplay.toggled.connect(lambda v: config.set("auto_play_audio", v))
        top_h.addWidget(self.cb_autoplay)

        layout.addLayout(top_h)

        # Two Dedicated Audio Playback Buttons Row
        track_row = QHBoxLayout()
        track_row.setSpacing(6)

        self.btn_play_walkthrough = QPushButton("▶ 1. Walkthrough Audio")
        self.btn_play_walkthrough.setObjectName("primary_btn")
        self.btn_play_walkthrough.setToolTip("Listen to the Code Walkthrough, Intuition & Why It's Optimal")
        self.btn_play_walkthrough.clicked.connect(self._on_play_walkthrough_clicked)
        track_row.addWidget(self.btn_play_walkthrough, 1)

        self.btn_play_bigo = QPushButton("▶ 2. Big O Audio")
        self.btn_play_bigo.setObjectName("success_btn")
        self.btn_play_bigo.setToolTip("Listen to the separate Big O Runtime & Memory Complexity explanation")
        self.btn_play_bigo.clicked.connect(self._on_play_bigo_clicked)
        track_row.addWidget(self.btn_play_bigo, 1)

        layout.addLayout(track_row)

        # Status & slider row
        self.audio_status = QLabel("Ready — Choose Track 1 (Walkthrough) or Track 2 (Big O)")
        self.audio_status.setStyleSheet("color: #a6adc8; font-size: 11px;")
        layout.addWidget(self.audio_status)

        self.audio_slider = QSlider(Qt.Horizontal)
        self.audio_slider.setRange(0, 1000)
        self.audio_slider.sliderMoved.connect(self._on_slider_seek)
        layout.addWidget(self.audio_slider)

        # Transport & Voice/Speed controls row
        btn_row = QHBoxLayout()
        btn_row.setSpacing(6)

        self.btn_pause_resume = QPushButton("⏯ Pause")
        self.btn_pause_resume.clicked.connect(self._on_pause_resume_clicked)
        btn_row.addWidget(self.btn_pause_resume)

        self.btn_stop = QPushButton("⏹ Stop")
        self.btn_stop.clicked.connect(self._on_stop_clicked)
        btn_row.addWidget(self.btn_stop)

        # Voice Selector
        self.voice_combo = QComboBox()
        self.voice_combo.setToolTip("Select AI Voice")
        current_voice = config.get("edge_voice", "en-US-ChristopherNeural")
        for idx, v in enumerate(VOICES):
            self.voice_combo.addItem(v["name"], v["id"])
            if v["id"] == current_voice:
                self.voice_combo.setCurrentIndex(idx)
        self.voice_combo.currentIndexChanged.connect(self._on_voice_changed)
        btn_row.addWidget(self.voice_combo, 1)

        # Speed Selector
        self.speed_combo = QComboBox()
        self.speed_combo.setToolTip("Playback Speed")
        speeds = [("0.75x", 0.75), ("1.0x", 1.0), ("1.25x", 1.25), ("1.5x", 1.5)]
        current_speed = float(config.get("tts_speed", 1.0))
        for idx, (label, val) in enumerate(speeds):
            self.speed_combo.addItem(label, val)
            if abs(val - current_speed) < 0.05:
                self.speed_combo.setCurrentIndex(idx)
        self.speed_combo.currentIndexChanged.connect(self._on_speed_changed)
        btn_row.addWidget(self.speed_combo)

        layout.addLayout(btn_row)
        return card

    def _connect_audio_player(self):
        audio_player.status_changed.connect(self._on_audio_status_changed)
        audio_player.position_changed.connect(self._on_audio_position_changed)
        audio_player.playback_finished.connect(self._on_audio_finished)

    def load_problem(self, code: str, problem_name: str):
        self.current_code = code
        self.current_name = problem_name
        self.title_lbl.setText(problem_name.replace(".py", "").replace("_", " "))

        audio_player.stop()
        self.audio_status.setText("Analyzing walkthrough & Big O complexity...")

        if self.llm_worker and self.llm_worker.isRunning():
            self.llm_worker.terminate()
            self.llm_worker.wait()

        self.llm_worker = LLMWorker(code, problem_name, force_refresh=False)
        self.llm_worker.finished_signal.connect(self._on_explanation_loaded)
        self.llm_worker.error_signal.connect(self._on_explanation_error)
        self.llm_worker.start()

    def _on_explanation_loaded(self, data: dict):
        self.current_data = data

        # Populate Tab 1: Walkthrough, Core Understanding & Why Most Efficient
        self.understanding_text.setText(
            data.get("core_understanding", data.get("summary", ""))
        )
        self.efficiency_text.setText(
            data.get("why_most_efficient", "Optimal time and space efficiency.")
        )

        wt_list = data.get("code_walkthrough", data.get("walkthrough", []))
        if isinstance(wt_list, list):
            formatted_wt = "<br><br>".join(
                [f"<b>Step {i+1}:</b> {step}" for i, step in enumerate(wt_list)]
            )
        else:
            formatted_wt = str(wt_list)
        self.walkthrough_text.setText(formatted_wt)

        # Populate Tab 2: Separate Big O Runtime & Memory Complexity
        t_comp = data.get("time_complexity", "O(?)")
        s_comp = data.get("space_complexity", "O(?)")
        self.time_badge.setText(f"⏱ Time: {t_comp}")
        self.space_badge.setText(f"💾 Space: {s_comp}")

        self.time_text.setText(
            f"<b>{t_comp}</b> — {data.get('time_explanation', '')}"
        )
        self.space_text.setText(
            f"<b>{s_comp}</b> — {data.get('space_explanation', '')}"
        )

        dive_list = data.get("bigo_deep_dive", [])
        if isinstance(dive_list, list) and dive_list:
            formatted_dive = "<br><br>".join([f"• {item}" for item in dive_list])
        else:
            formatted_dive = (
                f"• <b>Runtime:</b> {t_comp}<br><br>"
                f"• <b>Auxiliary Space:</b> {s_comp}"
            )
        self.bigo_dive_text.setText(formatted_dive)

        self.provider_lbl.setText(
            f"Source: {data.get('provider', 'Curated Algorithm Mentor')}"
        )
        self.audio_status.setText(
            "Audio Ready — Click Track 1 (Walkthrough) or Track 2 (Big O)"
        )

        if self.cb_autoplay.isChecked():
            self._on_play_walkthrough_clicked()

    def _on_explanation_error(self, err: str):
        self.audio_status.setText(f"Analysis note: {err}")

    def _on_regenerate_clicked(self):
        if not self.current_code:
            return
        self.audio_status.setText("Regenerating both AI explanations...")
        self.llm_worker = LLMWorker(self.current_code, self.current_name, force_refresh=True)
        self.llm_worker.finished_signal.connect(self._on_explanation_loaded)
        self.llm_worker.error_signal.connect(self._on_explanation_error)
        self.llm_worker.start()

    def _on_play_walkthrough_clicked(self):
        self.active_track = "walkthrough"
        self.tabs.setCurrentIndex(0)
        text = self.current_data.get("walkthrough_audio_text", "")
        if not text:
            steps = self.current_data.get("code_walkthrough", [])
            steps_str = " ".join(steps) if isinstance(steps, list) else str(steps)
            text = (
                f"Code walkthrough for {self.current_name}. "
                f"{self.current_data.get('core_understanding', '')} "
                f"{self.current_data.get('why_most_efficient', '')} "
                f"{steps_str}"
            )
        voice_id = self.voice_combo.currentData()
        speed_val = self.speed_combo.currentData()
        audio_player.play_text(text, voice_id, speed_val)
        self.btn_pause_resume.setText("⏸ Pause")

    def _on_play_bigo_clicked(self):
        self.active_track = "bigo"
        self.tabs.setCurrentIndex(1)
        text = self.current_data.get("bigo_audio_text", "")
        if not text:
            text = (
                f"Big O complexity analysis for {self.current_name}. "
                f"Time complexity is {self.current_data.get('time_complexity', '')}. "
                f"{self.current_data.get('time_explanation', '')} "
                f"Space complexity is {self.current_data.get('space_complexity', '')}. "
                f"{self.current_data.get('space_explanation', '')}"
            )
        voice_id = self.voice_combo.currentData()
        speed_val = self.speed_combo.currentData()
        audio_player.play_text(text, voice_id, speed_val)
        self.btn_pause_resume.setText("⏸ Pause")

    def _on_pause_resume_clicked(self):
        if audio_player.is_playing():
            audio_player.pause()
            self.btn_pause_resume.setText("▶ Resume")
        elif "Paused" in self.audio_status.text():
            audio_player.resume()
            self.btn_pause_resume.setText("⏸ Pause")
        else:
            if self.active_track == "bigo":
                self._on_play_bigo_clicked()
            else:
                self._on_play_walkthrough_clicked()

    def _on_stop_clicked(self):
        audio_player.stop()
        self.btn_pause_resume.setText("⏯ Pause")
        self.audio_slider.setValue(0)

    def _on_voice_changed(self, idx):
        voice_id = self.voice_combo.itemData(idx)
        config.set("edge_voice", voice_id)

    def _on_speed_changed(self, idx):
        speed_val = self.speed_combo.itemData(idx)
        config.set("tts_speed", speed_val)

    def _on_slider_seek(self, value):
        dur = audio_player.player.duration()
        if dur > 0:
            pos = int((value / 1000.0) * dur)
            audio_player.seek(pos)

    def _on_audio_status_changed(self, status: str):
        track_label = "Track 1 (Walkthrough)" if self.active_track == "walkthrough" else "Track 2 (Big O)"
        if "Playing" in status:
            self.audio_status.setText(f"🔊 {track_label}: Playing")
            self.btn_pause_resume.setText("⏸ Pause")
        elif "Paused" in status:
            self.audio_status.setText(f"⏸ {track_label}: Paused")
            self.btn_pause_resume.setText("▶ Resume")
        elif "Synthesizing" in status:
            self.audio_status.setText(f"⏳ {track_label}: {status}")
        else:
            self.audio_status.setText(status)

    def _on_audio_position_changed(self, pos: int, dur: int):
        if dur > 0:
            ratio = min(1000, max(0, int((pos / dur) * 1000)))
            self.audio_slider.blockSignals(True)
            self.audio_slider.setValue(ratio)
            self.audio_slider.blockSignals(False)

            cur_sec = int(pos // 1000)
            tot_sec = int(dur // 1000)
            track_label = "Walkthrough Audio" if self.active_track == "walkthrough" else "Big O Audio"
            self.audio_status.setText(
                f"🔊 {track_label} ({cur_sec//60:02d}:{cur_sec%60:02d} / {tot_sec//60:02d}:{tot_sec%60:02d})"
            )

    def _on_audio_finished(self):
        self.btn_pause_resume.setText("⏯ Pause")
        self.audio_slider.setValue(0)
        track_label = "Track 1 (Walkthrough)" if self.active_track == "walkthrough" else "Track 2 (Big O)"
        self.audio_status.setText(f"✓ {track_label} finished")
