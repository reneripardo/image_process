from image_process.ct_processing.ct_image import morpho_erode, morpho_dilate, morpho_close, morpho_open

import argparse
import matplotlib.pyplot as plt
import cv2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example3.tif',
                    help='path image example')
    ap.add_argument('-i2', '--path_image2', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example4.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    image_input = cv2.imread(args['path_image'],0)
    image_input2 = cv2.imread(args['path_image2'], 0)

    # Morphological Transformations
    image_erode = morpho_erode(image_input, 5)
    image_dilate = morpho_dilate(image_input, 5)

    plt.subplot(131), plt.imshow(image_input, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(image_erode, cmap='gray')
    plt.title('Erosão'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(image_dilate, cmap='gray')
    plt.title('Dilatação'), plt.xticks([]), plt.yticks([])
    plt.show()

    image_close = morpho_close(image_input2, 5)
    image_open = morpho_open(image_input2, 5)

    plt.subplot(131), plt.imshow(image_input2, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(image_close, cmap='gray')
    plt.title('Fechamento'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(image_open, cmap='gray')
    plt.title('Abertura'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()