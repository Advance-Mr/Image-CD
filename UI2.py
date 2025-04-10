# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import cv2
import wx
import wx.xrc
import numpy as np

###########################################################################
## Class window
###########################################################################
from PIL import Image

from EncryptionDecryptionFunc import arnold_encrypt, PilImage2WxImage, arnold_decrypt

###########################################################################
## Class window
###########################################################################

class window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片加解密程序", pos = wx.DefaultPosition, size = wx.Size( 1058,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		LayRoot = wx.BoxSizer( wx.VERTICAL )

		LayMain = wx.BoxSizer( wx.HORIZONTAL )

		LayFile = wx.BoxSizer( wx.HORIZONTAL )

		LayFileBrower = wx.BoxSizer( wx.VERTICAL )

		self.m_genericDirCtrl2 = wx.GenericDirCtrl( self, wx.ID_ANY, u"D:/Image-Encryption-Decryption-main/OriImg", wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl2.ShowHidden( False )
		LayFileBrower.Add( self.m_genericDirCtrl2, 1, wx.EXPAND |wx.ALL, 5 )


		LayFile.Add( LayFileBrower, 7, wx.EXPAND, 5 )

		LayFileFunc = wx.BoxSizer( wx.VERTICAL )

		self.FileChoose = wx.Button( self, wx.ID_ANY, u"选择图片文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.FileChoose, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )


		LayFile.Add( LayFileFunc, 3, wx.EXPAND|wx.FIXED_MINSIZE, 2 )


		LayMain.Add( LayFile, 3, wx.EXPAND, 5 )

		LayImage = wx.BoxSizer( wx.HORIZONTAL )

		ImageFunc = wx.BoxSizer( wx.VERTICAL )

		AlgorithmChoices = [ u"算法1", u"算法2" ]
		self.Algorithm = wx.ComboBox( self, wx.ID_ANY, u"选择算法", wx.DefaultPosition, wx.Size( 100,-1 ), AlgorithmChoices, 0 )
		ImageFunc.Add( self.Algorithm, 0, wx.ALL, 5 )

		self.Encrypt_button = wx.Button( self, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Encrypt_button, 0, wx.ALL, 5 )

		self.Decryption_button = wx.Button( self, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Decryption_button, 0, wx.ALL, 5 )

		self.Save_button = wx.Button( self, wx.ID_ANY, u"保存图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		ImageFunc.Add( self.Save_button, 0, wx.ALL, 5 )


		LayImage.Add( ImageFunc, 1, wx.EXPAND, 5 )

		LayerImage = wx.BoxSizer( wx.HORIZONTAL )

		OriImage = wx.BoxSizer( wx.VERTICAL )

		self.OriImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriImage.Add( self.OriImage, 1, wx.ALL, 5 )


		LayerImage.Add( OriImage, 1, wx.EXPAND, 5 )

		EncryptImage = wx.BoxSizer( wx.VERTICAL )

		self.EncryptImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EncryptImage.Add( self.EncryptImage, 1, wx.ALL, 5 )


		LayerImage.Add( EncryptImage, 1, wx.EXPAND, 5 )

		DecryptImage = wx.BoxSizer( wx.VERTICAL )

		self.DecryptImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		DecryptImage.Add( self.DecryptImage, 1, wx.ALL, 5 )


		LayerImage.Add( DecryptImage, 1, wx.EXPAND, 5 )


		LayImage.Add( LayerImage, 6, wx.EXPAND, 5 )


		LayMain.Add( LayImage, 7, wx.EXPAND, 5 )


		LayRoot.Add( LayMain, 4, wx.EXPAND, 5 )

		LayerAnalysis = wx.BoxSizer( wx.VERTICAL )

		LayerAnalysisButton = wx.BoxSizer( wx.VERTICAL )

		self.StartAnalysis = wx.Button( self, wx.ID_ANY, u"开始分析", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayerAnalysisButton.Add( self.StartAnalysis, 0, wx.ALL, 5 )

		self.SavaAnalysis = wx.Button( self, wx.ID_ANY, u"保存分析结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayerAnalysisButton.Add( self.SavaAnalysis, 0, wx.ALL, 5 )


		LayerAnalysis.Add( LayerAnalysisButton, 2, wx.EXPAND, 5 )

		LayerAnalysisImage = wx.BoxSizer( wx.VERTICAL )

		self.Analysis_scrolledWindow3 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.Analysis_scrolledWindow3.SetScrollRate( 5, 5 )
		self.Analysis_scrolledWindow3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.Analysis_scrolledWindow3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		AnalysisBox = wx.BoxSizer( wx.VERTICAL )

		SensitivityAnalyBox = wx.BoxSizer( wx.HORIZONTAL )

		SensitivityAnalyLabelBox = wx.BoxSizer( wx.HORIZONTAL )

		self.SensitivityAnalyLabelBoxText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"灵敏度分析\n密钥敏感性分析\nNPCR 和 UACI 越接近理想值，加密算法对安全密钥\n的敏感度越强，加密算法越安全。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SensitivityAnalyLabelBoxText.Wrap( -1 )

		self.SensitivityAnalyLabelBoxText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		SensitivityAnalyLabelBox.Add( self.SensitivityAnalyLabelBoxText, 0, wx.EXPAND, 5 )


		SensitivityAnalyBox.Add( SensitivityAnalyLabelBox, 2, wx.EXPAND, 5 )

		SensitivityAnalyGrid1 = wx.BoxSizer( wx.HORIZONTAL )

		self.SensitivityAnalyGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.SensitivityAnalyGrid.CreateGrid( 5, 5 )
		self.SensitivityAnalyGrid.EnableEditing( True )
		self.SensitivityAnalyGrid.EnableGridLines( True )
		self.SensitivityAnalyGrid.EnableDragGridSize( False )
		self.SensitivityAnalyGrid.SetMargins( 0, 0 )

		# Columns
		self.SensitivityAnalyGrid.EnableDragColMove( False )
		self.SensitivityAnalyGrid.EnableDragColSize( True )
		self.SensitivityAnalyGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.SensitivityAnalyGrid.EnableDragRowSize( True )
		self.SensitivityAnalyGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.SensitivityAnalyGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		SensitivityAnalyGrid1.Add( self.SensitivityAnalyGrid, 0, wx.ALL, 5 )


		SensitivityAnalyBox.Add( SensitivityAnalyGrid1, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( SensitivityAnalyBox, 1, wx.EXPAND, 5 )

		HistogramBox = wx.BoxSizer( wx.HORIZONTAL )

		HistogramTextBox = wx.BoxSizer( wx.VERTICAL )

		self.HistogramText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"直方图分析（原图）\n直方图显示图像的统计信息，直观地反映了图像中各\n个灰度值的分布情况。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HistogramText.Wrap( -1 )

		HistogramTextBox.Add( self.HistogramText, 0, wx.ALL, 5 )


		HistogramBox.Add( HistogramTextBox, 2, wx.EXPAND, 5 )

		OriHistogramBox = wx.BoxSizer( wx.HORIZONTAL )

		OriHistogramG1 = wx.BoxSizer( wx.VERTICAL )

		self.OriHistogramG = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriHistogramG1.Add( self.OriHistogramG, 1, wx.ALL, 5 )


		OriHistogramBox.Add( OriHistogramG1, 1, wx.EXPAND, 5 )

		OriHistogramR1 = wx.BoxSizer( wx.VERTICAL )

		self.OriHistogramR = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriHistogramR1.Add( self.OriHistogramR, 1, wx.ALL, 5 )


		OriHistogramBox.Add( OriHistogramR1, 1, wx.EXPAND, 5 )

		OriHistogramGn1 = wx.BoxSizer( wx.VERTICAL )

		self.OriHistogramGn = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriHistogramGn1.Add( self.OriHistogramGn, 1, wx.ALL, 5 )


		OriHistogramBox.Add( OriHistogramGn1, 1, wx.EXPAND, 5 )

		OriHistogramB1 = wx.BoxSizer( wx.VERTICAL )

		self.OriHistogramB = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriHistogramB1.Add( self.OriHistogramB, 1, wx.ALL, 5 )


		OriHistogramBox.Add( OriHistogramB1, 1, wx.EXPAND, 5 )


		HistogramBox.Add( OriHistogramBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( HistogramBox, 1, wx.EXPAND, 5 )

		EnyHistogramBox1 = wx.BoxSizer( wx.HORIZONTAL )

		EnyHistogramText1 = wx.BoxSizer( wx.VERTICAL )

		self.EnyHistogramText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"直方图分析（加密图）\n直方图显示图像的统计信息，直观地反映了图像中各\n个灰度值的分布情况。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EnyHistogramText.Wrap( -1 )

		EnyHistogramText1.Add( self.EnyHistogramText, 0, wx.ALL, 5 )


		EnyHistogramBox1.Add( EnyHistogramText1, 2, wx.EXPAND, 5 )

		EnyHistogramBox = wx.BoxSizer( wx.HORIZONTAL )

		EnyHistogramBoxG = wx.BoxSizer( wx.VERTICAL )

		self.EnyHistogramG = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyHistogramBoxG.Add( self.EnyHistogramG, 1, wx.ALL, 5 )


		EnyHistogramBox.Add( EnyHistogramBoxG, 1, wx.EXPAND, 5 )

		EnyHistogramBoxR = wx.BoxSizer( wx.VERTICAL )

		self.EnyHistogramR = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyHistogramBoxR.Add( self.EnyHistogramR, 1, wx.ALL, 5 )


		EnyHistogramBox.Add( EnyHistogramBoxR, 1, wx.EXPAND, 5 )

		EnyHistogramBoxGn = wx.BoxSizer( wx.VERTICAL )

		self.EnyHistogramGn = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyHistogramBoxGn.Add( self.EnyHistogramGn, 1, wx.ALL, 5 )


		EnyHistogramBox.Add( EnyHistogramBoxGn, 1, wx.EXPAND, 5 )

		EnyHistogramBoxB = wx.BoxSizer( wx.VERTICAL )

		self.EnyHistogramB = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyHistogramBoxB.Add( self.EnyHistogramB, 1, wx.ALL, 5 )


		EnyHistogramBox.Add( EnyHistogramBoxB, 1, wx.EXPAND, 5 )


		EnyHistogramBox1.Add( EnyHistogramBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( EnyHistogramBox1, 1, wx.EXPAND, 5 )

		OriCorrelationBox1 = wx.BoxSizer( wx.HORIZONTAL )

		OriCorrelationTextBox = wx.BoxSizer( wx.VERTICAL )

		self.OriCorrelationText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"相关性分析（原图）\n由于图像相邻像素之间存在着很高的相关性，一个像\n素往往会泄露其周边像素的信息，攻击者往往可以利\n用该特性推理预测出下一个像素的灰度值,，从而实现\n对整个明文图像的恢复。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OriCorrelationText.Wrap( -1 )

		OriCorrelationTextBox.Add( self.OriCorrelationText, 0, wx.ALL, 5 )


		OriCorrelationBox1.Add( OriCorrelationTextBox, 2, wx.EXPAND, 5 )

		OriCorrelationBox = wx.BoxSizer( wx.HORIZONTAL )

		OriCorrelationBoxG = wx.BoxSizer( wx.VERTICAL )

		self.OriCorrelationG = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriCorrelationBoxG.Add( self.OriCorrelationG, 1, wx.ALL, 5 )


		OriCorrelationBox.Add( OriCorrelationBoxG, 1, wx.EXPAND, 5 )

		OriCorrelationBoxR = wx.BoxSizer( wx.VERTICAL )

		self.OriCorrelationR = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriCorrelationBoxR.Add( self.OriCorrelationR, 1, wx.ALL, 5 )


		OriCorrelationBox.Add( OriCorrelationBoxR, 1, wx.EXPAND, 5 )

		OriCorrelationBoxGn = wx.BoxSizer( wx.VERTICAL )

		self.OriCorrelationGn = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriCorrelationBoxGn.Add( self.OriCorrelationGn, 1, wx.ALL, 5 )


		OriCorrelationBox.Add( OriCorrelationBoxGn, 1, wx.EXPAND, 5 )

		OriCorrelationBoxB = wx.BoxSizer( wx.VERTICAL )

		self.OriCorrelationB = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriCorrelationBoxB.Add( self.OriCorrelationB, 1, wx.ALL, 5 )


		OriCorrelationBox.Add( OriCorrelationBoxB, 1, wx.EXPAND, 5 )


		OriCorrelationBox1.Add( OriCorrelationBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( OriCorrelationBox1, 1, wx.EXPAND, 5 )

		EnyCorrelationBox1 = wx.BoxSizer( wx.HORIZONTAL )

		EnyCorrelationText1 = wx.BoxSizer( wx.VERTICAL )

		self.EnyCorrelationText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"相关性分析（加密图）\n由于图像相邻像素之间存在着很高的相关性，一个像\n素往往会泄露其周边像素的信息，攻击者往往可以利\n用该特性推理预测出下一个像素的灰度值,，从而实现\n对整个明文图像的恢复。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EnyCorrelationText.Wrap( -1 )

		EnyCorrelationText1.Add( self.EnyCorrelationText, 0, wx.ALL, 5 )


		EnyCorrelationBox1.Add( EnyCorrelationText1, 2, wx.EXPAND, 5 )

		EnyCorrelationBox = wx.BoxSizer( wx.HORIZONTAL )

		EnyCorrelationBoxG1 = wx.BoxSizer( wx.VERTICAL )

		self.EnyCorrelationBoxG = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyCorrelationBoxG1.Add( self.EnyCorrelationBoxG, 1, wx.ALL, 5 )


		EnyCorrelationBox.Add( EnyCorrelationBoxG1, 1, wx.EXPAND, 5 )

		EnyCorrelationBoxR = wx.BoxSizer( wx.VERTICAL )

		self.EnyCorrelationR = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyCorrelationBoxR.Add( self.EnyCorrelationR, 1, wx.ALL, 5 )


		EnyCorrelationBox.Add( EnyCorrelationBoxR, 1, wx.EXPAND, 5 )

		EnyCorrelationBoxGn = wx.BoxSizer( wx.VERTICAL )

		self.EnyCorrelationGn = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyCorrelationBoxGn.Add( self.EnyCorrelationGn, 1, wx.ALL, 5 )


		EnyCorrelationBox.Add( EnyCorrelationBoxGn, 1, wx.EXPAND, 5 )

		EnyCorrelationBoxB = wx.BoxSizer( wx.VERTICAL )

		self.EnyCorrelationB = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EnyCorrelationBoxB.Add( self.EnyCorrelationB, 1, wx.ALL, 5 )


		EnyCorrelationBox.Add( EnyCorrelationBoxB, 1, wx.EXPAND, 5 )


		EnyCorrelationBox1.Add( EnyCorrelationBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( EnyCorrelationBox1, 1, wx.EXPAND, 5 )

		Information_EntropyBox = wx.BoxSizer( wx.HORIZONTAL )

		Information_EntropyTextBox = wx.BoxSizer( wx.HORIZONTAL )

		self.Information_EntropyText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"信息熵分析\n熵常用来描述事物的复杂性，信源的信息熵是度量信息\n随机性的一个重要参考指标。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Information_EntropyText.Wrap( -1 )

		Information_EntropyTextBox.Add( self.Information_EntropyText, 0, wx.ALL, 5 )


		Information_EntropyBox.Add( Information_EntropyTextBox, 2, wx.EXPAND, 5 )

		Information_EntropyGridBox = wx.BoxSizer( wx.HORIZONTAL )

		self.Information_EntropyGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Information_EntropyGrid.CreateGrid( 5, 5 )
		self.Information_EntropyGrid.EnableEditing( True )
		self.Information_EntropyGrid.EnableGridLines( True )
		self.Information_EntropyGrid.EnableDragGridSize( False )
		self.Information_EntropyGrid.SetMargins( 0, 0 )

		# Columns
		self.Information_EntropyGrid.EnableDragColMove( False )
		self.Information_EntropyGrid.EnableDragColSize( True )
		self.Information_EntropyGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Information_EntropyGrid.EnableDragRowSize( True )
		self.Information_EntropyGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Information_EntropyGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		Information_EntropyGridBox.Add( self.Information_EntropyGrid, 0, wx.ALL, 5 )


		Information_EntropyBox.Add( Information_EntropyGridBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( Information_EntropyBox, 1, wx.EXPAND, 5 )

		RandomnessBox = wx.BoxSizer( wx.HORIZONTAL )

		RandomnessTextBox = wx.BoxSizer( wx.HORIZONTAL )

		self.RandomnessText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"随机性测试\n保证密码学模块的安全性，确定随机序列的随机性质，\n防止基于伪随机性的攻击。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RandomnessText.Wrap( -1 )

		RandomnessTextBox.Add( self.RandomnessText, 0, wx.ALL, 5 )


		RandomnessBox.Add( RandomnessTextBox, 2, wx.EXPAND, 5 )

		RandomnessGrid1 = wx.BoxSizer( wx.HORIZONTAL )

		self.RandomnessGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.RandomnessGrid.CreateGrid( 5, 5 )
		self.RandomnessGrid.EnableEditing( True )
		self.RandomnessGrid.EnableGridLines( True )
		self.RandomnessGrid.EnableDragGridSize( False )
		self.RandomnessGrid.SetMargins( 0, 0 )

		# Columns
		self.RandomnessGrid.EnableDragColMove( False )
		self.RandomnessGrid.EnableDragColSize( True )
		self.RandomnessGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.RandomnessGrid.EnableDragRowSize( True )
		self.RandomnessGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.RandomnessGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		RandomnessGrid1.Add( self.RandomnessGrid, 0, wx.ALL, 5 )


		RandomnessBox.Add( RandomnessGrid1, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( RandomnessBox, 1, wx.EXPAND, 5 )

		EncryptionQualityBox = wx.BoxSizer( wx.HORIZONTAL )

		EncryptionQualityTextBox = wx.BoxSizer( wx.HORIZONTAL )

		self.EncryptionQualityText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"加密质量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptionQualityText.Wrap( -1 )

		EncryptionQualityTextBox.Add( self.EncryptionQualityText, 0, wx.ALL, 5 )


		EncryptionQualityBox.Add( EncryptionQualityTextBox, 2, wx.EXPAND, 5 )

		EncryptionQualityGridBox = wx.BoxSizer( wx.HORIZONTAL )

		self.EncryptionQualityGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.EncryptionQualityGrid.CreateGrid( 5, 5 )
		self.EncryptionQualityGrid.EnableEditing( True )
		self.EncryptionQualityGrid.EnableGridLines( True )
		self.EncryptionQualityGrid.EnableDragGridSize( False )
		self.EncryptionQualityGrid.SetMargins( 0, 0 )

		# Columns
		self.EncryptionQualityGrid.EnableDragColMove( False )
		self.EncryptionQualityGrid.EnableDragColSize( True )
		self.EncryptionQualityGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.EncryptionQualityGrid.EnableDragRowSize( True )
		self.EncryptionQualityGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.EncryptionQualityGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		EncryptionQualityGridBox.Add( self.EncryptionQualityGrid, 0, wx.ALL, 5 )


		EncryptionQualityBox.Add( EncryptionQualityGridBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( EncryptionQualityBox, 1, wx.EXPAND, 5 )

		NoiseAdditionBox3 = wx.BoxSizer( wx.HORIZONTAL )

		NoiseAdditionTextBox = wx.BoxSizer( wx.VERTICAL )

		self.NoiseAdditionText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"噪声攻击（高斯噪声）\n鲁棒性的测试", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoiseAdditionText.Wrap( -1 )

		NoiseAdditionTextBox.Add( self.NoiseAdditionText, 0, wx.ALL, 5 )


		NoiseAdditionBox3.Add( NoiseAdditionTextBox, 2, wx.EXPAND, 5 )

		NoiseAdditionBox = wx.BoxSizer( wx.HORIZONTAL )

		OriImage11 = wx.BoxSizer( wx.VERTICAL )

		self.OriImage21 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriImage11.Add( self.OriImage21, 1, wx.ALL, 5 )


		NoiseAdditionBox.Add( OriImage11, 1, wx.EXPAND, 5 )

		EncryptImage11 = wx.BoxSizer( wx.VERTICAL )

		self.EncryptImage21 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EncryptImage11.Add( self.EncryptImage21, 1, wx.ALL, 5 )


		NoiseAdditionBox.Add( EncryptImage11, 1, wx.EXPAND, 5 )


		NoiseAdditionBox3.Add( NoiseAdditionBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( NoiseAdditionBox3, 1, wx.EXPAND, 5 )

		NoiseAdditionBox1 = wx.BoxSizer( wx.HORIZONTAL )

		NoiseAdditionTextBox1 = wx.BoxSizer( wx.VERTICAL )

		self.NoiseAdditionText1 = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"噪声攻击（椒盐噪声）\n鲁棒性的测试", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoiseAdditionText1.Wrap( -1 )

		NoiseAdditionTextBox1.Add( self.NoiseAdditionText1, 0, wx.ALL, 5 )


		NoiseAdditionBox1.Add( NoiseAdditionTextBox1, 2, wx.EXPAND, 5 )

		NoiseAdditionBox2 = wx.BoxSizer( wx.HORIZONTAL )

		OriImage111 = wx.BoxSizer( wx.VERTICAL )

		self.OriImage211 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriImage111.Add( self.OriImage211, 1, wx.ALL, 5 )


		NoiseAdditionBox2.Add( OriImage111, 1, wx.EXPAND, 5 )

		EncryptImage111 = wx.BoxSizer( wx.VERTICAL )

		self.EncryptImage211 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EncryptImage111.Add( self.EncryptImage211, 1, wx.ALL, 5 )


		NoiseAdditionBox2.Add( EncryptImage111, 1, wx.EXPAND, 5 )


		NoiseAdditionBox1.Add( NoiseAdditionBox2, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( NoiseAdditionBox1, 1, wx.EXPAND, 5 )

		BlockingAttackBox1 = wx.BoxSizer( wx.HORIZONTAL )

		BlockingAttackTextBox1 = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackTextBox = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"阻塞攻击\n图像的一部分可能丢失，提出的算法必须能够以适当\n的方式处理有损图像的解码。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BlockingAttackTextBox.Wrap( -1 )

		BlockingAttackTextBox1.Add( self.BlockingAttackTextBox, 0, wx.ALL, 5 )


		BlockingAttackBox1.Add( BlockingAttackTextBox1, 2, wx.EXPAND, 5 )

		BlockingAttackBox = wx.BoxSizer( wx.HORIZONTAL )

		BlockingAttackEnyBox = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackEny = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		BlockingAttackEnyBox.Add( self.BlockingAttackEny, 1, wx.ALL, 5 )


		BlockingAttackBox.Add( BlockingAttackEnyBox, 1, wx.EXPAND, 5 )

		BlockingAttackDecBox = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackDec = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		BlockingAttackDecBox.Add( self.BlockingAttackDec, 1, wx.ALL, 5 )


		BlockingAttackBox.Add( BlockingAttackDecBox, 1, wx.EXPAND, 5 )


		BlockingAttackBox1.Add( BlockingAttackBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( BlockingAttackBox1, 1, wx.EXPAND, 5 )

		PSNRBox = wx.BoxSizer( wx.HORIZONTAL )

		PSNRTextBox = wx.BoxSizer( wx.HORIZONTAL )

		self.PSNRText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"裁剪攻击\n峰值信噪比\n峰值信噪比主要考察对应像素点之间的误差。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PSNRText.Wrap( -1 )

		PSNRTextBox.Add( self.PSNRText, 0, wx.ALL, 5 )


		PSNRBox.Add( PSNRTextBox, 2, wx.EXPAND, 5 )

		PSNRGridBox = wx.BoxSizer( wx.HORIZONTAL )

		self.PSNRGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.PSNRGrid.CreateGrid( 5, 5 )
		self.PSNRGrid.EnableEditing( True )
		self.PSNRGrid.EnableGridLines( True )
		self.PSNRGrid.EnableDragGridSize( False )
		self.PSNRGrid.SetMargins( 0, 0 )

		# Columns
		self.PSNRGrid.EnableDragColMove( False )
		self.PSNRGrid.EnableDragColSize( True )
		self.PSNRGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.PSNRGrid.EnableDragRowSize( True )
		self.PSNRGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.PSNRGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		PSNRGridBox.Add( self.PSNRGrid, 0, wx.ALL, 5 )


		PSNRBox.Add( PSNRGridBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( PSNRBox, 1, wx.EXPAND, 5 )


		self.Analysis_scrolledWindow3.SetSizer( AnalysisBox )
		self.Analysis_scrolledWindow3.Layout()
		AnalysisBox.Fit( self.Analysis_scrolledWindow3 )
		LayerAnalysisImage.Add( self.Analysis_scrolledWindow3, 1, wx.ALL|wx.EXPAND, 5 )


		LayerAnalysis.Add( LayerAnalysisImage, 8, wx.EXPAND, 5 )


		LayRoot.Add( LayerAnalysis, 6, wx.EXPAND, 5 )


		self.SetSizer( LayRoot )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.FileChoose.Bind(wx.EVT_BUTTON, self.getImageEvents)
		self.Encrypt_button.Bind(wx.EVT_BUTTON, self.EncryptImageEvents)
		self.Decryption_button.Bind(wx.EVT_BUTTON, self.DecryptImageEvents)

	def __del__(self):
		pass


	def getImageEvents(self, event):
		path = self.m_genericDirCtrl2.GetFilePath()
		if path:
			# image = wx.Image('D:/Image-Encryption-Decryption-main/Images/4.jpg', wx.BITMAP_TYPE_JPEG)
			image = wx.Image(path, wx.BITMAP_TYPE_ANY)
			# temp = image.ConvertToBitmap()
			# bitmap2Width=self.m_bitmap2.GetSize()
			# bitmap2Height = self.m_bitmap2.GetMaxHeight()
			self.PhotoMaxSize = 250

			W = image.GetWidth()
			H = image.GetHeight()
			if W > H:
				NewW = self.PhotoMaxSize
				NewH = self.PhotoMaxSize * H / W
			else:
				NewH = self.PhotoMaxSize
				NewW = self.PhotoMaxSize * W / H
			img = image.Scale(NewW, NewH)
			# screen_width, screen_height = screen.GetSize()
			# print(bitmap2Width)
			# print(bitmap2Height)
			# bgm = image.Scale(int(screen_width*3/15), screen_height*3/15)
			temp = img.ConvertToBitmap()
			size = temp.GetWidth(), temp.GetHeight()
			self.m_bitmap2.SetBitmap(wx.BitmapFromImage(temp))

			# self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
			self.m_bitmap2.Refresh()
			# bSizer29.Add(self.m_bitmap2, 0, wx.ALL, 5)
			# self.frame.Show()
			# self.SetTopWindow(self.frame)
			# return True
			print(path)
		else:
			wx.MessageBox('未选中文件', '失败', wx.OK | wx.ICON_ERROR)
		event.Skip()

	def EncryptImageEvents(self, event):
		global encrypted_image, iterations
		path = self.m_genericDirCtrl2.GetFilePath()
		# print(x)
		image_input = cv2.imread(path, 0)  # 'C:/Users/aakas/Documents/flower.jpg'

		# 加密图像
		iterations = 10
		encrypted_image = arnold_encrypt(image_input, iterations)
		# print(image_input)
		# (imageWidth1, imageHeight1) = image_input.shape
		# image_inputFloat = image_input.astype(float) / 255.0
		# print(image_inputFloat)

		# mu, sigma = 0, 0.1  # mean and standard deviation
		# global key

		# key = np.random.normal(mu, sigma, (imageWidth1, imageHeight1)) + np.finfo(float).eps
		# print(key)
		# image_encrypted = image_inputFloat / key

		# EnyImage=cv2.imwrite('image_encrypted1.jpg', image_encrypted * 255)
		# print(image_encrypted * 255)
		path = 'D:/Image-Encryption-Decryption-main/EnyImg/Encryption.jpg'
		cv2.imwrite(path, encrypted_image)
		imge1 = wx.Image(path, wx.BITMAP_TYPE_JPEG)

		self.PhotoMaxSize = 250
		W = imge1.GetWidth()
		H = imge1.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = imge1.Scale(NewW, NewH)
		temp = img.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		self.m_bitmap3.SetBitmap(wx.BitmapFromImage(temp))

		# self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
		self.m_bitmap3.Refresh()

		event.Skip()

	def DecryptImageEvents(self, event):
		# path='D:/Image-Encryption-Decryption-main/image_encrypted1.jpg'
		# path = self.m_genericDirCtrl2.GetFilePath()
		# image_input = cv2.imread(path, 0)
		# (imageWidth1, imageHeight1) = image_input.shape
		# image_inputFloat = image_input.astype(float) / 255.0
		# print(image_input.astype(float))

		# print(key)
		# image_output = image_inputFloat * key
		# image_output *= 255.0
		# cv2.imwrite('image_output1.jpg', image_output)

		# imge1 = wx.Image('image_output1.jpg')

		# 解密图像
		decrypted_image = arnold_decrypt(encrypted_image, iterations)

		path = 'D:/Image-Encryption-Decryption-main/EnyImg/Decryption.jpg'
		cv2.imwrite(path, decrypted_image)
		imge1 = wx.Image(path, wx.BITMAP_TYPE_JPEG)

		self.PhotoMaxSize = 250
		W = imge1.GetWidth()
		H = imge1.GetHeight()
		if W > H:
			NewW = self.PhotoMaxSize
			NewH = self.PhotoMaxSize * H / W
		else:
			NewH = self.PhotoMaxSize
			NewW = self.PhotoMaxSize * W / H
		img = imge1.Scale(NewW, NewH)
		temp = img.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		self.m_bitmap4.SetBitmap(wx.BitmapFromImage(temp))

		# self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
		self.m_bitmap4.Refresh()

		event.Skip()


