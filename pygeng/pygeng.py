import sys

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(['ellow World'])
hello = QWidget()
helloLabel = QLabel('ellow World')
helloLayout = QVBoxLayout()
helloLayout.addWidget(helloLabel)
hello.setLayout(helloLayout)
hello.show()
sys.exit(app.exec_())

if __name__ == '__main__':
  pass
