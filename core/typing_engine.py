import time
from typing import List, Tuple

class TypingEngine:
    def __init__(self, target_code: str = ""):
        self.set_target(target_code)

    def set_target(self, target_code: str):
        # Normalize newlines
        self.target = target_code.replace("\r\n", "\n").replace("\r", "\n").strip()
        self.typed_chars: List[str] = []
        self.cursor_idx: int = 0
        self.start_time: float = 0.0
        self.end_time: float = 0.0
        self.is_started: bool = False
        self.is_completed: bool = False
        self.total_keystrokes: int = 0
        self.error_count: int = 0
        # Map of index -> bool (True = correct, False = mistyped)
        self.char_states: List[bool] = []

    def handle_input(self, char: str) -> bool:
        """
        Handle a typed character (or special sequence).
        Returns True if state changed.
        """
        if self.is_completed or not self.target:
            return False

        if not self.is_started:
            self.start_time = time.time()
            self.is_started = True

        self.total_keystrokes += 1

        if self.cursor_idx >= len(self.target):
            self.complete()
            return True

        expected = self.target[self.cursor_idx]

        # Handle Tab key (insert 4 spaces)
        if char == "\t":
            for _ in range(4):
                if self.cursor_idx < len(self.target):
                    if self.target[self.cursor_idx] == " ":
                        self.typed_chars.append(" ")
                        self.char_states.append(True)
                        self.cursor_idx += 1
                    else:
                        break
            if self.cursor_idx >= len(self.target):
                self.complete()
            return True

        # Handle Enter key
        if char == "\n" or char == "\r":
            # If expected is newline
            if expected == "\n":
                self.typed_chars.append("\n")
                self.char_states.append(True)
                self.cursor_idx += 1
                
                # Optional: auto-skip leading spaces on new line if any
                # Let's see if next characters are indentation spaces
                # Many typing tutors auto-indent or allow typing spaces.
                # Auto-matching leading indentation makes coding typing super smooth!
                while self.cursor_idx < len(self.target) and self.target[self.cursor_idx] == " ":
                    self.typed_chars.append(" ")
                    self.char_states.append(True)
                    self.cursor_idx += 1
            else:
                self.typed_chars.append(char)
                self.char_states.append(False)
                self.error_count += 1
                self.cursor_idx += 1
        else:
            # Regular character
            is_correct = (char == expected)
            self.typed_chars.append(char)
            self.char_states.append(is_correct)
            if not is_correct:
                self.error_count += 1
            self.cursor_idx += 1

        if self.cursor_idx >= len(self.target):
            self.complete()

        return True

    def handle_backspace(self) -> bool:
        if not self.is_started or self.cursor_idx == 0 or self.is_completed:
            return False

        # Pop last typed character
        self.typed_chars.pop()
        self.char_states.pop()
        self.cursor_idx -= 1
        
        # If we backed into an auto-indented line, optionally pop leading spaces
        # (Only if previous was an auto-skipped sequence of spaces right after a newline)
        return True

    def complete(self):
        self.is_completed = True
        self.end_time = time.time()

    def get_elapsed_seconds(self) -> float:
        if not self.is_started:
            return 0.0
        if self.is_completed:
            return max(0.001, self.end_time - self.start_time)
        return max(0.001, time.time() - self.start_time)

    def get_wpm(self) -> float:
        elapsed_sec = self.get_elapsed_seconds()
        if elapsed_sec <= 0:
            return 0.0
        correct_count = sum(1 for s in self.char_states if s)
        # Standard formula: (correct characters / 5) / (minutes)
        wpm = (correct_count / 5.0) / (elapsed_sec / 60.0)
        return max(0.0, round(wpm, 1))

    def get_accuracy(self) -> float:
        if self.total_keystrokes == 0:
            return 100.0
        correct_count = sum(1 for s in self.char_states if s)
        acc = (correct_count / self.total_keystrokes) * 100.0
        return max(0.0, min(100.0, round(acc, 1)))

    def get_progress_percent(self) -> float:
        if not self.target:
            return 0.0
        pct = (self.cursor_idx / len(self.target)) * 100.0
        return min(100.0, max(0.0, round(pct, 1)))

