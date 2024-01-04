import cv2
import numpy as np
import numpy as plt
image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\gaussian.jpg'
kernel_size=1.8
def apply_gaussian(image_path, kernel_size):
    
    img = cv2.imread(image_path)
    blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB)), plt.title(f'Gaussian Blur (Kernel Size = {kernel_size})')
    plt.show()