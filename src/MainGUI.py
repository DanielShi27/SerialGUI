## 2017.0.04 Initial  ##

# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import GUI


if __name__ == '__main__':
    app = wx.App()
    main_win = GUI.MyFrame(None)
    main_win.Show()
    main_win.ShowSerial(None)
    app.MainLoop()