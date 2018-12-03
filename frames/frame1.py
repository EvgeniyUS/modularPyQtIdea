#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init(parent):
  frame = parent.makeFrame('v')
  parent.makeTab(frame, 'icons/ru.png', 'Enter your text')
  line = parent.makeLine()
  parent.addWidget(frame, line)
  parent.makeBtn(frame, 'Enter', lambda: parent.openDial(line[0].text()))

