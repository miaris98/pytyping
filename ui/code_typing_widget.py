import time
from PyQt5.QtCore import Qt, QRect, QTimer, pyqtSignal, QPoint
from PyQt5.QtWidgets import QWidget, QScrollBar
from PyQt5.QtGui import QPainter, QColor, QFont, QFontMetrics, QPen, QBrush
from core.typing_engine import TypingEngine
from core.sound_effects import SoundFX
from config import config

class CodeTypingWidget(QWidget):
    # Signals
    stats_updated = pyqtSignal(float, float, float, float, int) # wpm, acc, elapsed, progress, errors
    typing_completed = pyqtSignal(dict) # result dict

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.engine = TypingEngine("")
        
        # Colors
        self.bg_color = QColor("#181825")
        self.gutter_bg = QColor("#11111b")
        self.gutter_fg = QColor("#585b70")
        self.active_line_bg = QColor("#222336")
        self.correct_color = QColor("#a6e3a1")       # Green
        self.incorrect_color = QColor("#f38ba8")     # Red
        self.incorrect_bg = QColor("#582028")        # Dark Red Box
        self.pending_color = QColor("#6c7086")       # Dimmed slate
        self.cursor_color = QColor("#89b4fa")        # Cyan caret
        self.cursor_glow = QColor(137, 180, 250, 60)

        # Font configuration
        self.code_font = QFont("Consolas", int(config.get("font_size", 14)))
        self.code_font.setStyleHint(QFont.Monospace)
        self.setFont(self.code_font)

        # Layout metrics
        self.gutter_width = 50
        self.line_height = 24
        self.char_width = 10
        self.scroll_y = 0
        self.cursor_visible = True

        # Cursor blink timer
        self.blink_timer = QTimer(self)
        self.blink_timer.timeout.connect(self._toggle_cursor)
        self.blink_timer.start(500)

        # Live stats timer (100ms)
        self.stats_timer = QTimer(self)
        self.stats_timer.timeout.connect(self._emit_live_stats)
        self.stats_timer.start(100)

        self._recalc_metrics()

    def _toggle_cursor(self):
        self.cursor_visible = not self.cursor_visible
        self.update()

    def _recalc_metrics(self):
        fm = QFontMetrics(self.code_font)
        self.char_width = max(8, fm.horizontalAdvance("X"))
        self.line_height = max(20, fm.lineSpacing() + 6)
        lines_count = max(1, len(self.engine.target.split("\n")))
        max_digits = len(str(lines_count))
        self.gutter_width = max(45, (max_digits + 2) * self.char_width)

    def set_font_size(self, size: int):
        self.code_font.setPointSize(size)
        self.setFont(self.code_font)
        self._recalc_metrics()
        self.update()

    def load_code(self, code: str):
        self.engine.set_target(code)
        self.scroll_y = 0
        self._recalc_metrics()
        self._emit_live_stats()
        self.update()

    def restart(self):
        self.engine.set_target(self.engine.target)
        self.scroll_y = 0
        self._emit_live_stats()
        self.update()

    def _emit_live_stats(self):
        wpm = self.engine.get_wpm()
        acc = self.engine.get_accuracy()
        elapsed = self.engine.get_elapsed_seconds()
        prog = self.engine.get_progress_percent()
        errors = self.engine.error_count
        self.stats_updated.emit(wpm, acc, elapsed, prog, errors)

    def keyPressEvent(self, event):
        key = event.key()

        # Handle Backspace
        if key == Qt.Key_Backspace:
            if self.engine.handle_backspace():
                SoundFX.play_click()
                self._after_keystroke()
            return

        # Handle Tab
        if key == Qt.Key_Tab or key == Qt.Key_Backtab:
            if self.engine.handle_input("\t"):
                SoundFX.play_click()
                self._after_keystroke()
            return

        # Handle Enter / Return
        if key in (Qt.Key_Return, Qt.Key_Enter):
            expected = self.engine.target[self.engine.cursor_idx] if self.engine.cursor_idx < len(self.engine.target) else ""
            if self.engine.handle_input("\n"):
                if expected == "\n":
                    SoundFX.play_click()
                else:
                    SoundFX.play_error()
                self._after_keystroke()
            return

        # Handle standard characters
        text = event.text()
        if text and text.isprintable():
            expected = self.engine.target[self.engine.cursor_idx] if self.engine.cursor_idx < len(self.engine.target) else ""
            is_correct = (text == expected)
            
            if self.engine.handle_input(text):
                if is_correct:
                    SoundFX.play_click()
                else:
                    SoundFX.play_error()
                self._after_keystroke()
            return

        super().keyPressEvent(event)

    def _after_keystroke(self):
        self._scroll_to_cursor()
        self._emit_live_stats()
        self.update()

        if self.engine.is_completed:
            result = {
                "wpm": self.engine.get_wpm(),
                "accuracy": self.engine.get_accuracy(),
                "time": self.engine.get_elapsed_seconds(),
                "total_keystrokes": self.engine.total_keystrokes,
                "errors": self.engine.error_count
            }
            self.typing_completed.emit(result)

    def _scroll_to_cursor(self):
        # Calculate line of current cursor
        current_idx = self.engine.cursor_idx
        target = self.engine.target
        line_num = target[:current_idx].count("\n")
        
        cursor_y = line_num * self.line_height
        viewport_height = self.height()
        
        # Keep cursor in middle 50% of viewport
        target_scroll = cursor_y - (viewport_height // 2) + (self.line_height // 2)
        target_scroll = max(0, target_scroll)
        
        # Smooth follow
        self.scroll_y = target_scroll

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        self.scroll_y = max(0, self.scroll_y - (delta // 2))
        self.update()

    def mousePressEvent(self, event):
        self.setFocus()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setRenderHint(QPainter.TextAntialiasing, True)
        painter.setFont(self.code_font)

        w = self.width()
        h = self.height()

        # Fill background
        painter.fillRect(0, 0, w, h, self.bg_color)

        if not self.engine.target:
            painter.setPen(QPen(self.pending_color))
            painter.drawText(self.rect(), Qt.AlignCenter, "Select a LeetCode problem from the left menu to start typing.")
            return

        # Prepare line-by-line structure
        lines = self.engine.target.split("\n")
        total_lines = len(lines)

        # Find active line
        current_idx = self.engine.cursor_idx
        active_line_num = self.engine.target[:current_idx].count("\n")

        # Gutter background
        painter.fillRect(0, 0, self.gutter_width, h, self.gutter_bg)
        painter.setPen(QPen(QColor("#313244"), 1))
        painter.drawLine(self.gutter_width, 0, self.gutter_width, h)

        # Active line highlight in typing arena
        active_y = active_line_num * self.line_height - self.scroll_y
        if 0 <= active_y < h + self.line_height:
            painter.fillRect(self.gutter_width + 1, active_y, w - self.gutter_width, self.line_height, self.active_line_bg)

        # Track character index across lines
        char_counter = 0

        y = -self.scroll_y
        for line_idx, line in enumerate(lines):
            # Only render lines in viewport
            if y + self.line_height >= 0 and y < h:
                # Render line number
                line_str = str(line_idx + 1)
                painter.setPen(QPen(self.cursor_color if line_idx == active_line_num else self.gutter_fg))
                num_rect = QRect(0, y, self.gutter_width - 10, self.line_height)
                painter.drawText(num_rect, Qt.AlignRight | Qt.AlignVCenter, line_str)

                # Render line characters
                x = self.gutter_width + 16
                line_len = len(line)

                for col_idx, ch in enumerate(line):
                    ch_idx = char_counter + col_idx
                    ch_w = self.char_width

                    if ch_idx < current_idx:
                        # Already typed
                        is_corr = self.engine.char_states[ch_idx] if ch_idx < len(self.engine.char_states) else True
                        if is_corr:
                            painter.setPen(QPen(self.correct_color))
                            painter.drawText(x, y + self.line_height - 6, ch)
                        else:
                            # Mistyped: red background card + red char
                            painter.fillRect(x, y + 2, ch_w, self.line_height - 4, self.incorrect_bg)
                            painter.setPen(QPen(self.incorrect_color))
                            painter.drawText(x, y + self.line_height - 6, ch)
                    elif ch_idx == current_idx:
                        # Cursor is here!
                        if self.cursor_visible and self.hasFocus():
                            # Caret box / glow
                            painter.fillRect(x, y + 2, ch_w, self.line_height - 4, self.cursor_glow)
                            painter.setPen(QPen(self.cursor_color, 2))
                            painter.drawLine(x, y + 2, x, y + self.line_height - 2)

                        painter.setPen(QPen(QColor("#f5e0dc")))
                        painter.drawText(x, y + self.line_height - 6, ch)
                    else:
                        # Remaining / pending
                        painter.setPen(QPen(self.pending_color))
                        painter.drawText(x, y + self.line_height - 6, ch)

                    x += ch_w

                # Check if cursor is at the end of this line (at newline char)
                newline_idx = char_counter + line_len
                if newline_idx == current_idx and self.cursor_visible and self.hasFocus():
                    painter.fillRect(x, y + 2, self.char_width, self.line_height - 4, self.cursor_glow)
                    painter.setPen(QPen(self.cursor_color, 2))
                    painter.drawLine(x, y + 2, x, y + self.line_height - 2)
                    # Show subtle newline arrow symbol
                    painter.setPen(QPen(QColor(137, 180, 250, 160)))
                    painter.drawText(x + 2, y + self.line_height - 6, "↵")

            char_counter += len(line) + 1  # +1 for newline
            y += self.line_height

        # Overlay if not focused
        if not self.hasFocus():
            painter.fillRect(0, 0, w, h, QColor(24, 24, 37, 140))
            painter.setPen(QPen(QColor("#89b4fa")))
            painter.drawText(self.rect(), Qt.AlignCenter, "⚡ Click here to focus and practice typing")

