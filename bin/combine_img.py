#!/usr/bin/env python3


import sys
import cv2 as cv
import numpy as np


def combine(f1, f2):
    img1 = cv.imread(f1)
    img2 = cv.imread(f2)

    img2 = img2[50:850, 50:850, :]

    new_img = np.zeros((800, 800, 3))
    new_img[:, :, :] = img2
    new_img[30:204, 30:280, :] = img1

    C=np.where(new_img == 0)

    for i in range(0, len(C[0])):
        new_img[C[0][i], C[1][i], :] = img2[C[0][i], C[1][i], :]


    cv.imwrite(sys.argv[3], new_img)


if __name__ == '__main__':
    combine(sys.argv[1], sys.argv[2])