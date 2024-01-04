import cv2
import numpy as np
import numpy as plt
image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\sobel.jpg'
def sobel_filter(image_path):
    
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.subplot(132), plt.imshow(np.abs(sobel_x), cmap='gray'), plt.title('Sobel X')
    plt.subplot(133), plt.imshow(np.abs(sobel_y), cmap='gray'), plt.title('Sobel Y')
    plt.show()

    plt.imshow(magnitude, cmap='gray'), plt.title('Sobel Magnitude')
    plt.show()
