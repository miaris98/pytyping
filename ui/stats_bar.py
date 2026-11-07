from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QProgressBar, QFrame
)
from config import config

class StatsBar(QWidget):
    restart_clicked = pyqtSignal()
    prev_clicked = pyqtSignal()
    next_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(12, 10, 12, 10)
        main_layout.setSpacing(8)

        # Top row: Stats Cards + Action Buttons
        top_row = QHBoxLayout()
        top_row.setSpacing(12)

        # WPM Card
        self.wpm_card = self._create_stat_card("WPM", "0.0", "#89b4fa")
        self.wpm_val = self.wpm_card.findChild(QLabel, "val")
        top_row.addWidget(self.wpm_card)

        # Accuracy Card
        self.acc_card = self._create_stat_card("ACCURACY", "100%", "#a6e3a1")
        self.acc_val = self.acc_card.findChild(QLabel, "val")
        top_row.addWidget(self.acc_card)

        # Time Card
        self.time_card = self._create_stat_card("TIME", "00:00", "#f9e2af")
        self.time_val = self.time_card.findChild(QLabel, "val")
        top_row.addWidget(self.time_card)

        # Errors Card
        self.err_card = self._create_stat_card("ERRORS", "0", "#f38ba8")
        self.err_val = self.err_card.findChild(QLabel, "val")
        top_row.addWidget(self.err_card)

        top_row.addStretch()

        # Action Buttons
        self.btn_sound = QPushButton("🔊 Sound FX")
        self.btn_sound.setToolTip("Toggle mechanical keyboard click sound")
        self.btn_sound.clicked.connect(self._toggle_sound)
        self._update_sound_btn_text()
        top_row.addWidget(self.btn_sound)

        self.btn_prev = QPushButton("◀ Prev")
        self.btn_prev.setShortcut("Ctrl+P")
        self.btn_prev.setToolTip("Previous problem (Ctrl+P)")
        self.btn_prev.clicked.connect(self.prev_clicked.emit)
        top_row.addWidget(self.btn_prev)

        self.btn_restart = QPushButton("↺ Restart")
        self.btn_restart.setShortcut("Ctrl+R")
        self.btn_restart.setToolTip("Restart current problem (Ctrl+R)")
        self.btn_restart.clicked.connect(self.restart_clicked.emit)
        top_row.addWidget(self.btn_restart)

        self.btn_next = QPushButton("Next ▶")
        self.btn_next.setObjectName("primary_btn")
        self.btn_next.setShortcut("Ctrl+N")
        self.btn_next.setToolTip("Next problem (Ctrl+N)")
        self.btn_next.clicked.connect(self.next_clicked.emit)
        top_row.addWidget(self.btn_next)

        main_layout.addLayout(top_row)

        # Bottom row: Progress bar + detail label
        prog_row = QHBoxLayout()
        prog_row.setSpacing(10)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        prog_row.addWidget(self.progress_bar, 1)

        self.progress_lbl = QLabel("0%")
        self.progress_lbl.setStyleSheet("color: #a6adc8; font-size: 11px; font-weight: bold;")
        prog_row.addWidget(self.progress_lbl)

        main_layout.addLayout(prog_row)

    def _create_stat_card(self, title: str, val: str, color_hex: str) -> QFrame:
        card = QFrame()
        card.setObjectName("stats_card")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(12, 6, 12, 6)
        layout.setSpacing(2)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: #6c7086; font-size: 10px; font-weight: bold; letter-spacing: 1px;")
        layout.addWidget(lbl_title)

        lbl_val = QLabel(val)
        lbl_val.setObjectName("val")
        lbl_val.setStyleSheet(f"color: {color_hex}; font-size: 18px; font-weight: bold; font-family: 'Consolas', monospace;")
        layout.addWidget(lbl_val)

        return card

    def update_stats(self, wpm: float, acc: float, elapsed_sec: float, progress: float, errors: int):
        self.wpm_val.setText(f"{wpm:.1f}")
        self.acc_val.setText(f"{acc:.1f}%")

        mins = int(elapsed_sec // 60)
        secs = int(elapsed_sec % 60)
        self.time_val.setText(f"{mins:02d}:{secs:02d}")

        self.err_val.setText(str(errors))
        self.progress_bar.setValue(int(progress))
        self.progress_lbl.setText(f"{progress:.1f}%")

    def _toggle_sound(self):
        cur = config.get("click_sounds", True)
        config.set("click_sounds", not cur)
        self._update_sound_btn_text()

    def _update_sound_btn_text(self):
        enabled = config.get("click_sounds", True)
        if enabled:
            self.btn_sound.setText("🔊 Sound FX: ON")
            self.btn_sound.setStyleSheet("color: #a6e3a1;")
        else:
            self.btn_sound.setText("🔇 Sound FX: OFF")
            self.btn_sound.setStyleSheet("color: #6c7086;")

