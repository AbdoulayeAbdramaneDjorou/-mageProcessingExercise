import cv2
import numpy as np

image_path='C:\Users\Abdoulaye Abdramane\Desktop\imageProcessing\bitplane.jpg'
def bit_plane_slice(image_path):
    
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    num_bits = int(np.max(img)).bit_length()
    bit_planes = []

    
    for i in range(num_bits):
       
        bit_plane = (img >> i) & 1
        bit_planes.append(bit_plane * 255) 
    cv2.imshow('Original Image', img)
    for i in range(num_bits):
        cv2.imshow(f'Bit Plane {i}', bit_planes[i])

    cv2.waitKey(0)
    cv2.destroyAllWindows()