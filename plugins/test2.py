#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init(parent):
  frame = parent.makeFrame('v')
  frame1 = parent.makeFrame('h')
  parent.addWidget(frame, frame1)
  parent.makeTab(frame, 'icons/ru.png', 'test2')
  parent.makeBtn(frame, 'Close', parent.closeTab)
  #for i in xrange(10):
  #  line = parent.makeLine()
  #  parent.addWidget(frame, line)
  #parent.makeTab(line, 'icons/ru.png', 'line')
  #for i in xrange(10):
  #  line = parent.makeLine()
  #  parent.addWidget(frame1, line)
  #for i in xrange(10):
  #  parent.makeBtn(frame1, 'Close', parent.closeTab)
