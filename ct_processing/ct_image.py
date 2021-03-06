import cv2

def mean_filter(image_in, kernel=3):
    image_out = cv2.blur(image_in, (kernel,kernel))
    return image_out

def median_filter(image_in, kernel=3):
    image_out = cv2.medianBlur(image_in, kernel)
    return image_out

def gaussian_filter(image_in, kernel=3):
    image_out = cv2.GaussianBlur(image_in, (kernel,kernel), 0)
    return image_out

def filter_laplacian(image_in):
    image_out = cv2.Laplacian(image_in, cv2.CV_64F)
    return image_out

def filter_sobel(image_in, kernel=3):
    image_outx = cv2.Sobel(image_in, cv2.CV_64F, 1, 0, ksize=kernel)
    image_outy = cv2.Sobel(image_in, cv2.CV_64F, 0, 1, ksize=kernel)
    return image_outx, image_outy

