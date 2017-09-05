# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 30 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import serial
import serial.tools.list_ports  

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
    
    SerialIsOpen=False
    ReceiveCnt=0
    SendCnt=0
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SerialGUI", pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        wSizer1 = wx.WrapSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Serial Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.m_staticText1.SetMinSize( wx.Size( 100,-1 ) )
        
        wSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        S_listChoices = []
        self.S_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, S_listChoices, 0 )
        self.S_list.SetSelection( 0 )
        self.S_list.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.S_list.SetMinSize( wx.Size( 180,-1 ) )
        
        wSizer1.Add( self.S_list, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.ok_button = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ok_button.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.ok_button.SetMinSize( wx.Size( 80,-1 ) )
        
        wSizer1.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.clear_button = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.clear_button.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.clear_button.SetMinSize( wx.Size( 80,-1 ) )
        
        wSizer1.Add( self.clear_button, 0, wx.ALL, 5 )
        
        rsvSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Receive" ), wx.VERTICAL )
        
        rsvSizer.SetMinSize( wx.Size( 500,200 ) ) 
        self.m_RsvTextCtrl = wx.TextCtrl( rsvSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_MULTILINE )
        self.m_RsvTextCtrl.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        
        rsvSizer.Add( self.m_RsvTextCtrl, 0, wx.ALL, 5 )
        
        
        wSizer1.Add( rsvSizer, 1, wx.EXPAND, 5 )
        
        sendSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Send" ), wx.HORIZONTAL )
        
        sendSizer.SetMinSize( wx.Size( 500,50 ) ) 
        self.m_SendTextCtrl = wx.TextCtrl( sendSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_SendTextCtrl.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.m_SendTextCtrl.SetMinSize( wx.Size( 400,30 ) )
        
        sendSizer.Add( self.m_SendTextCtrl, 0, wx.ALL, 5 )
        
        self.s_button = wx.Button( sendSizer.GetStaticBox(), wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.s_button.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.s_button.SetMinSize( wx.Size( 100,-1 ) )
        
        sendSizer.Add( self.s_button, 0, wx.ALL, 5 )
        
        
        wSizer1.Add( sendSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( wSizer1 )
        self.Layout()
        self.m_statusBar = self.CreateStatusBar( )
        self.m_statusBar.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "等线" ) )
        self.m_statusBar.SetFieldsCount(2)  
        self.m_statusBar.SetStatusWidths([-1, -1])
        self.m_statusBar.SetStatusText(u"Receive:", 0)
        self.m_statusBar.SetStatusText(u"Send:", 1)
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.Menu = wx.Menu()
        self.m_menubar1.Append( self.Menu, u"File" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menubar1.Append( self.m_menu3, u"View" ) 
        
        self.m_menu4 = wx.Menu()
        self.m_menubar1.Append( self.m_menu4, u"Tools" ) 
        
        self.m_menu5 = wx.Menu()
        self.m_menubar1.Append( self.m_menu5, u"Help" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_ACTIVATE, self.Frame_Active )
        self.ok_button.Bind( wx.EVT_BUTTON, self.ok_button_click )
        self.clear_button.Bind( wx.EVT_BUTTON, self.clear_button_click )
        self.s_button.Bind( wx.EVT_BUTTON, self.send_button_click )
    
    def __del__( self ):
        pass
    
    def ShowSerial( self, event ):
        port_list = list(serial.tools.list_ports.comports())  
        if len(port_list) <= 0:  
            print "The Serial port can't find!"  
        else:
            for s in port_list:
                self.S_list.Append(s[0])
                
    # Virtual event handlers, overide them in your derived class
    def Frame_Active( self, event ):
        #event.Skip()
        if(self.SerialIsOpen==True):
            n = self.t.inWaiting()
            if(n>0):
                ReadStr=self.t.read(n)
                LastVal=str(self.m_RsvTextCtrl.Value)
                self.m_RsvTextCtrl.SetValue(LastVal+ReadStr)                
                if(ReadStr.find("\r")>0):
                    self.ReceiveCnt= self.ReceiveCnt+n-2
                else:
                    self.ReceiveCnt= self.ReceiveCnt+n
                self.m_statusBar.SetStatusText(u"Receive:" + str(self.ReceiveCnt), 0)
            else:
                pass
        else:
            event.Skip()


    def ok_button_click( self, event ):
        #event.Skip()
        if(self.SerialIsOpen==False):
            sName=self.S_list.GetStringSelection()
            self.t = serial.Serial(sName,9600)
            self.t.write('Hello !\r\n')
            self.ok_button.SetLabel(u"Close")
            self.SerialIsOpen=True
        else:
            self.t.close()
            self.t=None
            self.ok_button.SetLabel(u"Open")
            self.SerialIsOpen=False
    
    def send_button_click( self, event ):
        #event.Skip()
        if(self.SerialIsOpen==True):
            SendStr=str(self.m_SendTextCtrl.GetValue())+"\r\n"
            pass
            n=self.t.write(SendStr)
            self.SendCnt=self.SendCnt+n-2
            self.m_statusBar.SetStatusText(u"Send:" + str(self.SendCnt), 1)
        else:
            event.Skip()

    def clear_button_click( self, event ):
        self.m_RsvTextCtrl.SetValue("")
        self.ReceiveCnt=0
        self.SendCnt=0
        self.m_statusBar.SetStatusText(u"Receive:", 0)
        self.m_statusBar.SetStatusText(u"Send:", 1)
        #event.Skip()