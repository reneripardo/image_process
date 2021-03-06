# from image_process.ct_processing.ct_image import


import argparse
import matplotlib.pyplot as plt
import cv2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--path_image', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example.tif',
                    help='path image example')
    ap.add_argument('-i2', '--path_image2', default='E:\\google_drive\\github\\repositories\\image_process\\images\\img_example2.tif',
                    help='path image example')

    args = vars(ap.parse_args())

    image_input = cv2.imread(args['path_image'],0)
    image_input2 = cv2.imread(args['path_image2'], 0)


if __name__ == "__main__":
    main()