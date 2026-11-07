import os
import subprocess
from PyQt5.QtCore import Qt, QSize, QByteArray
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QSplitter,
    QTreeWidget, QTreeWidgetItem, QLineEdit, QPushButton, QLabel,
    QAction, QMessageBox, QApplication, QFrame
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
        self.problem_list = [] # List of (rel_path, abs_path, display_name)
        self.current_problem_idx = -1

        self._init_ui()
        self._apply_responsive_geometry()
        self._load_problems_tree()
        self._select_first_problem()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        root_layout = QVBoxLayout(central_widget)
        root_layout.setContentsMargins(6, 6, 6, 6)
        root_layout.setSpacing(6)

        # TOP RESPONSIVE TOOLBAR
        toolbar_frame = QFrame()
        toolbar_frame.setObjectName("stats_card")
        toolbar_layout = QHBoxLayout(toolbar_frame)
        toolbar_layout.setContentsMargins(8, 4, 8, 4)
        toolbar_layout.setSpacing(8)

        lbl_logo = QLabel("⚡ LeetType")
        lbl_logo.setStyleSheet("font-size: 16px; font-weight: bold; color: #89b4fa; letter-spacing: 0.5px;")
        toolbar_layout.addWidget(lbl_logo)

        toolbar_layout.addSpacing(10)

        # Toggle Sidebar button
        self.btn_toggle_sidebar = QPushButton("📁 Problems")
        self.btn_toggle_sidebar.setCheckable(True)
        self.btn_toggle_sidebar.setChecked(True)
        self.btn_toggle_sidebar.setToolTip("Toggle Problem Explorer sidebar (Ctrl+B)")
        self.btn_toggle_sidebar.clicked.connect(self._toggle_sidebar)
        toolbar_layout.addWidget(self.btn_toggle_sidebar)

        # Toggle Explanation button
        self.btn_toggle_explanation = QPushButton("💡 Explanations")
        self.btn_toggle_explanation.setCheckable(True)
        self.btn_toggle_explanation.setChecked(True)
        self.btn_toggle_explanation.setToolTip("Toggle AI / Big O Explanation panel (Ctrl+E)")
        self.btn_toggle_explanation.clicked.connect(self._toggle_explanation)
        toolbar_layout.addWidget(self.btn_toggle_explanation)

        # Toggle Layout Orientation button (Ideal for vertical/portrait side monitors!)
        self.btn_toggle_layout = QPushButton("🔀 Layout: Columns")
        self.btn_toggle_layout.setToolTip("Switch between Horizontal Columns and Vertical Stacked layout for side/portrait monitors (Ctrl+L)")
        self.btn_toggle_layout.clicked.connect(self._toggle_work_orientation)
        toolbar_layout.addWidget(self.btn_toggle_layout)

        toolbar_layout.addStretch()

        btn_settings = QPushButton("⚙ Settings")
        btn_settings.setToolTip("Open Settings (Ctrl+,)")
        btn_settings.clicked.connect(self._open_settings)
        toolbar_layout.addWidget(btn_settings)

        root_layout.addWidget(toolbar_frame)

        # NESTED SPLITTER ARCHITECTURE
        # main_splitter: [sidebar_widget] | [work_splitter]
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.main_splitter.setChildrenCollapsible(True)

        # 1. LEFT SIDEBAR: Problem Explorer
        self.sidebar_widget = QWidget()
        self.sidebar_widget.setMinimumWidth(180)
        sidebar_layout = QVBoxLayout(self.sidebar_widget)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(6)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Filter problems...")
        self.search_input.textChanged.connect(self._filter_tree)
        sidebar_layout.addWidget(self.search_input)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.itemClicked.connect(self._on_tree_item_clicked)
        sidebar_layout.addWidget(self.tree_widget, 1)

        btn_open_folder = QPushButton("📂 Open Solutions Folder")
        btn_open_folder.setToolTip("Open the solutions directory in Windows Explorer")
        btn_open_folder.clicked.connect(self._open_solutions_folder)
        sidebar_layout.addWidget(btn_open_folder)

        self.main_splitter.addWidget(self.sidebar_widget)

        # 2. WORK SPLITTER: Holds [Typing Arena] and [Explanation Panel]
        # Can toggle between Qt.Horizontal (Landscape) and Qt.Vertical (Portrait side monitors!)
        self.work_splitter = QSplitter(Qt.Horizontal)
        self.work_splitter.setChildrenCollapsible(True)

        # CENTER: Typing Arena
        self.center_widget = QWidget()
        self.center_widget.setMinimumWidth(260)
        center_layout = QVBoxLayout(self.center_widget)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(6)

        self.stats_bar = StatsBar()
        self.stats_bar.restart_clicked.connect(self._on_restart)
        self.stats_bar.prev_clicked.connect(self._on_prev_problem)
        self.stats_bar.next_clicked.connect(self._on_next_problem)
        center_layout.addWidget(self.stats_bar)

        self.typing_widget = CodeTypingWidget()
        self.typing_widget.stats_updated.connect(self.stats_bar.update_stats)
        self.typing_widget.typing_completed.connect(self._on_typing_completed)
        center_layout.addWidget(self.typing_widget, 1)

        footer_lbl = QLabel("Shortcuts: [Tab] Indent • [Ctrl+R] Restart • [Ctrl+N] Next • [Ctrl+B] Toggle Sidebar • [Ctrl+L] Layout")
        footer_lbl.setStyleSheet("color: #6c7086; font-size: 11px; padding: 2px;")
        footer_lbl.setAlignment(Qt.AlignCenter)
        center_layout.addWidget(footer_lbl)

        self.work_splitter.addWidget(self.center_widget)

        # RIGHT: Explanation Panel
        self.explanation_panel = ExplanationPanel()
        self.explanation_panel.setMinimumWidth(240)
        self.work_splitter.addWidget(self.explanation_panel)

        self.main_splitter.addWidget(self.work_splitter)
        root_layout.addWidget(self.main_splitter, 1)

        # Allow flexible minimum size for small/side/tiled monitors
        self.setMinimumSize(480, 360)

        # Keyboard shortcuts
        act_toggle_sidebar = QAction(self)
        act_toggle_sidebar.setShortcut("Ctrl+B")
        act_toggle_sidebar.triggered.connect(self._toggle_sidebar)
        self.addAction(act_toggle_sidebar)

        act_toggle_explanation = QAction(self)
        act_toggle_explanation.setShortcut("Ctrl+E")
        act_toggle_explanation.triggered.connect(self._toggle_explanation)
        self.addAction(act_toggle_explanation)

        act_toggle_layout = QAction(self)
        act_toggle_layout.setShortcut("Ctrl+L")
        act_toggle_layout.triggered.connect(self._toggle_work_orientation)
        self.addAction(act_toggle_layout)

        act_settings = QAction(self)
        act_settings.setShortcut("Ctrl+,")
        act_settings.triggered.connect(self._open_settings)
        self.addAction(act_settings)

    def _apply_responsive_geometry(self):
        """Intelligently detects monitor resolution, DPI, and restores saved position."""
        # 1. Try to restore previous window geometry if saved
        saved_geom = config.get("window_geometry")
        if saved_geom:
            try:
                geom_bytes = QByteArray.fromHex(saved_geom.encode('ascii'))
                if self.restoreGeometry(geom_bytes):
                    # Check saved layout orientation
                    saved_orientation = config.get("layout_orientation", "horizontal")
                    if saved_orientation == "vertical":
                        self._set_vertical_layout()
                    else:
                        self._set_horizontal_layout()
                    return
            except Exception as e:
                print(f"Could not restore window geometry: {e}")

        # 2. Otherwise calculate smart initial geometry for current monitor
        screen = QApplication.primaryScreen()
        geom = screen.availableGeometry()
        w, h = geom.width(), geom.height()

        # Check if screen is portrait (height > width) or narrow side monitor
        is_portrait = (h > w) or (w < 1100)

        if is_portrait:
            # Optimize for vertical side monitor:
            init_w = min(w - 40, 950)
            init_h = min(h - 60, 1400)
            self.resize(init_w, init_h)
            self._set_vertical_layout()
            # In portrait, give 220px to sidebar, and rest to stacked workspace
            self.main_splitter.setSizes([200, init_w - 200])
            self.work_splitter.setSizes([int(init_h * 0.58), int(init_h * 0.42)])
        else:
            # Standard landscape monitor
            init_w = min(1280, int(w * 0.90))
            init_h = min(820, int(h * 0.88))
            self.resize(init_w, init_h)
            self._set_horizontal_layout()
            self.main_splitter.setSizes([220, init_w - 220])
            self.work_splitter.setSizes([int((init_w - 220) * 0.60), int((init_w - 220) * 0.40)])

        # Center on current screen
        self.move(geom.x() + (w - self.width()) // 2, geom.y() + (h - self.height()) // 2)

    def _toggle_sidebar(self):
        visible = self.sidebar_widget.isHidden()
        self.sidebar_widget.setVisible(visible)
        self.btn_toggle_sidebar.setChecked(visible)

    def _toggle_explanation(self):
        visible = self.explanation_panel.isHidden()
        self.explanation_panel.setVisible(visible)
        self.btn_toggle_explanation.setChecked(visible)

    def _toggle_work_orientation(self):
        if self.work_splitter.orientation() == Qt.Horizontal:
            self._set_vertical_layout()
        else:
            self._set_horizontal_layout()

    def _set_horizontal_layout(self):
        self.work_splitter.setOrientation(Qt.Horizontal)
        self.btn_toggle_layout.setText("🔀 Layout: Columns")
        total_w = self.work_splitter.width()
        if total_w > 0:
            self.work_splitter.setSizes([int(total_w * 0.60), int(total_w * 0.40)])
        config.set("layout_orientation", "horizontal")

    def _set_vertical_layout(self):
        self.work_splitter.setOrientation(Qt.Vertical)
        self.btn_toggle_layout.setText("🔀 Layout: Stacked")
        total_h = self.work_splitter.height()
        if total_h > 0:
            self.work_splitter.setSizes([int(total_h * 0.58), int(total_h * 0.42)])
        config.set("layout_orientation", "vertical")

    def closeEvent(self, event):
        """Save window position, size, and layout state on close so it persists on side monitors."""
        try:
            geom = self.saveGeometry().toHex().data().decode('ascii')
            config.set("window_geometry", geom)
            orientation = "vertical" if self.work_splitter.orientation() == Qt.Vertical else "horizontal"
            config.set("layout_orientation", orientation)
        except Exception as e:
            print(f"Error saving window state on close: {e}")
        super().closeEvent(event)

    def _load_problems_tree(self):
        self.tree_widget.clear()
        self.problem_list = []

        solutions_dir = config.get("solutions_dir", DEFAULT_SOLUTIONS_DIR)
        if not os.path.exists(solutions_dir):
            os.makedirs(solutions_dir, exist_ok=True)

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

            py_files = sorted([f for f in os.listdir(sub_path) if f.endswith(".py")])
            for py_file in py_files:
                full_path = os.path.join(sub_path, py_file)
                display_name = py_file.replace(".py", "").replace("_", " ")
                prob_item = QTreeWidgetItem(cat_item, [f"📄 {display_name}"])
                prob_item.setData(0, Qt.UserRole, full_path)
                prob_item.setData(0, Qt.UserRole + 1, py_file)

                self.problem_list.append((full_path, py_file, prob_item))

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
            self.typing_widget.set_font_size(int(config.get("font_size", 14)))
            self._load_problems_tree()
            self._select_first_problem()
