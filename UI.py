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
import os

###########################################################################
## Class window
###########################################################################
from PIL import Image

from EncryptionDecryptionFunc import arnold_encrypt, PilImage2WxImage, arnold_decrypt, logistic_decrypt_image, \
	logistic_encrypt_image
#从EncryptionDecryptionFunc模块中导入了几个函数
###########################################################################
## Class window
###########################################################################

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

###########################################################################
## Class window
###########################################################################
from EncryptionTest.HenonEncryption import HenonEncryption, HenonDecryption
from UIEvent import ReSizeImage
from performanceEvaluation.BlockingAttack import occlusion
from performanceEvaluation.Correlation import correlation
from performanceEvaluation.Encryption_Quality import EQ
from performanceEvaluation.Histogram import hist
from performanceEvaluation.Information_Entropy import entropy
from performanceEvaluation.NoiseAddition import gauss_noise, salt_and_pepper_noise
from performanceEvaluation.PSNR import PSNR
from performanceEvaluation.Randomness import GVD
from performanceEvaluation.SensitivityAnaly import NPCR, UACI
#从不同的模块中导入了多个函数和类

# 全局变量用于存储反向恢复所需信息
original_blur_amp = None
original_phase = None
original_spec_res_min = None
original_spec_res_max = None
saliency_image = None
encrypted_image = None
decrypted_image = None
iterations = None
original_image = None  # 添加变量存储原始图像

class window ( wx.Frame ):#类是使用wxPython库创建的窗口

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片加解密程序", pos = wx.DefaultPosition, size = wx.Size( 1058,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )#这是对父类wx.Frame的初始化方法的调用，设置窗口的标题、位置、大小和样式。

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )#这是对父类wx.Frame的初始化方法的调用，设置窗口的标题、位置、大小和样式。

		LayRoot = wx.BoxSizer( wx.VERTICAL )

		LayMain = wx.BoxSizer( wx.HORIZONTAL )

		LayFile = wx.BoxSizer( wx.HORIZONTAL )

		LayFileBrower = wx.BoxSizer( wx.VERTICAL )

		self.m_genericDirCtrl2 = wx.GenericDirCtrl( self, wx.ID_ANY, u"D:/Image-Encryption-Decryption-main/OriImg", wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl2.ShowHidden( False )
		LayFileBrower.Add( self.m_genericDirCtrl2, 1, wx.EXPAND |wx.ALL, 5 )

		# 添加加载提示文本
		self.loading_text = wx.StaticText(self, wx.ID_ANY, u"正在加载中，请勿操作...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER)
		self.loading_text.SetForegroundColour(wx.RED)
		self.loading_text.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
		self.loading_text.Hide()  # 初始时隐藏
		LayFileBrower.Add(self.loading_text, 0, wx.ALL|wx.ALIGN_CENTER, 5)

		LayFile.Add( LayFileBrower, 7, wx.EXPAND, 5 )

		LayFileFunc = wx.BoxSizer( wx.VERTICAL )

		self.FileChoose = wx.Button( self, wx.ID_ANY, u"选择图片文件", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.FileChoose, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

		self.Algorithm = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ['Arnold算法', 'Logistic算法', 'Henon算法'])
		self.Algorithm.SetSelection(0)
		LayFileFunc.Add(self.Algorithm, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5)

		self.Saliency_button = wx.Button( self, wx.ID_ANY, u"提取显著性", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.Saliency_button, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

		self.Encrypt_button = wx.Button( self, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.Encrypt_button, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

		self.Decryption_button = wx.Button( self, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.Decryption_button, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

		self.RestoreFeaturesButton = wx.Button( self, wx.ID_ANY, u"恢复特征值", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayFileFunc.Add( self.RestoreFeaturesButton, 1, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

		LayFile.Add( LayFileFunc, 3, wx.EXPAND|wx.FIXED_MINSIZE, 2 )


		LayMain.Add( LayFile, 3, wx.EXPAND, 5 )

		LayerImage = wx.BoxSizer( wx.HORIZONTAL )

		OriImageBox = wx.BoxSizer( wx.VERTICAL )

		self.OriImageLabel = wx.StaticText( self, wx.ID_ANY, u"原始图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OriImageLabel.Wrap( -1 )
		OriImageBox.Add( self.OriImageLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.OriImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		OriImageBox.Add( self.OriImage, 1, wx.ALL, 5 )


		LayerImage.Add( OriImageBox, 1, wx.EXPAND, 5 )

		SaliencyImageBox = wx.BoxSizer( wx.VERTICAL )

		self.SaliencyImageLabel = wx.StaticText( self, wx.ID_ANY, u"显著性图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SaliencyImageLabel.Wrap( -1 )
		SaliencyImageBox.Add( self.SaliencyImageLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.SaliencyImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		SaliencyImageBox.Add( self.SaliencyImage, 1, wx.ALL, 5 )


		LayerImage.Add( SaliencyImageBox, 1, wx.EXPAND, 5 )

		EncryptImageBox = wx.BoxSizer( wx.VERTICAL )

		self.EncryptImageLabel = wx.StaticText( self, wx.ID_ANY, u"加密图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptImageLabel.Wrap( -1 )
		EncryptImageBox.Add( self.EncryptImageLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.EncryptImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		EncryptImageBox.Add( self.EncryptImage, 1, wx.ALL, 5 )


		LayerImage.Add( EncryptImageBox, 1, wx.EXPAND, 5 )

		DecryptImage = wx.BoxSizer( wx.VERTICAL )

		self.DecryptImageLabel = wx.StaticText( self, wx.ID_ANY, u"解密图像", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DecryptImageLabel.Wrap( -1 )
		DecryptImage.Add( self.DecryptImageLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.DecryptImage = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		DecryptImage.Add( self.DecryptImage, 1, wx.ALL, 5 )


		LayerImage.Add( DecryptImage, 1, wx.EXPAND, 5 )


		LayMain.Add( LayerImage, 7, wx.EXPAND, 5 )


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
		self.SensitivityAnalyLabelBoxText.Wrap( -1 )#使用wxPython库来创建一个图形用户界面（GUI）中的一部分。具体来说，它在一个名为Analysis_scrolledWindow3的滚动窗口内创建了一个静态文本控件。

		self.SensitivityAnalyLabelBoxText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		SensitivityAnalyLabelBox.Add( self.SensitivityAnalyLabelBoxText, 0, wx.EXPAND, 5 )


		SensitivityAnalyBox.Add( SensitivityAnalyLabelBox, 2, wx.EXPAND, 5 )

		SensitivityAnalyGrid1 = wx.BoxSizer( wx.HORIZONTAL )

		self.SensitivityAnalyGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.SensitivityAnalyGrid.CreateGrid( 3, 2 )
		self.SensitivityAnalyGrid.SetColLabelValue(0,'NPCR');
		self.SensitivityAnalyGrid.SetColLabelValue(1,'UACI');
		self.SensitivityAnalyGrid.SetRowLabelValue(0, 'R');
		self.SensitivityAnalyGrid.SetRowLabelValue(1, 'G');
		self.SensitivityAnalyGrid.SetRowLabelValue(2,'B');

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
		self.HistogramText.Wrap( -1 )#使用wxPython库来创建一个GUI应用程序的部分。你正在创建一个分析部分，其中包含一些按钮、文本框和直方图

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
		self.EnyHistogramText.Wrap( -1 )#在wxPython GUI 中创建一个静态文本控件，创建了一个StaticText对象，用于在GUI中显示文本

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
		self.OriCorrelationText.Wrap( -1 )#创建一个静态文本控件，显示"相关性分析

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
		self.EnyCorrelationText.Wrap( -1 )#创建一个静态文本控件，显示"相关性分析

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
		self.Information_EntropyText.Wrap( -1 )#self.Information_EntropyText：创建一个静态文本控件，显示"信息熵分析"。

		Information_EntropyTextBox.Add( self.Information_EntropyText, 0, wx.ALL, 5 )


		Information_EntropyBox.Add( Information_EntropyTextBox, 2, wx.EXPAND, 5 )

		Information_EntropyGridBox = wx.BoxSizer( wx.HORIZONTAL )

		self.Information_EntropyGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Information_EntropyGrid.CreateGrid( 3, 3 )

		self.Information_EntropyGrid.SetColLabelValue(0, '原Lena图像');
		self.Information_EntropyGrid.SetColLabelValue(1, '加密图像1');
		self.Information_EntropyGrid.SetColLabelValue(2, '加密图像2');
		self.Information_EntropyGrid.SetRowLabelValue(0, 'R');
		self.Information_EntropyGrid.SetRowLabelValue(1, 'G');
		self.Information_EntropyGrid.SetRowLabelValue(2, 'B');

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
		self.RandomnessText.Wrap( -1 )#创建了一个静态文本（wx.StaticText）控件，用于在窗口中显示一段文本。设置了文本的自动换行模式。-1表示启用自动换行，但不允许超过最大宽度。这样做的目的是确保文本不会超出其容器的大小，并在需要时自动换行。

		RandomnessTextBox.Add( self.RandomnessText, 0, wx.ALL, 5 )


		RandomnessBox.Add( RandomnessTextBox, 2, wx.EXPAND, 5 )

		RandomnessGrid1 = wx.BoxSizer( wx.HORIZONTAL )

		self.RandomnessGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.RandomnessGrid.CreateGrid( 3, 2 )

		self.RandomnessGrid.SetColLabelValue(0, '加密图像1');
		self.RandomnessGrid.SetColLabelValue(1, '加密图像2');
		self.RandomnessGrid.SetRowLabelValue(0, 'R');
		self.RandomnessGrid.SetRowLabelValue(1, 'G');
		self.RandomnessGrid.SetRowLabelValue(2, 'B');

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
		self.EncryptionQualityGrid.CreateGrid( 3, 2 )

		self.EncryptionQualityGrid.SetColLabelValue(0, '加密图像1');
		self.EncryptionQualityGrid.SetColLabelValue(1, '加密图像2');
		self.EncryptionQualityGrid.SetRowLabelValue(0, 'R');
		self.EncryptionQualityGrid.SetRowLabelValue(1, 'G');
		self.EncryptionQualityGrid.SetRowLabelValue(2, 'B');

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

		NoiseAdditionBox1 = wx.BoxSizer( wx.HORIZONTAL )

		NoiseAdditionTextBox = wx.BoxSizer( wx.VERTICAL )

		self.NoiseAdditionText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"噪声攻击（高斯噪声）\n鲁棒性的测试", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoiseAdditionText.Wrap( -1 )#用Python的wxPython库创建另一个静态文本（wx.StaticText）控件的部分。创建了一个新的wx.StaticText控件并将其赋值给self.NoiseAdditionText。

		NoiseAdditionTextBox.Add( self.NoiseAdditionText, 0, wx.ALL, 5 )


		NoiseAdditionBox1.Add( NoiseAdditionTextBox, 2, wx.EXPAND, 5 )

		NoiseAdditionBox = wx.BoxSizer( wx.HORIZONTAL )

		NoiseOriImage = wx.BoxSizer( wx.VERTICAL )

		self.NoiseOriImage = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		NoiseOriImage.Add( self.NoiseOriImage, 1, wx.ALL, 5 )


		NoiseAdditionBox.Add( NoiseOriImage, 1, wx.EXPAND, 5 )

		NoiseEncryptImage = wx.BoxSizer( wx.VERTICAL )

		self.NoiseEncryptImage = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		NoiseEncryptImage.Add( self.NoiseEncryptImage, 1, wx.ALL, 5 )


		NoiseAdditionBox.Add( NoiseEncryptImage, 1, wx.EXPAND, 5 )


		NoiseAdditionBox1.Add( NoiseAdditionBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( NoiseAdditionBox1, 1, wx.EXPAND, 5 )

		NoiseAdditionBox2 = wx.BoxSizer( wx.HORIZONTAL )

		NoiseAdditionTextBox1 = wx.BoxSizer( wx.VERTICAL )

		self.NoiseAdditionText1 = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"噪声攻击（椒盐噪声）\n鲁棒性的测试", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoiseAdditionText1.Wrap( -1 )

		NoiseAdditionTextBox1.Add( self.NoiseAdditionText1, 0, wx.ALL, 5 )


		NoiseAdditionBox2.Add( NoiseAdditionTextBox1, 2, wx.EXPAND, 5 )

		NoiseAdditionBox1 = wx.BoxSizer( wx.HORIZONTAL )

		NoiseOriImage1 = wx.BoxSizer( wx.VERTICAL )

		self.NoiseOriImage2 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		NoiseOriImage1.Add( self.NoiseOriImage2, 1, wx.ALL, 5 )


		NoiseAdditionBox1.Add( NoiseOriImage1, 1, wx.EXPAND, 5 )

		NoiseEncryptImage1 = wx.BoxSizer( wx.VERTICAL )

		self.NoiseEncryptImage2 = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		NoiseEncryptImage1.Add( self.NoiseEncryptImage2, 1, wx.ALL, 5 )


		NoiseAdditionBox1.Add( NoiseEncryptImage1, 1, wx.EXPAND, 5 )


		NoiseAdditionBox2.Add( NoiseAdditionBox1, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( NoiseAdditionBox2, 1, wx.EXPAND, 5 )

		BlockingAttackBox = wx.BoxSizer( wx.HORIZONTAL )

		BlockingAttackTextBox = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"阻塞攻击\n在互联网上的通信过程中，图像的一部分可能丢失，\n提出的算法必须能够以适当的方式处理有损图像的\n解码。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BlockingAttackText.Wrap( -1 )

		BlockingAttackTextBox.Add( self.BlockingAttackText, 0, wx.ALL, 5 )


		BlockingAttackBox.Add( BlockingAttackTextBox, 2, wx.EXPAND, 5 )

		BlockingAttackImgBox = wx.BoxSizer( wx.HORIZONTAL )

		BlockingAttackOriImageBox = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackOriImage = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		BlockingAttackOriImageBox.Add( self.BlockingAttackOriImage, 1, wx.ALL, 5 )


		BlockingAttackImgBox.Add( BlockingAttackOriImageBox, 1, wx.EXPAND, 5 )

		BlockingAttackEnyImageBox = wx.BoxSizer( wx.VERTICAL )

		self.BlockingAttackEnpImage = wx.StaticBitmap( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		BlockingAttackEnyImageBox.Add( self.BlockingAttackEnpImage, 1, wx.ALL, 5 )


		BlockingAttackImgBox.Add( BlockingAttackEnyImageBox, 1, wx.EXPAND, 5 )


		BlockingAttackBox.Add( BlockingAttackImgBox, 8, wx.EXPAND, 5 )


		AnalysisBox.Add( BlockingAttackBox, 1, wx.EXPAND, 5 )

		PSNRBox = wx.BoxSizer( wx.HORIZONTAL )

		PSNRTextBox = wx.BoxSizer( wx.HORIZONTAL )

		self.PSNRText = wx.StaticText( self.Analysis_scrolledWindow3, wx.ID_ANY, u"裁剪攻击\n峰值信噪比\n峰值信噪比主要考察对应像素点之间的误差。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PSNRText.Wrap( -1 )

		PSNRTextBox.Add( self.PSNRText, 0, wx.ALL, 5 )


		PSNRBox.Add( PSNRTextBox, 2, wx.EXPAND, 5 )

		PSNRGridBox = wx.BoxSizer( wx.HORIZONTAL )

		self.PSNRGrid = wx.grid.Grid( self.Analysis_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.PSNRGrid.CreateGrid( 3, 2 )

		self.PSNRGrid.SetColLabelValue(0, '加密图像1');
		self.PSNRGrid.SetColLabelValue(1, '加密图像2');
		self.PSNRGrid.SetRowLabelValue(0, 'R');
		self.PSNRGrid.SetRowLabelValue(1, 'G');
		self.PSNRGrid.SetRowLabelValue(2, 'B');


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
		self.StartAnalysis.Bind(wx.EVT_BUTTON, self.StartAnalysisEvents)
		self.FileChoose.Bind( wx.EVT_BUTTON, self.getImageEvents )
		self.Encrypt_button.Bind( wx.EVT_BUTTON, self.EncryptImageEvents )
		self.Decryption_button.Bind( wx.EVT_BUTTON, self.DecryptImageEvents )
		self.Saliency_button.Bind( wx.EVT_BUTTON, self.SaliencyExtractEvents )
		self.RestoreFeaturesButton.Bind( wx.EVT_BUTTON, self.RestoreFeaturesEvents )

	def __del__( self ):
		pass


	def getImageEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		path = self.m_genericDirCtrl2.GetFilePath()
		if path:
			image = wx.Image(path, wx.BITMAP_TYPE_ANY)
			temp = ReSizeImage(image,250)
			self.OriImage.SetBitmap(wx.BitmapFromImage(temp))
			self.OriImage.Refresh()
			print(path)
		else:
			wx.MessageBox('未选中文件', '失败', wx.OK | wx.ICON_ERROR)
		
		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()



	def EncryptImageEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		global encrypted_image, iterations
		
		# 检查是否已执行显著性提取
		try:
			global saliency_image
			if saliency_image is None:
				
				wx.MessageBox('请先提取显著性', '操作顺序错误', wx.OK | wx.ICON_ERROR)
				self.loading_text.Hide()
				self.loading_text.Refresh()
				event.Skip()
				return
		except NameError:
			wx.MessageBox('请先提取显著性', '操作顺序错误', wx.OK | wx.ICON_ERROR)
			self.loading_text.Hide()
			self.loading_text.Refresh()
			event.Skip()
			return
				
		# 使用显著性图像作为输入
		image_input = saliency_image
		save_path = 'D:/Image-Encryption-Decryption-main/EnyImg/Encryption.png'

		al = self.Algorithm.GetString(self.Algorithm.GetSelection())
		if al == 'Arnold算法':
			iterations = 10
			encrypted_image = arnold_encrypt(image_input, iterations)
			cv2.imwrite(save_path, encrypted_image)

		elif al == 'Logistic算法':
			r = 3.9
			num_iterations = 100
			encrypted_image = logistic_encrypt_image(image_input, r)
			cv2.imwrite(save_path, encrypted_image)

		#decrypted_image = logistic_map_encrypt(encrypted_image, r)
		elif al == 'Henon算法':
			# 保存显著性图像为临时文件，因为Henon算法需要文件路径作为输入
			temp_path = 'D:/Image-Encryption-Decryption-main/restore/temp_saliency.png'
			cv2.imwrite(temp_path, image_input)
			key = (0.1, 0.1)
			HEncrypt = HenonEncryption(temp_path, key)
			HEncrypt.save(save_path, "PNG")
			encrypted_image = cv2.imread(save_path)

		imge1 = wx.Image(save_path)
		temp = ReSizeImage(imge1, 250)
		self.EncryptImage.SetBitmap(wx.BitmapFromImage(temp))
		self.EncryptImage.Refresh()

		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()

	def DecryptImageEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		global decrypted_image, encrypted_image, iterations
		save_path = 'D:/Image-Encryption-Decryption-main/EnyImg/Decryption.png'
		
		al = self.Algorithm.GetString(self.Algorithm.GetSelection())
		if al == 'Arnold算法':
			decrypted_image = arnold_decrypt(encrypted_image, iterations)
			cv2.imwrite(save_path, decrypted_image)
		elif al == 'Logistic算法':
			r = 3.9
			decrypted_image = logistic_decrypt_image(encrypted_image, r)
			cv2.imwrite(save_path, decrypted_image)
		elif al == 'Henon算法':
			key = (0.1, 0.1)
			HDecrypt = HenonDecryption('D:/Image-Encryption-Decryption-main/EnyImg/Encryption.png', key)
			HDecrypt.save(save_path, "PNG")
			decrypted_image = cv2.imread(save_path)

		imge1 = wx.Image(save_path)
		temp = ReSizeImage(imge1, 250)
		self.DecryptImage.SetBitmap(wx.BitmapFromImage(temp))
		self.DecryptImage.Refresh()

		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()

	def StartAnalysisEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		try:
			# 创建必要的目录
			analysis_dir = 'D:/Image-Encryption-Decryption-main/AnalysisImg'
			eny_dir = 'D:/Image-Encryption-Decryption-main/EnyImg'
			os.makedirs(analysis_dir, exist_ok=True)
			os.makedirs(eny_dir, exist_ok=True)
			
			# 获取当前处理的图像路径
			original_path = self.m_genericDirCtrl2.GetFilePath()
			encrypted_path = 'D:/Image-Encryption-Decryption-main/EnyImg/Encryption.png'
			decrypted_path = 'D:/Image-Encryption-Decryption-main/EnyImg/Decryption.png'
			
			if not os.path.exists(encrypted_path) or not os.path.exists(decrypted_path):
				wx.MessageBox('请先完成加密和解密流程', '操作顺序错误', wx.OK | wx.ICON_ERROR)
				self.loading_text.Hide()
				self.loading_text.Refresh()
				event.Skip()
				return
			
			# 1. 计算NPCR和UACI
			R_npcr, G_npcr, B_npcr = NPCR(encrypted_path, decrypted_path)
			R_uaci, G_uaci, B_uaci = UACI(encrypted_path, decrypted_path)
			
			# 更新灵敏度分析表格
			self.SensitivityAnalyGrid.SetCellValue(0, 0, '{:.4%}'.format(R_npcr))
			self.SensitivityAnalyGrid.SetCellValue(1, 0, '{:.4%}'.format(G_npcr))
			self.SensitivityAnalyGrid.SetCellValue(2, 0, '{:.4%}'.format(B_npcr))
			self.SensitivityAnalyGrid.SetCellValue(0, 1, '{:.4%}'.format(R_uaci))
			self.SensitivityAnalyGrid.SetCellValue(1, 1, '{:.4%}'.format(G_uaci))
			self.SensitivityAnalyGrid.SetCellValue(2, 1, '{:.4%}'.format(B_uaci))
			
			# 2. 计算直方图
			ori_hist_g, ori_hist_b, ori_hist_gr, ori_hist_r = hist(original_path)
			eny_hist_g, eny_hist_b, eny_hist_gr, eny_hist_r = hist(encrypted_path)
			
			# 保存直方图
			cv2.imwrite(os.path.join(analysis_dir, 'OriHis.png'), ori_hist_g)
			cv2.imwrite(os.path.join(analysis_dir, 'OriHisB.png'), ori_hist_b)
			cv2.imwrite(os.path.join(analysis_dir, 'OriHisG.png'), ori_hist_gr)
			cv2.imwrite(os.path.join(analysis_dir, 'OriHisR.png'), ori_hist_r)
			
			# 显示直方图
			self.OriHistogramG.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriHis.png')), 200)))
			self.OriHistogramB.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriHisB.png')), 200)))
			self.OriHistogramGn.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriHisG.png')), 200)))
			self.OriHistogramR.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriHisR.png')), 200)))
			
			self.EnyHistogramG.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyHis.png')), 200)))
			self.EnyHistogramB.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyHisB.png')), 200)))
			self.EnyHistogramGn.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyHisG.png')), 200)))
			self.EnyHistogramR.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyHisR.png')), 200)))
			
			# 3. 计算相关性
			R_Rxy, G_Rxy, B_Rxy = correlation(original_path)
			R_Rxy_eny, G_Rxy_eny, B_Rxy_eny = correlation(encrypted_path)
			
			# 保存相关性图
			cv2.imwrite(os.path.join(analysis_dir, 'OriCor.png'), R_Rxy)
			cv2.imwrite(os.path.join(analysis_dir, 'OriCorB.png'), B_Rxy)
			cv2.imwrite(os.path.join(analysis_dir, 'OriCorG.png'), G_Rxy)
			cv2.imwrite(os.path.join(analysis_dir, 'OriCorR.png'), R_Rxy)
			
			cv2.imwrite(os.path.join(analysis_dir, 'EnyCor.png'), R_Rxy_eny)
			cv2.imwrite(os.path.join(analysis_dir, 'EnyCorB.png'), B_Rxy_eny)
			cv2.imwrite(os.path.join(analysis_dir, 'EnyCorG.png'), G_Rxy_eny)
			cv2.imwrite(os.path.join(analysis_dir, 'EnyCorR.png'), R_Rxy_eny)
			
			# 显示相关性图
			self.OriCorrelationG.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriCor.png')), 200)))
			self.OriCorrelationB.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriCorB.png')), 200)))
			self.OriCorrelationGn.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriCorG.png')), 200)))
			self.OriCorrelationR.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'OriCorR.png')), 200)))
			
			self.EnyCorrelationBoxG.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyCor.png')), 200)))
			self.EnyCorrelationB.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyCorB.png')), 200)))
			self.EnyCorrelationGn.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyCorG.png')), 200)))
			self.EnyCorrelationR.SetBitmap(wx.Bitmap(ReSizeImage(wx.Image(os.path.join(analysis_dir, 'EnyCorR.png')), 200)))
			
			# 4. 计算信息熵
			R_entropy, G_entropy, B_entropy = entropy(original_path)
			R_entropy_eny, G_entropy_eny, B_entropy_eny = entropy(encrypted_path)
			
			# 更新信息熵表格
			self.Information_EntropyGrid.SetCellValue(0, 0, '{:.4f}'.format(R_entropy))
			self.Information_EntropyGrid.SetCellValue(1, 0, '{:.4f}'.format(G_entropy))
			self.Information_EntropyGrid.SetCellValue(2, 0, '{:.4f}'.format(B_entropy))
			self.Information_EntropyGrid.SetCellValue(0, 1, '{:.4f}'.format(R_entropy_eny))
			self.Information_EntropyGrid.SetCellValue(1, 1, '{:.4f}'.format(G_entropy_eny))
			self.Information_EntropyGrid.SetCellValue(2, 1, '{:.4f}'.format(B_entropy_eny))
			
			# 5. 计算随机性
			R_gvd, G_gvd, B_gvd = GVD(original_path, encrypted_path)
			
			# 更新随机性表格
			self.RandomnessGrid.SetCellValue(0, 0, '{:.4f}'.format(R_gvd))
			self.RandomnessGrid.SetCellValue(1, 0, '{:.4f}'.format(G_gvd))
			self.RandomnessGrid.SetCellValue(2, 0, '{:.4f}'.format(B_gvd))
			
			# 6. 计算加密质量
			R_EQ, G_EQ, B_EQ = EQ(original_path, encrypted_path)
			
			# 更新加密质量表格
			self.EncryptionQualityGrid.SetCellValue(0, 0, '{:.0f}'.format(R_EQ))
			self.EncryptionQualityGrid.SetCellValue(1, 0, '{:.0f}'.format(G_EQ))
			self.EncryptionQualityGrid.SetCellValue(2, 0, '{:.0f}'.format(B_EQ))
			
			# 7. 噪声攻击测试
			im = cv2.imread(encrypted_path)
			gauss_img = gauss_noise(im, mean=0, var=0.0005)
			salt_img = salt_and_pepper_noise(im, proportion=0.05)
			
			cv2.imwrite(os.path.join(eny_dir, 'gauss_img.png'), gauss_img)
			cv2.imwrite(os.path.join(eny_dir, 'salt_img.png'), salt_img)
			
			gauss_img = wx.Image(os.path.join(eny_dir, 'gauss_img.png'))
			salt_img = wx.Image(os.path.join(eny_dir, 'salt_img.png'))
			
			self.NoiseOriImage.SetBitmap(wx.Bitmap(ReSizeImage(gauss_img, 200)))
			self.NoiseOriImage2.SetBitmap(wx.Bitmap(ReSizeImage(salt_img, 200)))
			
			# 8. 阻塞攻击测试
			lossy_encrypt = occlusion(encrypted_path)
			cv2.imwrite(os.path.join(eny_dir, 'lossy_encrypt.png'), lossy_encrypt)
			
			lossy_img = wx.Image(os.path.join(eny_dir, 'lossy_encrypt.png'))
			self.BlockingAttackOriImage.SetBitmap(wx.Bitmap(ReSizeImage(lossy_img, 200)))
			
			# 9. 计算PSNR
			R_psnr, G_psnr, B_psnr = PSNR(original_path, encrypted_path)
			
			# 更新PSNR表格
			self.PSNRGrid.SetCellValue(0, 0, '{:.4f}'.format(R_psnr))
			self.PSNRGrid.SetCellValue(1, 0, '{:.4f}'.format(G_psnr))
			self.PSNRGrid.SetCellValue(2, 0, '{:.4f}'.format(B_psnr))
			
			# 刷新所有显示
			self.SensitivityAnalyGrid.Refresh()
			self.Information_EntropyGrid.Refresh()
			self.RandomnessGrid.Refresh()
			self.EncryptionQualityGrid.Refresh()
			self.PSNRGrid.Refresh()
			
			self.OriHistogramG.Refresh()
			self.OriHistogramB.Refresh()
			self.OriHistogramGn.Refresh()
			self.OriHistogramR.Refresh()
			
			self.EnyHistogramG.Refresh()
			self.EnyHistogramB.Refresh()
			self.EnyHistogramGn.Refresh()
			self.EnyHistogramR.Refresh()
			
			self.OriCorrelationG.Refresh()
			self.OriCorrelationB.Refresh()
			self.OriCorrelationGn.Refresh()
			self.OriCorrelationR.Refresh()
			
			self.EnyCorrelationBoxG.Refresh()
			self.EnyCorrelationB.Refresh()
			self.EnyCorrelationGn.Refresh()
			self.EnyCorrelationR.Refresh()
			
			self.NoiseOriImage.Refresh()
			self.NoiseOriImage2.Refresh()
			self.BlockingAttackOriImage.Refresh()
			
		except Exception as e:
			wx.MessageBox(f'分析过程中出现错误: {str(e)}', '错误', wx.OK | wx.ICON_ERROR)
		
		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()

	def SaliencyExtractEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		# Get the selected image path
		path = self.m_genericDirCtrl2.GetFilePath()
		
		# Check if path is valid
		if not path:
			wx.MessageBox('未选中文件', '失败', wx.OK | wx.ICON_ERROR)
			self.loading_text.Hide()
			self.loading_text.Refresh()
			event.Skip()
			return
			
		# Create restore directory if it doesn't exist
		restore_dir = 'D:/Image-Encryption-Decryption-main/restore'
		if not os.path.exists(restore_dir):
			os.makedirs(restore_dir)
			
		# Read the image
		img = cv2.imread(path)
		
		# 保存原始图像和关键信息
		global original_image, original_info
		original_image = img.copy()
		
		# 计算并保存关键信息
		original_info = {
			# 1. 全局统计信息
			'global_mean': [float(x) for x in np.mean(img, axis=(0,1))],  # BGR三个通道的全局均值
			'global_std': [float(x) for x in np.std(img, axis=(0,1))],    # BGR三个通道的全局标准差
			'global_min': [float(x) for x in np.min(img, axis=(0,1))],    # BGR三个通道的全局最小值
			'global_max': [float(x) for x in np.max(img, axis=(0,1))],    # BGR三个通道的全局最大值
			
			# 2. 局部统计信息（16x16块）
			'local_stats': [],
			# 3. 边缘信息
			'edge_info': [],
			# 4. 纹理信息
			'texture_info': []
		}
		
		# 计算局部统计信息
		block_size = 16
		height, width = img.shape[:2]
		for y in range(0, height, block_size):
			for x in range(0, width, block_size):
				block = img[y:y+block_size, x:x+block_size]
				if block.shape[0] == block_size and block.shape[1] == block_size:
					# 计算每个通道的统计特征
					block_stats = []
					for channel in range(3):
						channel_data = block[:,:,channel]
						block_stats.extend([
							float(np.mean(channel_data)),
							float(np.std(channel_data)),
							float(np.min(channel_data)),
							float(np.max(channel_data))
						])
					original_info['local_stats'].append({
						'position': [int(y), int(x)],  # 确保位置是整数
						'stats': block_stats
					})
		
		# 计算边缘信息
		for channel in range(3):
			channel_data = img[:,:,channel]
			# 计算Sobel边缘
			sobelx = cv2.Sobel(channel_data, cv2.CV_64F, 1, 0, ksize=3)
			sobely = cv2.Sobel(channel_data, cv2.CV_64F, 0, 1, ksize=3)
			edge_magnitude = np.sqrt(sobelx**2 + sobely**2)
			original_info['edge_info'].append({
				'channel': int(channel),
				'mean_magnitude': float(np.mean(edge_magnitude)),
				'std_magnitude': float(np.std(edge_magnitude))
			})
		
		# 计算纹理信息
		for channel in range(3):
			channel_data = img[:,:,channel]
			# 计算局部二值模式(LBP)特征
			lbp = np.zeros_like(channel_data)
			for i in range(1, channel_data.shape[0]-1):
				for j in range(1, channel_data.shape[1]-1):
					center = channel_data[i,j]
					code = 0
					code |= (channel_data[i-1,j-1] >= center) << 7
					code |= (channel_data[i-1,j] >= center) << 6
					code |= (channel_data[i-1,j+1] >= center) << 5
					code |= (channel_data[i,j+1] >= center) << 4
					code |= (channel_data[i+1,j+1] >= center) << 3
					code |= (channel_data[i+1,j] >= center) << 2
					code |= (channel_data[i+1,j-1] >= center) << 1
					code |= (channel_data[i,j-1] >= center) << 0
					lbp[i,j] = code
			original_info['texture_info'].append({
				'channel': int(channel),
				'lbp_hist': [int(x) for x in np.histogram(lbp, bins=256, range=(0,256))[0]]
			})
		
		# 保存信息到文件
		import json
		with open(os.path.join(restore_dir, 'original_info.json'), 'w') as f:
			json.dump(original_info, f)
		
		# Convert to grayscale
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
		# Compute log Spectral
		fft = np.fft.fft2(gray)
		fshift = np.fft.fftshift(fft)
		LogAmp = np.log(np.abs(fshift))
		phase = np.angle(fshift)
		
		# Compute Spectral residual 
		global original_blur_amp, original_phase, original_spec_res_min, original_spec_res_max, saliency_image
		original_blur_amp = cv2.blur(LogAmp, (3, 3))
		original_phase = phase
		Spectral_res = LogAmp - original_blur_amp
		
		# 存储归一化前的范围
		original_spec_res_min = np.min(Spectral_res)
		original_spec_res_max = np.max(Spectral_res)
		
		# Inverse Fourier transform to compute saliency map
		ishift_saliency = np.fft.ifftshift(np.exp(Spectral_res + 1j * phase))
		Res_ifft_saliency = np.fft.ifft2(ishift_saliency)
		Res_saliency = np.abs(Res_ifft_saliency)
		
		# Normalize saliency map to 0-255 range
		rge_saliency = np.max(Res_saliency) - np.min(Res_saliency)
		if rge_saliency > 0:
			norm_saliency = (Res_saliency - np.min(Res_saliency)) * 255 / rge_saliency
		else:
			norm_saliency = np.zeros_like(Res_saliency)
		
		# Apply Gaussian blur to smooth the result
		saliency_map_display = cv2.GaussianBlur(norm_saliency, (9, 9), 2)
		
		# Save the saliency map
		saliency_save_path = os.path.join(restore_dir, 'saliency_map.png')
		cv2.imwrite(saliency_save_path, saliency_map_display.astype(np.uint8))
		
		# Display the saliency map in the UI
		imge1 = wx.Image(saliency_save_path, wx.BITMAP_TYPE_PNG)
		temp = ReSizeImage(imge1, 250)
		
		# Display in the saliency image place
		self.SaliencyImage.SetBitmap(wx.Bitmap(temp))
		self.SaliencyImage.Refresh()
		
		# Set the global saliency_image
		saliency_image = cv2.imread(saliency_save_path)
		
		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()

	def RestoreFeaturesEvents(self, event):
		self.loading_text.Show()
		self.loading_text.Refresh()
		wx.Yield()  # 让UI更新
		
		global decrypted_image, original_blur_amp, original_phase, original_info
		
		# 检查解密图像和所需恢复信息是否存在
		if decrypted_image is None or original_blur_amp is None or original_phase is None:
			wx.MessageBox('请先执行 提取显著性 -> 加密 -> 解密 完整流程', '操作顺序或数据错误', wx.OK | wx.ICON_ERROR)
			self.loading_text.Hide()
			self.loading_text.Refresh()
			event.Skip()
			return
		
		# 保存路径
		save_path = 'D:/Image-Encryption-Decryption-main/restore/restored_image_from_features.png'
		
		# 1. 将解密后的特征图转换为灰度图
		feature_map_gray = cv2.cvtColor(decrypted_image, cv2.COLOR_BGR2GRAY)
		feature_map_float = feature_map_gray.astype(np.float64)
		
		# 2. 对特征图进行高斯模糊，模拟原始处理过程
		blurred_feature = cv2.GaussianBlur(feature_map_float, (9, 9), 2)
		
		# 3. 计算特征图的傅里叶变换
		fft_feature = np.fft.fft2(blurred_feature)
		fshift_feature = np.fft.fftshift(fft_feature)
		log_amp_feature = np.log(np.abs(fshift_feature) + 1e-10)
		
		# 4. 计算特征图的相位谱
		phase_feature = np.angle(fshift_feature)
		
		# 5. 反向处理：从特征图恢复原始图像
		blur_amp_feature = cv2.blur(log_amp_feature, (3, 3))
		spec_res_feature = log_amp_feature - blur_amp_feature
		restored_log_amp = spec_res_feature + original_blur_amp
		
		# 6. 使用原始相位谱进行反傅里叶变换
		ishift = np.fft.ifftshift(np.exp(restored_log_amp + 1j * original_phase))
		restored_ifft = np.fft.ifft2(ishift)
		restored_image = np.abs(restored_ifft)
		
		# 7. 归一化恢复后的图像到0-255范围
		rge = np.max(restored_image) - np.min(restored_image)
		if rge > 0:
			norm_restored = (restored_image - np.min(restored_image)) * 255 / rge
		else:
			norm_restored = np.zeros_like(restored_image)
		
		# 8. 转换为BGR格式
		restored_image_bgr = cv2.cvtColor(norm_restored.astype(np.uint8), cv2.COLOR_GRAY2BGR)
		
		# 9. 使用保存的信息进行精确恢复
		# 9.1 应用全局统计信息
		for channel in range(3):
			# 获取当前通道的数据
			channel_data = restored_image_bgr[:,:,channel]
			
			# 应用全局统计信息
			current_mean = np.mean(channel_data)
			current_std = np.std(channel_data)
			current_min = np.min(channel_data)
			current_max = np.max(channel_data)
			
			# 计算缩放因子
			mean_scale = original_info['global_mean'][channel] / (current_mean + 1e-10)
			std_scale = original_info['global_std'][channel] / (current_std + 1e-10)
			
			# 应用缩放
			channel_data = (channel_data - current_mean) * std_scale + original_info['global_mean'][channel]
			
			# 确保值在原始范围内
			channel_data = np.clip(channel_data, 
								 original_info['global_min'][channel], 
								 original_info['global_max'][channel])
			
			restored_image_bgr[:,:,channel] = channel_data
		
		# 9.2 应用局部统计信息
		block_size = 16
		for block_info in original_info['local_stats']:
			y, x = block_info['position']
			block = restored_image_bgr[y:y+block_size, x:x+block_size]
			if block.shape[0] == block_size and block.shape[1] == block_size:
				for channel in range(3):
					channel_idx = channel * 4
					channel_data = block[:,:,channel]
					
					# 获取原始统计信息
					orig_mean = block_info['stats'][channel_idx]
					orig_std = block_info['stats'][channel_idx+1]
					orig_min = block_info['stats'][channel_idx+2]
					orig_max = block_info['stats'][channel_idx+3]
					
					# 计算当前统计信息
					current_mean = np.mean(channel_data)
					current_std = np.std(channel_data)
					
					# 应用局部调整
					channel_data = (channel_data - current_mean) * (orig_std/(current_std + 1e-10)) + orig_mean
					channel_data = np.clip(channel_data, orig_min, orig_max)
					
					block[:,:,channel] = channel_data
				restored_image_bgr[y:y+block_size, x:x+block_size] = block
		
		# 9.3 应用边缘信息
		for channel_info in original_info['edge_info']:
			channel = channel_info['channel']
			channel_data = restored_image_bgr[:,:,channel]
			
			# 计算当前边缘信息
			sobelx = cv2.Sobel(channel_data, cv2.CV_64F, 1, 0, ksize=3)
			sobely = cv2.Sobel(channel_data, cv2.CV_64F, 0, 1, ksize=3)
			current_edge_mag = np.sqrt(sobelx**2 + sobely**2)
			
			# 计算边缘强度缩放因子
			edge_scale = channel_info['mean_magnitude'] / (np.mean(current_edge_mag) + 1e-10)
			
			# 应用边缘调整
			channel_data = channel_data * edge_scale
			channel_data = np.clip(channel_data, 0, 255)
			
			restored_image_bgr[:,:,channel] = channel_data
		
		# 10. 保存处理后的图像
		cv2.imwrite(save_path, restored_image_bgr)

		# 显示恢复后的图像
		imge1 = wx.Image(save_path)
		temp = ReSizeImage(imge1, 250)
		self.DecryptImage.SetBitmap(wx.Bitmap(temp))
		self.DecryptImage.Refresh()

		self.loading_text.Hide()
		self.loading_text.Refresh()
		event.Skip()


