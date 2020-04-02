import numpy as np


def low_pass_filter(img, frequency):
    # 先进行傅里叶变换
    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)

    # 进行低通滤波
    rows, cols = img.shape
    mask = np.zeros((rows, cols), np.uint8)
    center_row, center_col = int(rows / 2), int(cols / 2)
    cut_rows, cut_cols = int(center_row * frequency / 100), int(center_col * frequency / 100)
    mask[center_row - cut_rows: center_row + cut_rows, center_col - cut_cols: center_col + cut_cols] = 1

    f_shift = f_shift * mask

    # 逆变换还原图片
    i_shift = np.fft.ifftshift(f_shift)
    new_img = np.fft.ifft2(i_shift)
    new_img = np.abs(new_img)
    return new_img
