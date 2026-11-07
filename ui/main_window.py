import os
import subprocess
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QSplitter,
    QTreeWidget, QTreeWidgetItem, QLineEdit, QPushButton, QLabel,
    QAction, QMessageBox
)
from PyQt5.QtGui import QIcon, QFont
from config import config, DEFAULT_SOLUTIONS_DIR
from ui.code_typing_widget import CodeTypingWidget
from ui.stats_bar import StatsBar
from ui.explanation_panel import ExplanationPanel
from ui.completion_dialog import CompletionDialog
from ui.settings_dialog import SettingsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LeetType - Code Speed Typing & Big O Complexity Mentor")
        self.resize(1280, 800)
        self.setMinimumSize(960, 600)

        self.problem_list = [] # List of (rel_path, abs_path, display_name)
        self.current_problem_idx = -1

        self._init_ui()
        self._load_problems_tree()
        self._select_first_problem()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(6)

        # 3-Pane Splitter: [Tree Sidebar] | [Typing Center] | [Explanation Right]
        self.splitter = QSplitter(Qt.Horizontal)

        # 1. LEFT SIDEBAR: Problem Explorer
        sidebar_widget = QWidget()
        sidebar_layout = QVBoxLayout(sidebar_widget)
        sidebar_layout.setContentsMargins(4, 4, 4, 4)
        sidebar_layout.setSpacing(8)

        # App branding header
        brand_row = QHBoxLayout()
        lbl_logo = QLabel("⚡ LeetType")
        lbl_logo.setStyleSheet("font-size: 18px; font-weight: bold; color: #89b4fa; letter-spacing: 0.5px;")
        brand_row.addWidget(lbl_logo)
        brand_row.addStretch()

        btn_settings = QPushButton("⚙")
        btn_settings.setFixedSize(32, 32)
        btn_settings.setToolTip("Settings (Ctrl+,)")
        btn_settings.clicked.connect(self._open_settings)
        brand_row.addWidget(btn_settings)

        sidebar_layout.addLayout(brand_row)

        # Search / filter bar
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Filter problems...")
        self.search_input.textChanged.connect(self._filter_tree)
        sidebar_layout.addWidget(self.search_input)

        # Problem Tree Widget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.itemClicked.connect(self._on_tree_item_clicked)
        sidebar_layout.addWidget(self.tree_widget, 1)

        # Open folder button
        btn_open_folder = QPushButton("📂 Open Solutions Folder")
        btn_open_folder.setToolTip("Open the solutions directory in Windows Explorer")
        btn_open_folder.clicked.connect(self._open_solutions_folder)
        sidebar_layout.addWidget(btn_open_folder)

        self.splitter.addWidget(sidebar_widget)

        # 2. CENTER: Typing Arena
        center_widget = QWidget()
        center_layout = QVBoxLayout(center_widget)
        center_layout.setContentsMargins(4, 4, 4, 4)
        center_layout.setSpacing(6)

        # Live Stats bar
        self.stats_bar = StatsBar()
        self.stats_bar.restart_clicked.connect(self._on_restart)
        self.stats_bar.prev_clicked.connect(self._on_prev_problem)
        self.stats_bar.next_clicked.connect(self._on_next_problem)
        center_layout.addWidget(self.stats_bar)

        # Code Typing Arena
        self.typing_widget = CodeTypingWidget()
        self.typing_widget.stats_updated.connect(self.stats_bar.update_stats)
        self.typing_widget.typing_completed.connect(self._on_typing_completed)
        center_layout.addWidget(self.typing_widget, 1)

        # Bottom shortcut info
        footer_lbl = QLabel("⌨ Shortcuts: [Tab] Indent 4 spaces • [Ctrl+R] Restart • [Ctrl+N] Next Problem • [Ctrl+P] Prev Problem")
        footer_lbl.setStyleSheet("color: #6c7086; font-size: 11px; padding: 4px;")
        footer_lbl.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(footer_lbl)

        self.splitter.addWidget(center_widget)

        # 3. RIGHT: AI Explanation & Audio Narration
        self.explanation_panel = ExplanationPanel()
        self.splitter.addWidget(self.explanation_panel)

        # Set Splitter Proportions (22% left, 48% center, 30% right)
        self.splitter.setSizes([260, 620, 380])
        main_layout.addWidget(self.splitter)

        # Keyboard shortcuts
        act_settings = QAction(self)
        act_settings.setShortcut("Ctrl+,")
        act_settings.triggered.connect(self._open_settings)
        self.addAction(act_settings)

    def _load_problems_tree(self):
        self.tree_widget.clear()
        self.problem_list = []

        solutions_dir = config.get("solutions_dir", DEFAULT_SOLUTIONS_DIR)
        if not os.path.exists(solutions_dir):
            os.makedirs(solutions_dir, exist_ok=True)

        # Walk through subfolders
        try:
            subdirs = sorted([d for d in os.listdir(solutions_dir) if os.path.isdir(os.path.join(solutions_dir, d))])
        except Exception:
            subdirs = []

        for subdir in subdirs:
            sub_path = os.path.join(solutions_dir, subdir)
            category_title = subdir.replace("_", " ").title()
            cat_item = QTreeWidgetItem(self.tree_widget, [f"📁 {category_title}"])
            cat_item.setExpanded(True)
            cat_item.setFlags(cat_item.flags() & ~Qt.ItemIsSelectable)

            # Get python files
            py_files = sorted([f for f in os.listdir(sub_path) if f.endswith(".py")])
            for py_file in py_files:
                full_path = os.path.join(sub_path, py_file)
                display_name = py_file.replace(".py", "").replace("_", " ")
                prob_item = QTreeWidgetItem(cat_item, [f"📄 {display_name}"])
                prob_item.setData(0, Qt.UserRole, full_path)
                prob_item.setData(0, Qt.UserRole + 1, py_file)

                self.problem_list.append((full_path, py_file, prob_item))

        # If empty root has py files
        root_files = sorted([f for f in os.listdir(solutions_dir) if f.endswith(".py")])
        if root_files:
            root_cat = QTreeWidgetItem(self.tree_widget, ["📁 General Solutions"])
            root_cat.setExpanded(True)
            root_cat.setFlags(root_cat.flags() & ~Qt.ItemIsSelectable)
            for py_file in root_files:
                full_path = os.path.join(solutions_dir, py_file)
                display_name = py_file.replace(".py", "").replace("_", " ")
                prob_item = QTreeWidgetItem(root_cat, [f"📄 {display_name}"])
                prob_item.setData(0, Qt.UserRole, full_path)
                prob_item.setData(0, Qt.UserRole + 1, py_file)
                self.problem_list.append((full_path, py_file, prob_item))

    def _select_first_problem(self):
        if self.problem_list:
            self._select_problem_by_index(0)

    def _select_problem_by_index(self, index: int):
        if 0 <= index < len(self.problem_list):
            self.current_problem_idx = index
            full_path, py_file, item = self.problem_list[index]
            self.tree_widget.setCurrentItem(item)
            self._load_problem_file(full_path, py_file)

    def _load_problem_file(self, full_path: str, filename: str):
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                code = f.read()
            self.typing_widget.load_code(code)
            self.explanation_panel.load_problem(code, filename)
            self.typing_widget.setFocus()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to read file: {e}")

    def _on_tree_item_clicked(self, item, col):
        full_path = item.data(0, Qt.UserRole)
        filename = item.data(0, Qt.UserRole + 1)
        if full_path and os.path.exists(full_path):
            # Find in problem_list
            for idx, (path, fn, itm) in enumerate(self.problem_list):
                if path == full_path:
                    self.current_problem_idx = idx
                    break
            self._load_problem_file(full_path, filename)

    def _on_restart(self):
        self.typing_widget.restart()
        self.typing_widget.setFocus()

    def _on_prev_problem(self):
        if self.current_problem_idx > 0:
            self._select_problem_by_index(self.current_problem_idx - 1)

    def _on_next_problem(self):
        if self.current_problem_idx < len(self.problem_list) - 1:
            self._select_problem_by_index(self.current_problem_idx + 1)
        elif self.problem_list:
            self._select_problem_by_index(0)

    def _on_typing_completed(self, results: dict):
        current_name = "Problem"
        if 0 <= self.current_problem_idx < len(self.problem_list):
            current_name = self.problem_list[self.current_problem_idx][1]

        dlg = CompletionDialog(results, current_name, self)
        dlg.restart_requested.connect(self._on_restart)
        dlg.next_requested.connect(self._on_next_problem)
        dlg.exec_()

    def _filter_tree(self, text: str):
        text = text.lower().strip()
        for idx in range(self.tree_widget.topLevelItemCount()):
            cat_item = self.tree_widget.topLevelItem(idx)
            cat_matches = 0
            for c in range(cat_item.childCount()):
                child = cat_item.child(c)
                visible = text in child.text(0).lower()
                child.setHidden(not visible)
                if visible:
                    cat_matches += 1
            cat_item.setHidden(cat_matches == 0 and len(text) > 0)

    def _open_solutions_folder(self):
        folder = config.get("solutions_dir", DEFAULT_SOLUTIONS_DIR)
        if os.path.exists(folder):
            os.startfile(folder)
        else:
            QMessageBox.information(self, "Folder", f"Folder not found: {folder}")

    def _open_settings(self):
        dlg = SettingsDialog(self)
        if dlg.exec_() == SettingsDialog.Accepted:
            # Apply changes
            self.typing_widget.set_font_size(int(config.get("font_size", 14)))
            self._load_problems_tree()
            self._select_first_problem()

