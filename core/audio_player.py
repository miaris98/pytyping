import os
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from core.tts_service import tts_service
from config import config

class TTSWorker(QThread):
    finished_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, text: str, voice: str, speed: float):
        super().__init__()
        self.text = text
        self.voice = voice
        self.speed = speed

    def run(self):
        try:
            audio_path = tts_service.synthesize_to_file(self.text, self.voice, self.speed)
            if audio_path and os.path.exists(audio_path):
                self.finished_signal.emit(audio_path)
            else:
                self.error_signal.emit("Could not generate audio")
        except Exception as e:
            self.error_signal.emit(str(e))

class AudioPlayer(QObject):
    # Signals for UI
    status_changed = pyqtSignal(str)
    state_changed = pyqtSignal(int)
    position_changed = pyqtSignal(int, int)  # current_ms, total_ms
    playback_finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.current_worker = None
        self.current_text = ""
        self.current_file = ""
        self.speed = float(config.get("tts_speed", 1.0))

        self.player.stateChanged.connect(self._on_state_changed)
        self.player.positionChanged.connect(self._on_position_changed)
        self.player.durationChanged.connect(self._on_duration_changed)

    def play_text(self, text: str, voice: str = None, speed: float = None):
        """Synthesizes text in background (if needed) and plays audio."""
        if not text:
            return

        self.stop()
        self.current_text = text
        
        if voice is None:
            voice = config.get("edge_voice", "en-US-ChristopherNeural")
        if speed is None:
            speed = float(config.get("tts_speed", 1.0))
        self.speed = speed

        self.status_changed.emit("Synthesizing audio explanation...")

        # Stop any existing worker
        if self.current_worker and self.current_worker.isRunning():
            self.current_worker.terminate()
            self.current_worker.wait()

        self.current_worker = TTSWorker(text, voice, speed)
        self.current_worker.finished_signal.connect(self._on_synthesis_finished)
        self.current_worker.error_signal.connect(self._on_synthesis_error)
        self.current_worker.start()

    def _on_synthesis_finished(self, audio_path: str):
        self.current_file = audio_path
        media_url = QUrl.fromLocalFile(os.path.abspath(audio_path))
        self.player.setMedia(QMediaContent(media_url))
        self.player.play()
        self.status_changed.emit("Playing")

    def _on_synthesis_error(self, err_msg: str):
        self.status_changed.emit(f"Audio Error: {err_msg}")

    def toggle_play_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.status_changed.emit("Paused")
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
            self.status_changed.emit("Playing")
        elif self.current_text:
            self.play_text(self.current_text)

    def pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.status_changed.emit("Paused")

    def resume(self):
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
            self.status_changed.emit("Playing")

    def stop(self):
        if self.player.state() != QMediaPlayer.StoppedState:
            self.player.stop()
        self.status_changed.emit("Stopped")

    def seek(self, position_ms: int):
        self.player.setPosition(position_ms)

    def is_playing(self) -> bool:
        return self.player.state() == QMediaPlayer.PlayingState

    def _on_state_changed(self, state):
        self.state_changed.emit(state)
        if state == QMediaPlayer.StoppedState:
            self.status_changed.emit("Stopped")
            if self.player.position() > 0 and self.player.position() >= self.player.duration() - 500:
                self.playback_finished.emit()
        elif state == QMediaPlayer.PlayingState:
            self.status_changed.emit("Playing")
        elif state == QMediaPlayer.PausedState:
            self.status_changed.emit("Paused")

    def _on_position_changed(self, pos):
        self.position_changed.emit(pos, self.player.duration())

    def _on_duration_changed(self, dur):
        self.position_changed.emit(self.player.position(), dur)

# Global player instance
audio_player = AudioPlayer()

