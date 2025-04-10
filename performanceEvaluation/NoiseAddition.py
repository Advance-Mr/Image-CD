import cv2
import math
import random
import numpy as np
import matplotlib.pyplot as plt

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



def gauss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''

    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out

#默认10%的椒盐噪声
def salt_and_pepper_noise(noise_img, proportion=0.1):
    height, width, _ = noise_img.shape
    num = int(height * width * proportion)  # 多少个像素点添加椒盐噪声
    for i in range(num):
        w = random.randint(0, width - 1)
        h = random.randint(0, height - 1)
        if random.randint(0, 1) == 0:
            noise_img[h, w] = 0
        else:
            noise_img[h, w] = 255
    return noise_img

def main():
  img = '../OriImg/lena.png'
  img1 = '../EnyImg/Encryption.png'
  img2 = '../OriImg/Lena_encrypt2.png'
  im=cv2.imread(img1)
  gauss_img=gauss_noise(im,mean=0,var=0.0005)
  im = cv2.imread(img1)
  salt_img=salt_and_pepper_noise(im,proportion=0.05)
  cv2.imshow("gauss_img", gauss_img)
  cv2.imshow("salt_imge", salt_img)
  iterations = 10
  decrypted_image1 = arnold_decrypt(gauss_img, iterations)
  decrypted_image2 = arnold_decrypt(salt_img, iterations)
  cv2.imshow("decrypted_image1", decrypted_image1)
  cv2.imshow("decrypted_image2", decrypted_image2)
  im = cv2.imread(img1)
  decrypted_image3 = arnold_decrypt(im, iterations)
  cv2.imshow("decrypted_image3", decrypted_image3)

  #cv2.imwrite('./gauss_img.png',gauss_img)
  #cv2.imwrite('./salt_img.png',salt_img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()


if __name__== '__main__':
  main()
