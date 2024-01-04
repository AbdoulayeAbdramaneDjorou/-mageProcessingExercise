import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\Laplace.jpg'
kernel_size=1.8

def blur_and_laplace(image_path, kernel_size):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

   
    img_blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    laplace = cv2.Laplacian(img_blurred, cv2.CV_64F)

    plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.subplot(132), plt.imshow(img_blurred, cmap='gray'), plt.title('Blurred Image')
    plt.subplot(133), plt.imshow(np.abs(laplace), cmap='gray'), plt.title('Laplace Operator')
    plt.show()