import cv2
import numpy as np


def myThreshold(img):
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return thresh

if __name__ == '__main__':
    img = cv2.imread('flower.jpeg', cv2.IMREAD_GRAYSCALE)
    threshold= myThreshold(img)

    cv2.imshow('Flower', img)
    cv2.imshow('Thresholded', threshold)
    cv2.imwrite('Thresholded.png', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()