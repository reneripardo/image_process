import cv2

def mean_filter(image_in, kernel=3):
    """Apply mean filter.
        Arguments:
            image_in {numpy.array} -- image input.
            kernel {int} -- neighborhood size.
        Returns:
            image_out {numpy.array} -- image ouput.
    """
    image_out = cv2.blur(image_in, (kernel,kernel))
    return image_out

def median_filter(image_in, kernel=3):
    """Apply median filter.
        Arguments:
            image_in {numpy.array} -- image input.
            kernel {int} -- neighborhood size.
        Returns:
            image_out {numpy.array} -- image ouput.
    """
    image_out = cv2.medianBlur(image_in, kernel)
    return image_out

def gaussian_filter(image_in, kernel=3):
    """Apply gaussian filter.
        Arguments:
            image_in {numpy.array} -- image input.
            kernel {int} -- neighborhood size.
        Returns:
            image_out {numpy.array} -- image ouput.
    """
    image_out = cv2.GaussianBlur(image_in, (kernel,kernel), 0)
    return image_out

def laplacian_filter(image_in):
    """Apply laplacian filter.
        Arguments:
            image_in {numpy.array} -- image input.
        Returns:
            image_out {numpy.array} -- image ouput.
    """
    image_out = cv2.Laplacian(image_in, cv2.CV_64F)
    return image_out

def sobel_filter(image_in, kernel=3):
    """Apply sobel filter.
        Arguments:
            image_in {numpy.array} -- image input.
            kernel {int} -- neighborhood size.
        Returns:
            image_outx {numpy.array} -- x-axis output image.
            image_outy {numpy.array} -- y-axis output image.
    """
    image_outx = cv2.Sobel(image_in, cv2.CV_64F, 1, 0, ksize=kernel)
    image_outy = cv2.Sobel(image_in, cv2.CV_64F, 0, 1, ksize=kernel)
    return image_outx, image_outy

