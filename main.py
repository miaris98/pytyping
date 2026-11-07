import sys
import os
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QIcon
from ui.theme import DARK_THEME_QSS
from ui.main_window import MainWindow

def main():
    # Enable High DPI display support on Windows
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("LeetType")
    app.setApplicationDisplayName("LeetType")

    # Set icon
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    # Set default app font
    default_font = QFont("Segoe UI", 10)
    app.setFont(default_font)

    # Apply sleek dark theme
    app.setStyleSheet(DARK_THEME_QSS)

    window = MainWindow()
    if os.path.exists(icon_path):
        window.setWindowIcon(QIcon(icon_path))
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
