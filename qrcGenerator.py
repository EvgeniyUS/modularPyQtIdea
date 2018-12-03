#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
file = open('icons.qrc','w')
text = '<RCC>\n<qresource prefix="icons">\n'
iconsList = []
files = os.listdir('icons/')
for i in range(len(files)):
  name = files[i].split('.')
  if len(name) > 1:
    if name[1] == 'png' and name[0] != '__init__':
      iconsList.append(u'<file>icons/{}.{}</file>\n'.format(name[0], name[1]))
for row in iconsList:
  text += row
text += '</qresource>\n</RCC>'
print text
file.write(text)
file.close()

qrcFileText = '''
<RCC>
  <qresource prefix="icons">
    <file>icons/application-pencil-icon-icon.png</file>
    <file>icons/arrow-down-icon.png</file>
    <file>icons/Delete-icon.png</file>
    <file>icons/folder-pencil-icon-icon.png</file>
    <file>icons/folder-plus-icon-icon.png</file>
    <file>icons/icon-accept-icon.png</file>
    <file>icons/icon-alert-icon.png</file>
    <file>icons/icon-home-icon.png</file>
    <file>icons/icon-info-icon.png</file>
    <file>icons/Image-icon.png</file>
    <file>icons/Places-folder-red-icon.png</file>
    <file>icons/star-icon.png</file>
    <file>icons/Very-Basic-Icons8-Cup-icon.png</file>
    <file>icons/Very-Basic-Icons8-Cup-icon0.png</file>
  </qresource>
</RCC>
'''
