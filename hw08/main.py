import cv2
import numpy as np

def otsu_threshold(img):
    # 計算圖像灰度直方圖
    hist, bins = np.histogram(img.ravel(), 256, [0,256])

    # 計算圖像總像素數
    total_pixels = img.shape[0] * img.shape[1]

    # 初始化類間方差、閾值、前景像素數、背景像素數
    inter_class_variance = 0
    threshold = 0
    foreground_pixels = 0
    background_pixels = 0

    # 遍歷每一個灰度級
    for i in range(256):
        # 計算前景和背景的像素數
        foreground_pixels += hist[i]
        background_pixels = total_pixels - foreground_pixels

        # 計算前景和背景的平均灰度值
        if foreground_pixels == 0:
            foreground_mean = 0
        else:
           foreground_mean = np.sum([j * hist[j] for j in range(i+1)]) / foreground_pixels

        if background_pixels == 0:
            background_mean = 0
        else:
            background_mean = np.sum([j * hist[j] for j in range(i+1, 256)]) / background_pixels

        # 計算類間方差
        curr_inter_class_variance = (foreground_pixels / total_pixels) * (background_pixels / total_pixels) * ((foreground_mean - background_mean) ** 2)

        # 找到最大的類間方差以及對應的閾值
        if curr_inter_class_variance > inter_class_variance:
            inter_class_variance = curr_inter_class_variance
            threshold = i

    # 應用閾值處理
    _, output = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    return output


if __name__=='__main__':
    # 讀取圖像
    img = cv2.imread('flower.jpeg', 0)

    # 應用Otsu閾值處理
    threshold = otsu_threshold(img)

    # 顯示圖像
    cv2.imshow('Original', img)
    cv2.imshow('Otsu Thresholded', threshold)
    cv2.imwrite('Otsu Thresholded.jpg', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
