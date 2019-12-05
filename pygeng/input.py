from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout

class InputArea(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)

    # Define the prompt
    promptText = config.get('prompt_text', 'pygeng')
    prompt = QLabel(self, promptText)

    # Layout
    layout = QHBoxLayout()
    layout.addWidget(prompt)
    self.setLayout(prompt)
