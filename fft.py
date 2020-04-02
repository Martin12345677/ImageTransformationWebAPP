# -*- coding: utf-8 -*-
import numpy as np
import cv2


def fft(img):
    # img = cv2.imread('test.jpeg', 0)

    print(img.shape)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

    dft_shift = np.fft.fftshift(dft)

    result = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    return result
