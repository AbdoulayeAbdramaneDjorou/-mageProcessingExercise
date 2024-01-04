import cv2
import numpy as np
import numpy as plt

image='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\salt.jpg'
salt_prob=0.01
pepper_pro=0.01

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
     
    salt_mask = np.random.rand(*image.shape[:2]) < salt_prob
    noisy_image[salt_mask] = 255

    
    pepper_mask = np.random.rand(*image.shape[:2]) < pepper_prob
    noisy_image[pepper_mask] = 0

    return noisy_image

def main(image_path, salt_prob, pepper_prob):
   
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    noisy_image = add_salt_and_pepper_noise(img, salt_prob, pepper_prob)

    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(noisy_image, cmap='gray'), plt.title('Image with Salt and Pepper Noise')
    plt.show()
