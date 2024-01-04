import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\contraharmonic.jpg'
window_size=5
Q=2.5
def contraharmonic_mean_filter(image, window_size, Q):
    pad = (window_size - 1) // 2
    result_image = np.zeros_like(image, dtype=np.float64)

    padded_image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_CONSTANT, value=0)

    for i in range(pad, padded_image.shape[0] - pad):
        for j in range(pad, padded_image.shape[1] - pad):
            window = padded_image[i-pad:i+pad+1, j-pad:j+pad+1]
            numerator = np.sum(np.power(window, Q+1))
            denominator = np.sum(np.power(window, Q))
            result_image[i-pad, j-pad] = numerator / (denominator + 1e-10)

    return np.uint8(result_image)

def main(image_path, window_size, Q):
   
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    filtered_image = contraharmonic_mean_filter(img, window_size, Q)

    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
    plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Contraharmonic Mean Filtered Image')
    plt.show()
