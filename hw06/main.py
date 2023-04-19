import numpy as np
import cv2
import random
import math
import matplotlib.pyplot as plt


sigma = 5
mu = 0

def generateImage(imgRow, imgCol):
    img = np.full((imgRow, imgCol), 100, np.uint8)

    return img

def calculateZ():
    r = random.random()
    fi = random.random()
    z1 = sigma * math.sqrt(-2 * math.log(r)) * math.cos(2 * math.pi * fi)
    z2 = sigma * math.sqrt(-2 * math.log(r)) * math.sin(2 * math.pi * fi)

    return z1, z2

def inspect(val, z):
    if val+z > 255:
        return 255
    elif val+z < 0:
        return 0

    return val+z

if __name__ == "__main__":
    img = generateImage(500, 500)
    cv2.imshow('Image', img)
    cv2.imwrite('Origin.png', img)
    GNImage = img.copy()

    for row in range(GNImage.shape[0]):
        for col in range(0, GNImage.shape[1]-1, 2):
            z1, z2 = calculateZ()
            GNImage[row, col] = inspect(GNImage[row, col], z1)
            GNImage[row, col+1] = inspect(GNImage[row, col+1], z2)

    # generate histogram
    plt.hist(img.flatten(), bins=256, range=(0, 256))
    plt.savefig('origin_histogram.png')
    plt.clf()
    plt.hist(GNImage.flatten(), bins=256, range=(0, 256))
    plt.savefig('GaussianNoise_histogram.png')

    cv2.imshow('Gaussian Noise Image', GNImage)
    cv2.imwrite('Gaussian Noise.png', GNImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()