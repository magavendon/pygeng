from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout

from input import InputArea

class MainWindow(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
    self.config = config

    # Create the window
    inputArea = InputArea(self.config)

    # Layout
    layout = QVBoxLayout()
    layout.addWidget(inputArea)
    self.setLayout(layout)
