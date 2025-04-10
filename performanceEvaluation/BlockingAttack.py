import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

'''
对加密图像进行处理，返回处理后的结果
'''
def arnold_encrypt(image, iterations):
    height, width,ch = image.shape
    encrypted_image = np.zeros_like(image)#dtype=np.uint8

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                new_y = (2 * y + x) % height
                new_x = (y + x) % width
                encrypted_image[new_y, new_x] = image[y, x]
        image = encrypted_image.copy()

    return encrypted_image


def arnold_decrypt(encrypted_image, iterations):
    height, width,ch = encrypted_image.shape
    decrypted_image = np.zeros_like(encrypted_image)#, dtype=np.uint8

    for i in range(iterations):
        for y in range(height):
            for x in range(width):
                old_y = (y - x) % height
                old_x = (2 * x - y) % width
                decrypted_image[old_y, old_x] = encrypted_image[y, x]
        encrypted_image = decrypted_image.copy()

    return decrypted_image


def occlusion(img):
    img = cv2.imread(img)
    h, w, ch = img.shape
    R, G, B  = cv2.split(img)
    # 随机移除R通道80*80大小的像素
    # 产生随机整数，裁剪大小为80
    pos_w = np.random.randint(0, w - 80)
    pos_h = np.random.randint(0, h - 80)
    for i in range(80):
        for j in range(80):
            R[pos_h + i][pos_w + j] = 0
    # 随机移除G通道50*80的像素
    pos_w = np.random.randint(0, w - 50)
    pos_h = np.random.randint(0, h - 80)
    for i in range(80):
        for j in range(50):
            G[pos_h + i][pos_w + j] = 0
    # 三通道合并
    im = cv2.merge([R, G, B])
    # 随机移除All通道60*50的像素
    pos_w = np.random.randint(0, w - 60)
    pos_h = np.random.randint(0, h - 50)
    for i in range(50):
        for j in range(60):
            im[pos_h + i][pos_w + j] = np.array([0, 0, 0])

    return im


def main():
    img = '../OriImg/lena.png'
    img1 = '../EnyImg/Encryption.png'
    img2 = '../OriImg/Lena_encrypt2.png'
    lossy_encrypt = occlusion(img1)
    cv2.imshow("lossy_encrypt", lossy_encrypt)

    iterations = 10
    decrypted_image1 = arnold_decrypt(lossy_encrypt, iterations)
    cv2.imshow("decrypted_image1", decrypted_image1)
    # 保存处理后的有损加密图像,opencv的颜色通道顺序为[B,G,R]
    #cv2.imwrite('./Lossy_Lena_encrypt1.png', lossy_encrypt[:, :, (2, 1, 0)])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()