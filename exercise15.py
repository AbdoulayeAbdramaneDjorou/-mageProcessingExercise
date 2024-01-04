import cv2
import numpy as np
import numpy as plt

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\opening.jpg'
operation_type='opening'

kernel_size=1.8
def acma_kapama(image_path, operation_type, kernel_size):
    
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

   
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

   
    if operation_type == 'opening':
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif operation_type == 'closing':
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    else:
        raise ValueError("Geçersiz işlem türü. 'opening' veya 'closing' kullanın.")

  
    plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Orjinal Görüntü')
    plt.subplot(132), plt.imshow(result, cmap='gray'), plt.title(f'{operation_type.capitalize()} İşlemi ({kernel_size}x{kernel_size} Çekirdek)')
    plt.subplot(133), plt.imshow(kernel, cmap='gray'), plt.title('Morfolojik İşlem Çekirdeği')
    plt.show()
