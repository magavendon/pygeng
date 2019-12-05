from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout

class InputArea(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)

    # Get input area dictionary
    inputAreaConfig = config.get('input_area', {})

    # Define the prompt
    promptText = inputAreaConfig.get('prompt_text', 'pygeng')
    prompt = QLabel(promptText)

    # Layout
    layout = QHBoxLayout()
    layout.addWidget(prompt)
    self.setLayout(layout)
