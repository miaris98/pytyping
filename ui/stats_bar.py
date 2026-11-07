from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QProgressBar, QFrame, QSizePolicy
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
        main_layout.setContentsMargins(8, 6, 8, 6)
        main_layout.setSpacing(6)

        # Row 1: Four Stat Cards (Distribute evenly across available width)
        cards_row = QHBoxLayout()
        cards_row.setSpacing(8)

        # WPM Card
        self.wpm_card = self._create_stat_card("WPM", "0.0", "#89b4fa")
        self.wpm_val = self.wpm_card.findChild(QLabel, "val")
        cards_row.addWidget(self.wpm_card, 1)

        # Accuracy Card
        self.acc_card = self._create_stat_card("ACCURACY", "100%", "#a6e3a1")
        self.acc_val = self.acc_card.findChild(QLabel, "val")
        cards_row.addWidget(self.acc_card, 1)

        # Time Card
        self.time_card = self._create_stat_card("TIME", "00:00", "#f9e2af")
        self.time_val = self.time_card.findChild(QLabel, "val")
        cards_row.addWidget(self.time_card, 1)

        # Errors Card
        self.err_card = self._create_stat_card("ERRORS", "0", "#f38ba8")
        self.err_val = self.err_card.findChild(QLabel, "val")
        cards_row.addWidget(self.err_card, 1)

        main_layout.addLayout(cards_row)

        # Row 2: Progress bar + Action Controls (Wraps and scales seamlessly on side monitors)
        ctrl_row = QHBoxLayout()
        ctrl_row.setSpacing(8)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        ctrl_row.addWidget(self.progress_bar, 1)

        self.progress_lbl = QLabel("0%")
        self.progress_lbl.setStyleSheet("color: #a6adc8; font-size: 11px; font-weight: bold;")
        self.progress_lbl.setFixedWidth(38)
        ctrl_row.addWidget(self.progress_lbl)

        # Buttons
        self.btn_sound = QPushButton("🔊 Clicks")
        self.btn_sound.setToolTip("Toggle mechanical keyboard click sound")
        self.btn_sound.clicked.connect(self._toggle_sound)
        self._update_sound_btn_text()
        ctrl_row.addWidget(self.btn_sound)

        self.btn_prev = QPushButton("◀ Prev")
        self.btn_prev.setShortcut("Ctrl+P")
        self.btn_prev.setToolTip("Previous problem (Ctrl+P)")
        self.btn_prev.clicked.connect(self.prev_clicked.emit)
        ctrl_row.addWidget(self.btn_prev)

        self.btn_restart = QPushButton("↺ Restart")
        self.btn_restart.setShortcut("Ctrl+R")
        self.btn_restart.setToolTip("Restart current problem (Ctrl+R)")
        self.btn_restart.clicked.connect(self.restart_clicked.emit)
        ctrl_row.addWidget(self.btn_restart)

        self.btn_next = QPushButton("Next ▶")
        self.btn_next.setObjectName("primary_btn")
        self.btn_next.setShortcut("Ctrl+N")
        self.btn_next.setToolTip("Next problem (Ctrl+N)")
        self.btn_next.clicked.connect(self.next_clicked.emit)
        ctrl_row.addWidget(self.btn_next)

        main_layout.addLayout(ctrl_row)

    def _create_stat_card(self, title: str, val: str, color_hex: str) -> QFrame:
        card = QFrame()
        card.setObjectName("stats_card")
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(2)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: #6c7086; font-size: 9px; font-weight: bold; letter-spacing: 0.5px;")
        lbl_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl_title)

        lbl_val = QLabel(val)
        lbl_val.setObjectName("val")
        lbl_val.setStyleSheet(f"color: {color_hex}; font-size: 16px; font-weight: bold; font-family: 'Consolas', monospace;")
        lbl_val.setAlignment(Qt.AlignCenter)
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
            self.btn_sound.setText("🔊 Clicks: ON")
            self.btn_sound.setStyleSheet("color: #a6e3a1;")
        else:
            self.btn_sound.setText("🔇 Clicks: OFF")
            self.btn_sound.setStyleSheet("color: #6c7086;")
