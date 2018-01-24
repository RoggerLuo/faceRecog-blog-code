import os
import sys
import numpy as np
import cv2
from resize_image import resize_image
from load_data import load_dataset

if __name__ == '__main__':    
    if len(sys.argv) == 2:

        # full_path = sys.argv[1]
        # if full_path.endswith('.jpg') or full_path.endswith('.bmp'):
            
            # image = cv2.imread(full_path) # 统一输入彩色图
            # image = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)
            
            # cv2.imshow('imaggggge',image)
            # cv2.waitKey(0) 
            # cv2.destroyAllWindows()

        load_dataset(sys.argv[1])        
                        

