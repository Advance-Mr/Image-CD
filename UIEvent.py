import cv2
import wx
import wx.xrc
import numpy as np


def getImageEvents(self, event):
    path = self.m_genericDirCtrl2.GetFilePath()
    if path:
        # image = wx.Image('D:/Image-Encryption-Decryption-main/Images/4.jpg', wx.BITMAP_TYPE_JPEG)
        image = wx.Image(path, wx.BITMAP_TYPE_ANY)
        # temp = image.ConvertToBitmap()
        # bitmap2Width=self.m_bitmap2.GetSize()
        # bitmap2Height = self.m_bitmap2.GetMaxHeight()
        temp = ReSizeImage(image, 250)

        self.OriImage.SetBitmap(wx.BitmapFromImage(temp))

        # self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
        self.OriImage.Refresh()
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

    temp = ReSizeImage(imge1, 250)

    self.EncryptImage.SetBitmap(wx.BitmapFromImage(temp))

    # self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
    self.EncryptImage.Refresh()

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

    temp = ReSizeImage(imge1, 250)

    self.DecryptImage.SetBitmap(wx.BitmapFromImage(temp))

    # self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
    self.DecryptImage.Refresh()

    event.Skip()


def StartAnalysisEvents(self, event):
    img = './OriImg/Lena.png'
    img1 = './OriImg/Lena_encrypt1.png'
    img2 = './OriImg/Lena_encrypt2.png'
    R_npcr, G_npcr, B_npcr = NPCR(img1, img2);
    R_uaci, G_uaci, B_uaci = UACI(img1, img2)

    _cols = "a b c d".split()
    _cows = "a b c d".split()
    # self.SensitivityAnalyGrid.SetColLabelValue("a b c d".split());
    # self.SensitivityAnalyGrid.Refresh();
    self.SensitivityAnalyGrid.SetCellValue(0, 0, '{:.4%}'.format(R_npcr))
    self.SensitivityAnalyGrid.SetCellValue(1, 0, '{:.4%}'.format(G_npcr))
    self.SensitivityAnalyGrid.SetCellValue(2, 0, '{:.4%}'.format(B_npcr))
    self.SensitivityAnalyGrid.SetCellValue(0, 1, '{:.4%}'.format(R_uaci))
    self.SensitivityAnalyGrid.SetCellValue(1, 1, '{:.4%}'.format(G_uaci))
    self.SensitivityAnalyGrid.SetCellValue(2, 1, '{:.4%}'.format(B_uaci))

    f1, f2, f3, f4 = hist(img)
    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHis.png'
    f1 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f1 = ReSizeImage(f1, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisB.png'
    f2 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f2 = ReSizeImage(f2, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisG.png'
    f3 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f3 = ReSizeImage(f3, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisR.png'
    f4 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f4 = ReSizeImage(f4, 200)

    self.OriHistogramG.SetBitmap(wx.BitmapFromImage(f1))
    self.OriHistogramG.Refresh()
    self.OriHistogramR.SetBitmap(wx.BitmapFromImage(f2))
    self.OriHistogramR.Refresh()
    self.OriHistogramGn.SetBitmap(wx.BitmapFromImage(f3))
    self.OriHistogramGn.Refresh()
    self.OriHistogramB.SetBitmap(wx.BitmapFromImage(f4))
    self.OriHistogramB.Refresh()

    f1, f2, f3, f4 = hist(img1)
    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHis.png'
    f5 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f5 = ReSizeImage(f5, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisB.png'
    f6 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f6 = ReSizeImage(f6, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisG.png'
    f7 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f7 = ReSizeImage(f7, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisR.png'
    f8 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f8 = ReSizeImage(f8, 200)

    self.EnyHistogramG.SetBitmap(wx.BitmapFromImage(f5))
    self.EnyHistogramG.Refresh()
    self.EnyHistogramR.SetBitmap(wx.BitmapFromImage(f6))
    self.EnyHistogramR.Refresh()
    self.EnyHistogramGn.SetBitmap(wx.BitmapFromImage(f7))
    self.EnyHistogramGn.Refresh()
    self.EnyHistogramB.SetBitmap(wx.BitmapFromImage(f8))
    self.EnyHistogramB.Refresh()

    R_Rxy, G_Rxy, B_Rxy = correlation(img)
    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCor.png'
    f1 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f1 = ReSizeImage(f1, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorR.png'
    f2 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f2 = ReSizeImage(f2, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorGn.png'
    f3 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f3 = ReSizeImage(f3, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorB.png'
    f4 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f4 = ReSizeImage(f4, 200)

    self.OriCorrelationG.SetBitmap(wx.BitmapFromImage(f1))
    self.OriCorrelationG.Refresh()
    self.OriCorrelationR.SetBitmap(wx.BitmapFromImage(f2))
    self.OriCorrelationR.Refresh()
    self.OriCorrelationGn.SetBitmap(wx.BitmapFromImage(f3))
    self.OriCorrelationGn.Refresh()
    self.OriCorrelationB.SetBitmap(wx.BitmapFromImage(f4))
    self.OriCorrelationB.Refresh()

    R_Rxy, G_Rxy, B_Rxy = correlation(img1)
    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCor.png'
    f1 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f1 = ReSizeImage(f1, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorR.png'
    f2 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f2 = ReSizeImage(f2, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorGn.png'
    f3 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f3 = ReSizeImage(f3, 200)

    path = 'D:\Image-Encryption-Decryption-main\AnalysisImg\OriCorB.png'
    f4 = wx.Image(path, wx.BITMAP_TYPE_ANY)
    f4 = ReSizeImage(f4, 200)

    self.EnyCorrelationBoxG.SetBitmap(wx.BitmapFromImage(f1))
    self.EnyCorrelationBoxG.Refresh()
    self.EnyCorrelationR.SetBitmap(wx.BitmapFromImage(f2))
    self.EnyCorrelationR.Refresh()
    self.EnyCorrelationGn.SetBitmap(wx.BitmapFromImage(f3))
    self.EnyCorrelationGn.Refresh()
    self.EnyCorrelationB.SetBitmap(wx.BitmapFromImage(f4))
    self.EnyCorrelationB.Refresh()

    R_entropy, G_entropy, B_entropy = entropy(img)
    R_entropy1, G_entropy1, B_entropy1 = entropy(img1)
    R_entropy2, G_entropy2, B_entropy2 = entropy(img2)

    # self.SensitivityAnalyGrid.SetColLabelValue("a b c d".split());
    # self.SensitivityAnalyGrid.Refresh();
    self.Information_EntropyGrid.SetCellValue(0, 0, '{:.4}'.format(R_entropy))
    self.Information_EntropyGrid.SetCellValue(1, 0, '{:.4}'.format(G_entropy))
    self.Information_EntropyGrid.SetCellValue(2, 0, '{:.4}'.format(B_entropy))
    self.Information_EntropyGrid.SetCellValue(0, 1, '{:.4}'.format(R_entropy1))
    self.Information_EntropyGrid.SetCellValue(1, 1, '{:.4}'.format(G_entropy1))
    self.Information_EntropyGrid.SetCellValue(2, 1, '{:.4}'.format(B_entropy1))
    self.Information_EntropyGrid.SetCellValue(0, 2, '{:.4}'.format(R_entropy2))
    self.Information_EntropyGrid.SetCellValue(1, 2, '{:.4}'.format(G_entropy2))
    self.Information_EntropyGrid.SetCellValue(2, 2, '{:.4}'.format(B_entropy2))

    R_gvd1, G_gvd1, B_gvd1 = GVD(img, img1)
    R_gvd2, G_gvd2, B_gvd2 = GVD(img, img2)
    self.RandomnessGrid.SetCellValue(0, 0, '{:.4}'.format(R_gvd1))
    self.RandomnessGrid.SetCellValue(1, 0, '{:.4}'.format(G_gvd1))
    self.RandomnessGrid.SetCellValue(2, 0, '{:.4}'.format(B_gvd1))
    self.RandomnessGrid.SetCellValue(0, 1, '{:.4}'.format(R_gvd2))
    self.RandomnessGrid.SetCellValue(1, 1, '{:.4}'.format(G_gvd2))
    self.RandomnessGrid.SetCellValue(2, 1, '{:.4}'.format(B_gvd2))

    img111 = './OriImg/Lena.png'
    # img1 = '../OriImg/Lena_encrypt1.png'
    # img2 = '../OriImg/Lena_encrypt2.png'
    im = cv2.imread(img111)
    iterations = 10
    gauss_img = gauss_noise(im, mean=0, var=0.0005)
    salt_img = salt_and_pepper_noise(im, proportion=0.05)
    # decrypted_image_gauss = arnold_decrypt(gauss_img, iterations)
    # decrypted_image_salt  = arnold_decrypt(salt_img, iterations)

    # path = 'D:/Image-Encryption-Decryption-main/EnyImg/Decryption.jpg'
    # cv2.imwrite(path, decrypted_image)
    # imge1 = wx.Image(path, wx.BITMAP_TYPE_JPEG)

    temp = ReSizeImage(gauss_img, 200)

    self.NoiseOriImage.SetBitmap(wx.BitmapFromImage(gauss_img))
    self.NoiseOriImage.Refresh()
    # self.NoiseEncryptImage.SetBitmap(wx.BitmapFromImage(decrypted_image_gauss))
    # self.NoiseEncryptImage.Refresh()
    self.NoiseOriImage1.SetBitmap(wx.BitmapFromImage(salt_img))
    self.NoiseOriImage1.Refresh()
    # self.NoiseEncryptImage1.SetBitmap(wx.BitmapFromImage(decrypted_image_salt))
    # self.NoiseEncryptImage1.Refresh()

    # self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
    # self.DecryptImage.Refresh()

    R_EQ1, G_EQ1, B_EQ1 = EQ(img, img1)
    R_EQ2, G_EQ2, B_EQ2 = EQ(img, img2)
    self.EncryptionQualityGrid.SetCellValue(0, 0, '{:.0f}'.format(R_EQ1))
    self.EncryptionQualityGrid.SetCellValue(1, 0, '{:.0f}'.format(G_EQ1))
    self.EncryptionQualityGrid.SetCellValue(2, 0, '{:.0f}'.format(B_EQ1))
    self.EncryptionQualityGrid.SetCellValue(0, 1, '{:.0f}'.format(R_EQ2))
    self.EncryptionQualityGrid.SetCellValue(1, 1, '{:.0f}'.format(G_EQ2))
    self.EncryptionQualityGrid.SetCellValue(2, 1, '{:.0f}'.format(B_EQ2))


def ReSizeImage(image,PhotoMaxSize):

    W = image.GetWidth()
    H = image.GetHeight()
    if W > H:
        NewW = PhotoMaxSize
        NewH = PhotoMaxSize * H / W
    else:
        NewH = PhotoMaxSize
        NewW = PhotoMaxSize * W / H
    img = image.Scale(NewW, NewH)
    temp = img.ConvertToBitmap()
    size = temp.GetWidth(), temp.GetHeight()
    return  img

