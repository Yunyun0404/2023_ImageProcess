import cv2
import numpy as np


def myThreshold(img, threshold_value, max_value, threshold_type):
    output = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if threshold_type == cv2.THRESH_BINARY:
                if img[i,j] > threshold_value:
                    output[i,j] = max_value
                else:
                    output[i,j] = 0
            elif threshold_type == cv2.THRESH_BINARY_INV:
                if img[i,j] > threshold_value:
                    output[i,j] = 0
                else:
                    output[i,j] = max_value
    return output

if __name__ == '__main__':
    img = cv2.imread('flower.jpeg', cv2.IMREAD_GRAYSCALE)
    threshold= myThreshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Flower', img)
    cv2.imshow('Thresholded', threshold)
    cv2.imwrite('Thresholded.png', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()