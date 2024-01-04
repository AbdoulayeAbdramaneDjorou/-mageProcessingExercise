import cv2
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\rgb.jpg'
def bolumleme(image_path):
   
    img = cv2.imread(image_path)
    blue_channel, green_channel, red_channel = cv2.split(img)
    plt.figure(figsize=(12, 4))

    plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Orjinal Resim')
    plt.subplot(132), plt.imshow(blue_channel, cmap='Blues'), plt.title('Mavi Kanal')
    plt.subplot(133), plt.imshow(red_channel, cmap='Reds'), plt.title('Kırmızı Kanal')

    plt.show()