# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
import cv2

IMAGE_SIZE = 64

#按照指定图像大小调整尺寸
def resize_image(image, height = IMAGE_SIZE, width = IMAGE_SIZE):    
    top, bottom, left, right = (0, 0, 0, 0)

    #将当前桢图像转换成灰度图像            
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    #获取图像尺寸，黑白的话，就没有第三个层次,
    h, w = image.shape #, _
    #对于长宽不相等的图片，找到最长的一边
    longest_edge = max(h, w)    

    #计算短边需要增加多上像素宽度使其与长边等长
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    #RGB颜色
    BLACK = [0, 0, 0]
    
    #给图像增加边界，是图片长、宽等长，cv2.BORDER_CONSTANT指定边界颜色由value指定
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    
    #调整图像大小并返回
    return cv2.resize(constant, (height, width))
