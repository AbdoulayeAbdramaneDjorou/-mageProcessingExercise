import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\gamma.jpg'
gamma=1.4
def gamma_correction(image_path, gamma):
   
    img = cv2.imread(image_path, 0)  
    img_normalized = img / 255.0

    img_corrected = np.power(img_normalized, gamma)

    img_corrected = (img_corrected * 255).astype(np.uint8)
    plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(img_corrected, 'gray'), plt.title(f'Gamma Corrected Image (Gamma={gamma})')
    plt.show()
