from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit

class InputArea(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)

    # Get input area dictionary
    inputAreaConfig = config.get('input_area', {})

    # Define the prompt
    promptText = inputAreaConfig.get('prompt_text', 'pygeng')
    prompt = QLabel(promptText)

    # Define the textbox
    userInputConfig = inputAreaConfig.get('user_input', {})
    userInputColor = QColor()
    userInputColor.setNamedColor(userInputConfig.get('background', '#00000000'))
    userInputPalette = QPalette()
    userInputPalette.setColor(QPalette.Base, userInputColor)
    userInput = QLineEdit()
    userInput.setPalette(userInputPalette)
    userInput.setFrame(False)

    # Layout
    layout = QHBoxLayout()
    layout.addWidget(prompt)
    layout.addWidget(userInput)
    self.setLayout(layout)
