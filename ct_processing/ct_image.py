import cv2
import numpy as np

def mean_filter(image_in, kernel=3):
    image_out = cv2.blur(image_in, (kernel,kernel))
    return image_out

def median_filter(image_in, kernel=3):
    image_out = cv2.medianBlur(image_in, kernel)
    return image_out

def gaussian_filter(image_in, kernel=3):
    image_out = cv2.GaussianBlur(image_in, (kernel,kernel), 0)
    return image_out

