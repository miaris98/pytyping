from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QWidget
)

class CompletionDialog(QDialog):
    restart_requested = pyqtSignal()
    next_requested = pyqtSignal()

    def __init__(self, stats: dict, problem_name: str, parent=None):
        super().__init__(parent)
        self.stats = stats
        self.problem_name = problem_name.replace(".py", "").replace("_", " ")
        self.setWindowTitle("Problem Complete! 🎉")
        self.setFixedSize(420, 460)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        # Header
        lbl_head = QLabel("🎉 Practice Complete!")
        lbl_head.setAlignment(Qt.AlignCenter)
        lbl_head.setStyleSheet("font-size: 20px; font-weight: bold; color: #a6e3a1;")
        layout.addWidget(lbl_head)

        lbl_prob = QLabel(self.problem_name)
        lbl_prob.setAlignment(Qt.AlignCenter)
        lbl_prob.setStyleSheet("font-size: 14px; color: #89b4fa; font-weight: 600;")
        layout.addWidget(lbl_prob)

        # Rank badge
        wpm = self.stats.get("wpm", 0.0)
        rank_text, rank_color = self._get_rank(wpm)
        
        lbl_rank = QLabel(rank_text)
        lbl_rank.setAlignment(Qt.AlignCenter)
        lbl_rank.setStyleSheet(f"""
            background-color: #1e1e2e;
            border: 1px solid {rank_color};
            color: {rank_color};
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 13px;
            font-weight: bold;
        """)
        layout.addWidget(lbl_rank)

        # Stats Card Grid
        grid_card = QFrame()
        grid_card.setObjectName("card")
        g_layout = QVBoxLayout(grid_card)
        g_layout.setSpacing(10)

        # WPM & Accuracy Row
        row1 = QHBoxLayout()
        row1.addWidget(self._stat_item("TYPING SPEED", f"{wpm:.1f} WPM", "#89b4fa"))
        row1.addWidget(self._stat_item("ACCURACY", f"{self.stats.get('accuracy', 100):.1f}%", "#a6e3a1"))
        g_layout.addLayout(row1)

        # Time & Typos Row
        elapsed = self.stats.get("time", 0.0)
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        time_str = f"{mins:02d}:{secs:02d}"

        row2 = QHBoxLayout()
        row2.addWidget(self._stat_item("TIME TAKEN", time_str, "#f9e2af"))
        row2.addWidget(self._stat_item("MISTAKES", str(self.stats.get("errors", 0)), "#f38ba8"))
        g_layout.addLayout(row2)

        layout.addWidget(grid_card)

        layout.addStretch()

        # Action Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(10)

        btn_retry = QPushButton("↺ Try Again")
        btn_retry.clicked.connect(self._on_retry)
        btn_layout.addWidget(btn_retry)

        btn_next = QPushButton("Next Problem ▶")
        btn_next.setObjectName("primary_btn")
        btn_next.clicked.connect(self._on_next)
        btn_layout.addWidget(btn_next)

        layout.addLayout(btn_layout)

    def _stat_item(self, label: str, value: str, color_hex: str) -> QWidget:
        widget = QWidget()
        v = QVBoxLayout(widget)
        v.setContentsMargins(4, 4, 4, 4)
        v.setSpacing(2)

        lbl = QLabel(label)
        lbl.setStyleSheet("color: #6c7086; font-size: 10px; font-weight: bold; letter-spacing: 0.5px;")
        v.addWidget(lbl)

        val = QLabel(value)
        val.setStyleSheet(f"color: {color_hex}; font-size: 17px; font-weight: bold; font-family: 'Consolas', monospace;")
        v.addWidget(val)

        return widget

    def _get_rank(self, wpm: float):
        if wpm >= 100:
            return "🚀 10x Algorithm Architect (Grandmaster)", "#cba6f7"
        elif wpm >= 80:
            return "⚡ High-Frequency Coder (Master)", "#89b4fa"
        elif wpm >= 60:
            return "🔥 Senior Developer (Proficient)", "#a6e3a1"
        elif wpm >= 40:
            return "💻 Software Engineer (Solid)", "#f9e2af"
        else:
            return "🌱 Rising Apprentice (Keep Practicing!)", "#f5e0dc"

    def _on_retry(self):
        self.restart_requested.emit()
        self.accept()

    def _on_next(self):
        self.next_requested.emit()
        self.accept()
