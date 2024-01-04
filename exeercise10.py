import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\smoothing.jpg'
kernel_size=1.8
def image_smoothing(image_path, kernel_size):
    img = cv2.imread(image_path)

    
    smoothed_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
 
    
    sharpened_img = cv2.filter2D(img, -1, kernel)

   
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB)), plt.title('Sharpened Image')
    plt.show()
    
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB)), plt.title('Smoothed Image')
    plt.show()
