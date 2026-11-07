DARK_THEME_QSS = """
/* Global Application Style */
QWidget {
    background-color: #181825;
    color: #cdd6f4;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    font-size: 13px;
    selection-background-color: #45475a;
    selection-color: #f5e0dc;
}

/* Main Window & Toolbars */
QMainWindow {
    background-color: #181825;
}

QSplitter::handle {
    background-color: #313244;
}
QSplitter::handle:horizontal {
    width: 2px;
}
QSplitter::handle:vertical {
    height: 2px;
}

/* Sidebar / Problem Tree */
QTreeView, QTreeWidget {
    background-color: #1e1e2e;
    border: 1px solid #313244;
    border-radius: 8px;
    padding: 6px;
    outline: none;
}
QTreeView::item, QTreeWidget::item {
    padding: 6px 8px;
    border-radius: 6px;
    margin: 1px 0px;
}
QTreeView::item:hover, QTreeWidget::item:hover {
    background-color: #313244;
}
QTreeView::item:selected, QTreeWidget::item:selected {
    background-color: #45475a;
    color: #89b4fa;
    font-weight: bold;
}

/* Cards & Panels */
QFrame#card {
    background-color: #1e1e2e;
    border: 1px solid #313244;
    border-radius: 8px;
    padding: 12px;
}

QFrame#stats_card {
    background-color: #1e1e2e;
    border: 1px solid #313244;
    border-radius: 8px;
    padding: 8px 14px;
}

/* Buttons */
QPushButton {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 6px 14px;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #45475a;
    border-color: #89b4fa;
    color: #89b4fa;
}
QPushButton:pressed {
    background-color: #585b70;
}
QPushButton:disabled {
    background-color: #1e1e2e;
    color: #6c7086;
    border-color: #313244;
}

QPushButton#primary_btn {
    background-color: #89b4fa;
    color: #11111b;
    border: none;
}
QPushButton#primary_btn:hover {
    background-color: #b4befe;
}

QPushButton#success_btn {
    background-color: #a6e3a1;
    color: #11111b;
    border: none;
}
QPushButton#success_btn:hover {
    background-color: #94e2d5;
}

/* Line Edit & Inputs */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #1e1e2e;
    color: #cdd6f4;
    border: 1px solid #313244;
    border-radius: 6px;
    padding: 6px 10px;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #89b4fa;
}

/* ComboBox */
QComboBox {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 6px;
    padding: 4px 10px;
}
QComboBox:hover {
    border-color: #89b4fa;
}
QComboBox::drop-down {
    border: none;
}
QComboBox QAbstractItemView {
    background-color: #1e1e2e;
    border: 1px solid #313244;
    selection-background-color: #45475a;
    selection-color: #89b4fa;
    padding: 4px;
}

/* Sliders */
QSlider::groove:horizontal {
    height: 6px;
    background: #313244;
    border-radius: 3px;
}
QSlider::sub-page:horizontal {
    background: #89b4fa;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #cdd6f4;
    width: 14px;
    margin-top: -4px;
    margin-bottom: -4px;
    border-radius: 7px;
}
QSlider::handle:horizontal:hover {
    background: #b4befe;
}

/* Progress Bar */
QProgressBar {
    background-color: #313244;
    border-radius: 4px;
    text-align: center;
    color: #cdd6f4;
    font-size: 11px;
    height: 8px;
}
QProgressBar::chunk {
    background-color: #89b4fa;
    border-radius: 4px;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #181825;
    width: 8px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: #45475a;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::handle:vertical:hover {
    background: #585b70;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Badges */
QLabel#time_badge {
    background-color: rgba(137, 180, 250, 0.15);
    color: #89b4fa;
    border: 1px solid #89b4fa;
    border-radius: 6px;
    padding: 4px 10px;
    font-weight: bold;
    font-size: 13px;
}

QLabel#space_badge {
    background-color: rgba(203, 166, 247, 0.15);
    color: #cba6f7;
    border: 1px solid #cba6f7;
    border-radius: 6px;
    padding: 4px 10px;
    font-weight: bold;
    font-size: 13px;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #313244;
    border-radius: 8px;
    background-color: #1e1e2e;
}
QTabBar::tab {
    background: #181825;
    color: #a6adc8;
    padding: 8px 16px;
    margin-right: 4px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}
QTabBar::tab:selected {
    background: #1e1e2e;
    color: #89b4fa;
    font-weight: bold;
}
"""

