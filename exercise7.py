import cv2
import numpy as np
import numpy as plt
image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\gaussianF.jpg'
kernel_size=1.3
def gaussian_filter(image_path, kernel_size):
    img = cv2.imread(image_path, 0)  
    img_filtered = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(img_filtered, 'gray'), plt.title(f'Gaussian Filter (Kernel Size = {kernel_size})')
    plt.show()
