#-*- coding: utf-8 -*-

from faceTrain import Model
# from cv2 import cvLoadImage
import cv2
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:


        frame = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE) # cv2.IMREAD_COLOR #cv2.IMREAD_GRAYSCALE
        cv2.imshow('image',frame)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

        model = Model()
        model.load_model(file_path = './model/me.face.model.h5')
        faceID = model.face_predict(frame)  
        print(faceID)