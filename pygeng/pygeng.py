from pathlib import Path
import sys
import yaml

from PySide2.QtWidgets import QApplication

from mainWindow import MainWindow

def loadConfigFile():
  try:
    configPath = '{}/.config/pygeng'.format(str(Path.home()))
    configFile = open('{}/config'.format(configPath))
  except FileNotFoundError:
    return {}

  try:
    config = yaml.load(configFile, Loader = yaml.FullLoader)
  except yaml.parser.ParserError as e:
    logFilename = '{}/.pygeng.log'.format(str(Path.home()))
    logFile = open(logFilename, 'a')
    logFile.write('Config file has bad formatting [{}]'.format(
      str(e).split(', ')[2]))

  return config

def main():
  app = QApplication(['pygeng'])
  mainWindow = MainWindow(loadConfigFile())

  mainWindow.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
