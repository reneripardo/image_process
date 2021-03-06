import argparse
import matplotlib.pyplot as plt
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\img_example_input.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    img = cv2.imread(args['path_image'], 0)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Imagem'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Imagem'), plt.xticks([]), plt.yticks([])
    plt.show()




if __name__ == "__main__":
    main()