from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget

class MainWindow(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
    self.config = config
