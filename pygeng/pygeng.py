from collections import OrderedDict
from pathlib import Path
import sys
import yaml

from PySide2.QtWidgets import QApplication

from mainWindow import MainWindow

def loadConfigFile():
  def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

  try:
    configPath = '{}/.config/pygeng'.format(str(Path.home()))
    configFile = open('{}/config'.format(configPath))
  except FileNotFoundError:
    return {}

  try:
    config = ordered_load(configFile, yaml.SafeLoader)
  except yaml.parser.ParserError as e:
    logFilename = '{}/.pygeng.log'.format(str(Path.home()))
    logFile = open(logFilename, 'a')
    logFile.write('Config file has bad formatting [{}]'.format(
      str(e).split(', ')[2]))

  print(config)
  return config

def main():
  app = QApplication(['pygeng'])
  mainWindow = MainWindow(loadConfigFile())

  mainWindow.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
