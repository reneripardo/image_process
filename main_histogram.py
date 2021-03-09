import argparse
import matplotlib.pyplot as plt
import cv2
import locale
locale.setlocale(locale.LC_NUMERIC, "deu_deu")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example5.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    image_input = cv2.imread(args['path_image'],0)

    # Equalization
    image_equ = cv2.equalizeHist(image_input)

    # Otsu's thresholding
    _, image_input_otsu = cv2.threshold(image_input, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _, image_equ_otsu = cv2.threshold(image_equ, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    plt.subplot(221), plt.imshow(image_input, cmap='gray')
    plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(image_equ, cmap='gray')
    plt.title('Com equalização'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(image_input_otsu, cmap='gray')
    plt.title('Limiarização com Otsu \n na imagem original'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(image_equ_otsu, cmap='gray')
    plt.title('Limiarização com Otsu \n na imagem com equalização'), plt.xticks([]), plt.yticks([])
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