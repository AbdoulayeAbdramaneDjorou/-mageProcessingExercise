import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\Histogram.jpg'
def histogram_esitleme(image_path):
   
    img = cv2.imread(image_path, 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    img_esitleme = np.interp(img.flatten(), bins[:-1], cdf_normalized)
    img_esitleme = img_esitleme.reshape(img.shape).astype('uint8')
    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Orjinal')
    plt.subplot(122), plt.imshow(img_esitleme, 'gray'), plt.title('Eşitlenmiş')
    plt.show()
