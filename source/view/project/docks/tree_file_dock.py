from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from PyQt5.QtWidgets import *

from source.store.project_information_store import project_information_store


class TreeFileDock(QDockWidget):

    def __init__(self):
        super().__init__()
        self.tree = None
        self.model = None
        self.path = None
        self.setWindowTitle("Files")

        self.widget = QWidget()
        self.createTree()

    def createTree(self):
        self.path = project_information_store.project_location

        self.model = QFileSystemModel()
        self.model.setRootPath(self.path)

        self.tree = QTreeView()
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.context_menu)

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))
        self.tree.doubleClicked.connect(self.handle_double_click)

        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)

        self.setWidget(self.tree)

    def context_menu(self):
        menu = QMenu()
        load_file = menu.addAction("Load File on Graph Filter")
        load_file.triggered.connect(self.load_file_on_combo)
        cursor = QCursor()
        menu.exec(cursor.pos())

    def handle_double_click(self):
        index = self.tree.currentIndex()
        type_item = self.model.type(index)
        if type_item == "g6 File" or type_item == "json File":
            self.load_file_on_combo()
        else:
            pass

    def load_file_on_combo(self):
        print("open on combo box")