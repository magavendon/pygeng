from PySide2.QtGui import QPalette, QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, \
QLineEdit

def setupContainer(objectInfo):
  widget = QWidget()

  # Define the looks for this widget and sub-widgets.
  widgetLooks = objectInfo.get('looks', {})
  if len(widgetLooks) > 0:
    # If the background color was given,
    if 'background' in widgetLooks:
      # Define the color.
      w_color = QColor()
      w_color.setNamedColor(widgetLooks['background'])

      # Set the background to that color.
      w_background = QPalette()
      w_background.setColor(QPalette.Base, w_color)
      widget.setPalette(w_background)

  # Define the layout for this widget.
  w_layout = objectInfo.get('layout', 'horizontal')
  layout = None
  if w_layout == 'horizontal':
    layout = QHBoxLayout()
  elif w_layout == 'vertical':
    layout = QVBoxLayout()

  # Add other widgets.
  subObjects = objectInfo.get('contains', {})
  for subName in subObjects:
    subObject = subObjects[subName]
    subObjectType = subObject.get('type', 'container')
    if not 'looks' in subObject:
      subObject['looks'] = widgetLooks
    subWidget = guiTypes[subObjectType](subObject)
    layout.addWidget(subWidget)

  widget.setLayout(layout)
  return widget

def setupLabel(objectInfo):
  widget = QLabel()

  # Define the looks for this widget.
  widgetLooks = objectInfo.get('looks', {})
  if len(widgetLooks) > 0:
    # If the background color was given,
    if 'background' in widgetLooks:
      # Define the color.
      w_color = QColor()
      w_color.setNamedColor(widgetLooks['background'])

      # Set the background to that color.
      w_background = QPalette()
      w_background.setColor(QPalette.Base, w_color)
      widget.setPalette(w_background)

  # Define how this widget works.
  w_info = objectInfo.get('info', {})
  widget.setText(w_info.get('text', ''))
  widget.setToolTip(w_info.get('onhover', ''))

  return widget

def setupLineEdit(objectInfo):
  widget = QLineEdit()

  # Define the looks for this widget.
  widgetLooks = objectInfo.get('looks', {})
  if len(widgetLooks) > 0:
    # If the background color was given,
    if 'background' in widgetLooks:
      # Define the color.
      w_color = QColor()
      w_color.setNamedColor(widgetLooks['background'])

      # Set the background to that color.
      w_background = QPalette()
      w_background.setColor(QPalette.Base, w_color)
      widget.setPalette(w_background)

  return widget

guiTypes = {
    'container' : setupContainer,
    'label'     : setupLabel,
    'line_edit' : setupLineEdit,
}

class MainWindow(QWidget):
  def __init__(self, config):
    QWidget.__init__(self)
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)

    # Add defined sections from config file
    if len(config) > 0:
      layout = QVBoxLayout()

      for guiName in config:
        guiObject = config[guiName]
        guiObjectType = guiObject.get('type', 'container')
        guiWidget = guiTypes[guiObjectType](guiObject)
        layout.addWidget(guiWidget)

      self.setLayout(layout)
