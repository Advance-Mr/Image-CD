import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
绘制灰度直方图
'''
def hist(img):
  img=cv2.imread(img)
  B,G,R=cv2.split(img)
  #转成一维
  R=R.flatten(order='C')
  G=G.flatten(order='C')
  B=B.flatten(order='C')


  #结果展示
  plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文乱码
  #plt.subplot(232)
  # plt.imshow(img[:,:,(2,1,0)])
  plt.hist(img.flatten(order='C'),bins=range(257),color='gray')
  plt.title('原图像')
  f = plt.gcf()  # 获取当前图像
  f1=f.savefig(r'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHis.png', format='png')
  f.clear()  # 释放内存
  #子图2，通道R
  #plt.subplot(234)
  #imshow()对图像进行处理，画出图像，show()进行图像显示
  plt.hist(R,bins=range(257),color='red')
  plt.title('通道R')
  f = plt.gcf()  # 获取当前图像
  f2=f.savefig(r'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisR.png', format='png')
  f.clear()  # 释放内存
  # plt.show()
  #不显示坐标轴
  # plt.axis('off')

  #子图3，通道G
  #plt.subplot(235)
  plt.hist(G,bins=range(257),color='green')
  plt.title('通道G')
  f = plt.gcf()  # 获取当前图像
  f3=f.savefig(r'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisG.png', format='png')
  f.clear()  # 释放内存
  # plt.show()
  # plt.axis('off')

  #子图4，通道B
  #plt.subplot(236)
  plt.hist(B,bins=range(257),color='blue')
  plt.title('通道B')
  f = plt.gcf()  # 获取当前图像
  f4=f.savefig(r'D:\Image-Encryption-Decryption-main\AnalysisImg\OriHisB.png', format='png')
  f.clear()  # 释放内存
  return f1,f2,f3,f4
  # plt.axis('off')
  # #设置子图默认的间距
  #plt.tight_layout()
  #plt.show()
  #print('生成结束')


def main():
  img='../OriImg/Lena.png'
  #图像lean的灰度直方图
  #img = '../OriImg/Lena_encrypt1.png'
  hist(img)

if __name__== '__main__':
  main()