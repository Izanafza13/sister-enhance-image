import os
import cv2
import numpy as np

def denoise(image_path):
    image = cv2.imread(image_path)
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    
    result_path = os.path.join('/tmp', f"denoised_{os.path.basename(image_path)}")
    cv2.imwrite(result_path, denoised_image)
    
    return result_path