import argparse
import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example5.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    image_input = cv2.imread(args['path_image'],0)

    image_equ = cv2.equalizeHist(image_input)
    # image_equ = np.hstack((op_equ, op_equ))  # stacking images side-by-side

    plt.subplot(121), plt.imshow(image_input, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(image_equ, cmap='gray')
    plt.title('Com equalização'), plt.xticks([]), plt.yticks([])
    plt.show()


    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax0, ax1 = axes.flatten()
    ax0.hist(image_input.flatten(), 256, [0, 256], color='black')
    ax0.set_title('Histograma da imagem original')
    ax1.hist(image_equ.flatten(), 256, [0, 256], color='black')
    ax1.set_title('Histograma da imagem original com equalização')
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()