# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import cv2
import wx
import wx.xrc
import numpy as np

###########################################################################
## Class window
###########################################################################
from PIL import Image

from EncryptionDecryptionFunc import arnold_encrypt, PilImage2WxImage, arnold_decrypt


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

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_bitmap2, 1, wx.ALL, 5 )


		LayerImage.Add( bSizer29, 1, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_bitmap3, 1, wx.ALL, 5 )


		LayerImage.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_bitmap4, 1, wx.ALL, 5 )


		LayerImage.Add( bSizer33, 1, wx.EXPAND, 5 )


		LayImage.Add( LayerImage, 6, wx.EXPAND, 5 )


		LayMain.Add( LayImage, 7, wx.EXPAND, 5 )


		LayRoot.Add( LayMain, 4, wx.EXPAND, 5 )

		LayerAnalysis = wx.BoxSizer( wx.VERTICAL )

		LayerAnalysisButton = wx.BoxSizer( wx.VERTICAL )

		self.SavaAnalysis_button25 = wx.Button( self, wx.ID_ANY, u"保存分析结果", wx.DefaultPosition, wx.DefaultSize, 0 )
		LayerAnalysisButton.Add( self.SavaAnalysis_button25, 0, wx.ALL, 5 )


		LayerAnalysis.Add( LayerAnalysisButton, 2, wx.EXPAND, 5 )

		LayerAnalysisImage = wx.BoxSizer( wx.VERTICAL )

		self.Analysis_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		LayerAnalysisImage.Add( self.Analysis_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		LayerAnalysis.Add( LayerAnalysisImage, 8, wx.EXPAND, 5 )


		LayRoot.Add( LayerAnalysis, 6, wx.EXPAND, 5 )


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

		# Connect Events
		self.FileChoose.Bind( wx.EVT_BUTTON, self.getImage )
		self.Encrypt_button.Bind( wx.EVT_BUTTON, self.EncryptImage )
		self.Decryption_button.Bind( wx.EVT_BUTTON, self.DecryptImage )

	def __del__( self ):
		pass


	def getImage(self, event):
		path = self.m_genericDirCtrl2.GetFilePath()
		if path:
			#image = wx.Image('D:/Image-Encryption-Decryption-main/Images/4.jpg', wx.BITMAP_TYPE_JPEG)
			image = wx.Image(path, wx.BITMAP_TYPE_ANY)
			#temp = image.ConvertToBitmap()
			#bitmap2Width=self.m_bitmap2.GetSize()
			#bitmap2Height = self.m_bitmap2.GetMaxHeight()
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
			#screen_width, screen_height = screen.GetSize()
			#print(bitmap2Width)
			#print(bitmap2Height)
			#bgm = image.Scale(int(screen_width*3/15), screen_height*3/15)
			temp = img.ConvertToBitmap()
			size = temp.GetWidth(), temp.GetHeight()
			self.m_bitmap2.SetBitmap(wx.BitmapFromImage(temp))

			#self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
			self.m_bitmap2.Refresh()
			#bSizer29.Add(self.m_bitmap2, 0, wx.ALL, 5)
				#self.frame.Show()
				#self.SetTopWindow(self.frame)
				#return True
			print(path)
		else:
			wx.MessageBox('未选中文件', '失败', wx.OK | wx.ICON_ERROR)
		event.Skip()

	def EncryptImage(self, event):
		global encrypted_image,iterations
		path = self.m_genericDirCtrl2.GetFilePath()
		# print(x)
		image_input = cv2.imread(path, 0)  # 'C:/Users/aakas/Documents/flower.jpg'

		# 加密图像
		iterations = 10
		encrypted_image = arnold_encrypt(image_input, iterations)
		#print(image_input)
		#(imageWidth1, imageHeight1) = image_input.shape
		#image_inputFloat = image_input.astype(float) / 255.0
		#print(image_inputFloat)

		#mu, sigma = 0, 0.1  # mean and standard deviation
		#global key

		#key = np.random.normal(mu, sigma, (imageWidth1, imageHeight1)) + np.finfo(float).eps
		#print(key)
		#image_encrypted = image_inputFloat / key

		#EnyImage=cv2.imwrite('image_encrypted1.jpg', image_encrypted * 255)
		#print(image_encrypted * 255)
		path='D:/Image-Encryption-Decryption-main/EnyImg/Encryption.jpg'
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

	def DecryptImage(self, event):
			#path='D:/Image-Encryption-Decryption-main/image_encrypted1.jpg'
			#path = self.m_genericDirCtrl2.GetFilePath()
			#image_input = cv2.imread(path, 0)
			#(imageWidth1, imageHeight1) = image_input.shape
			#image_inputFloat = image_input.astype(float) / 255.0
			#print(image_input.astype(float))

			#print(key)
			#image_output = image_inputFloat * key
			#image_output *= 255.0
			#cv2.imwrite('image_output1.jpg', image_output)

			#imge1 = wx.Image('image_output1.jpg')

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


