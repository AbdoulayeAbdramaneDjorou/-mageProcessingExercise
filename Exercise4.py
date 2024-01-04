import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\contrast.jpg'
def contrast_stretching(image_path):
    
    img = cv2.imread(image_path, 0)  
    min_output, max_output = 0, 255

    
    min_input, max_input = np.min(img), np.max(img)
    img_stretched = ((img - min_input) / (max_input - min_input)) * (max_output - min_output) + min_output

    img_stretched = img_stretched.astype(np.uint8)

    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(img_stretched, 'gray'), plt.title('contrast.jpg')
    plt.show()