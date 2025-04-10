# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class window
###########################################################################

class window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片加解密程序", pos = wx.DefaultPosition, size = wx.Size( 1242,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		LayRoot = wx.BoxSizer( wx.VERTICAL )

		LayMain = wx.BoxSizer( wx.HORIZONTAL )

		LayFile = wx.BoxSizer( wx.HORIZONTAL )

		LayFileBrower = wx.BoxSizer( wx.VERTICAL )

		self.FilePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		LayFileBrower.Add( self.FilePanel, 1, wx.EXPAND |wx.ALL, 5 )


		LayFile.Add( LayFileBrower, 1, wx.EXPAND, 5 )

		LayFileFunc = wx.BoxSizer( wx.VERTICAL )

		LayFileFunc.SetMinSize( wx.Size( 50,200 ) )
		self.FileChoose = wx.Button( self, wx.ID_ANY, u"选择图片文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.FileChoose, 0, wx.ALL, 5 )


		LayFile.Add( LayFileFunc, 1, wx.EXPAND, 5 )


		LayMain.Add( LayFile, 1, wx.EXPAND, 5 )

		LayImage = wx.BoxSizer( wx.HORIZONTAL )

		ImageFunc = wx.BoxSizer( wx.VERTICAL )

		AlgorithmChoices = [ u"算法1", u"算法2" ]
		self.Algorithm = wx.ComboBox( self, wx.ID_ANY, u"选择算法", wx.DefaultPosition, wx.Size( 150,-1 ), AlgorithmChoices, 0 )
		ImageFunc.Add( self.Algorithm, 0, wx.ALL, 5 )

		self.Encrypt_button22 = wx.Button( self, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Encrypt_button22, 0, wx.ALL, 5 )

		self.Decryption_button23 = wx.Button( self, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Decryption_button23, 0, wx.ALL, 5 )

		self.Save_button24 = wx.Button( self, wx.ID_ANY, u"保存图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Save_button24, 0, wx.ALL, 5 )


		LayImage.Add( ImageFunc, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


		LayImage.Add( bSizer25, 1, wx.EXPAND, 5 )


		LayMain.Add( LayImage, 1, wx.EXPAND, 5 )


		LayRoot.Add( LayMain, 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.SavaAnalysis_button25 = wx.Button( self, wx.ID_ANY, u"保存分析结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.SavaAnalysis_button25, 0, wx.ALL, 5 )


		bSizer17.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer28.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer17.Add( bSizer28, 1, wx.EXPAND, 5 )


		LayRoot.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( LayRoot )
		self.Layout()
		self.m_menubar5 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menu3.AppendSubMenu( self.m_menu1, u"MyMenu" )

		self.m_menubar5.Append( self.m_menu3, u"MyMenu" )

		self.SetMenuBar( self.m_menubar5 )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

if __name__ == '__main__':
    app = wx.App()
    browser = window(None)
    browser.SetSize((800, 600))  # 设置窗口大小to 800x600
    browser.Show()
    app.MainLoop()
