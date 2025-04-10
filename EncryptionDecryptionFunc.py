import PIL
import numpy as np
import cv2
import wx


def arnold_encrypt(image, iterations):#Arnold's cat map（也称为Arnold's cat transform）的加密算法。Arnold's cat map是一个二维的线性变换，经常用于图像加密。
    height, width,ch = image.shape
    encrypted_image = np.zeros_like(image, dtype=np.uint8)

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                new_y = (2 * y + x) % height
                new_x = (y + x) % width
                encrypted_image[new_y, new_x] = image[y, x]
        image = encrypted_image.copy()

    return encrypted_image


def arnold_decrypt(encrypted_image, iterations):#用于解密经过Arnold's cat map加密的图像的函数
    height, width,ch = encrypted_image.shape
    decrypted_image = np.zeros_like(encrypted_image, dtype=np.uint8)

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                old_y = (y - x) % height
                old_x = (2 * x - y) % width
                decrypted_image[old_y, old_x] = encrypted_image[y, x]
        encrypted_image = decrypted_image.copy()

    return decrypted_image


def logistic_map(x, r, num_iterations):#定义了一个名为logistic_map的函数，该函数用于计算Logistic Map方程。Logistic Map是一个非线性动态系统，通常用于描述种群的增长或其他生态学过程。
    """Logistic Map equation"""
    X = []
    for i in range(num_iterations):
        x1 = r * x * (1 - x)
        x = x1
        X.append(x)
    return X



def logistic_encrypt_image(image,r):#定义了一个名为logistic_encrypt_image的函数，该函数使用Logistic Map和XOR算法对图像进行加密。
    """Encrypts an image using logistic map and XOR algorithm"""
    # Generate chaos key
    height, width,ch = image.shape
    key = np.zeros((height, width,ch), dtype=np.float64)
    chaotic_sequence = logistic_map(0.5, r, height * width*ch)
    chaotic_sequence = np.reshape(chaotic_sequence, (height, width,ch))
    key = chaotic_sequence.copy()

    # Perform XOR encryption
    encrypted_image = cv2.bitwise_xor(image, np.uint8(key * 255))
    return encrypted_image


def logistic_decrypt_image(encrypted_image, r):#定义了一个名为logistic_decrypt_image的函数，用于使用Logistic Map和XOR算法解密图像
    """Decrypts an encrypted image using logistic map and XOR algorithm"""
    height, width,ch = encrypted_image.shape

    # Generate chaos key
    key = np.zeros((height, width), dtype=np.float64)
    chaotic_sequence = logistic_map(0.5, r, height * width*ch)
    chaotic_sequence = np.reshape(chaotic_sequence, (height, width,ch))
    key = chaotic_sequence.copy()

    # Perform XOR decryption
    decrypted_image = cv2.bitwise_xor(encrypted_image, np.uint8(key * 255))
    return decrypted_image


def PilImage2WxImage(self, pilImage: PIL.Image.Image):#定义了一个方法 PilImage2WxImage，它的目的是将 PIL Image 转换为 wxPython Image
    '''
    转换　PIL Image 为　wxPython Image
    :param pilImage: PIL.Image.Image
    :return: wx.Image
    '''
    wxImage = wx.Image((pilImage.size[0], pilImage.size[1]), pilImage.convert("RGB").tobytes())
    return wxImage


def WxImage2PilImage(self, wxImage: wx.Image):#定义了一个名为 WxImage2PilImage 的方法，其目的是将 wxPython 的 Image 对象转换为 PIL Image 对象
    '''
    转换 wxPython Image 为　PIL Image 对象
    :param wxImage: wx.Image 实例
    :return: PIL.Image.Image
    '''
    from PIL import Image
    # wxImage 的 GetData方法返回图像的字节码，通过bytes强制转换，可以直接作为frombytes的参数。
    pilImage = Image.frombytes('RGB', (wxImage.GetWidth(), wxImage.GetHeight()), bytes(wxImage.GetData()))
    # pil.show()
    return pilImage


