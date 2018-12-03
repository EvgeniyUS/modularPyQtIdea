#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from importlib import import_module

imps = []
def loadImports(path):
    files = os.listdir(path)
    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
               name = name[0]
               imps.append(name)
    file = open(path+'__init__.py','w')
    toWrite = '__all__ = '+str(imps)
    file.write(toWrite)
    file.close()
loadImports('plugins/')


class MainWindow(QtGui.QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.win  = QtGui.QWidget(self)
    self.tabs = QtGui.QTabWidget(self.win)
    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(self.tabs)
    self.win.setLayout(hbox)
    self.setCentralWidget(self.win)
    for i in imps:
      import_module('plugins.{}'.format(i)).init(self)

  def loadFrame(self, name):
    import_module('frames.{}'.format(name)).init(self)

  def makeTab(self, widget, icon, title):
    self.tabs.addTab(widget[0], QtGui.QIcon('{}'.format(icon)), title)

  def addWidget(self, parent, widget):
    parent[1].addWidget(widget[0])

  def makeLine(self):
    line = QtGui.QLineEdit()
    return (line, False)

  def makeFrame(self, layout):
    frame = QtGui.QFrame()
    if layout == 'v':
      box = QtGui.QVBoxLayout()
    elif layout == 'h':
      box = QtGui.QHBoxLayout()
    frame.setLayout(box)
    return (frame, box)

  def makeBtn(self, widget, title, action):
    btn = QtGui.QPushButton(QtGui.QIcon('icons/ru.png'), u'{}'.format(title), widget[0])
    btn.clicked.connect(action)
    widget[1].addWidget(btn)

  def closeTab(self):
    self.tabs.removeTab(self.tabs.currentIndex())

  def openDial(self, text):
    dialog = Dialog()
    dialog.text.setText(text)
    result = dialog.exec_()

class Dialog(QtGui.QDialog):
  def __init__(self, parent=None):
    super(Dialog, self).__init__(parent)
    self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
    self.setMinimumSize(300, 0)
    self.setMaximumSize(500, 0)
    layout = QtGui.QVBoxLayout(self)
    self.text = QtGui.QTextEdit()

    buttons = QtGui.QDialogButtonBox(
      QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
      QtCore.Qt.Horizontal, self)
    buttons.accepted.connect(self.accept)
    buttons.rejected.connect(self.reject)
    layout.addWidget(self.text)
    layout.addWidget(buttons)

if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  mainWin = MainWindow()
  mainWin.show()
  sys.exit(app.exec_())
