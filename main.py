from image_process.ct_processing.ct_image import median_filter, mean_filter, gaussian_filter, filter_laplacian, \
    filter_sobel

import argparse
import matplotlib.pyplot as plt
import cv2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\img_example.tif',
                    help='path image example')
    ap.add_argument('-i2', '--path_image2', default='E:\\google_drive\\github\\repositories\\image_process\\img_example2.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    image_input = cv2.imread(args['path_image'],0)
    image_input2 = cv2.imread(args['path_image2'], 0)

    # low pass filter
    image_mean_filter = mean_filter(image_input, 5)
    image_median_filter = median_filter(image_input, 5)
    image_gaussian_filter = gaussian_filter(image_input, 5)

    plt.subplot(221), plt.imshow(image_input, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(image_mean_filter, cmap='gray')
    plt.title('Filtro da média (kernel=5x5)'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(image_median_filter, cmap='gray')
    plt.title('Filtro da mediana (kernel=5x5)'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(image_gaussian_filter, cmap='gray')
    plt.title('Filtro gaussiana (kernel=5x5)'), plt.xticks([]), plt.yticks([])
    plt.show()

    # high pass filter
    image_filter_laplacian = filter_laplacian(image_input2)
    image_sobx, image_soby = filter_sobel(image_input2, 5)

    plt.subplot(221), plt.imshow(image_input2, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(image_filter_laplacian, cmap='gray')
    plt.title('Filtro laplaciano '), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(image_sobx, cmap='gray')
    plt.title('Filtro sobel no eixo X (kernel=5x5)'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(image_soby, cmap='gray')
    plt.title('Filtro sobel no eixo Y (kernel=5x5)'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()