import numpy as np
import cv2

def generateRectangleImage(imgRow, imgCol):
    img = np.zeros((imgRow, imgCol, 3), np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if row>=imgRow/3 and row<=imgRow/3*2 and col>=imgCol/3 and col<=imgCol/3*2:
                img[row, col] = [255, 255, 255]

    return img

def getByBilinearInterpolation(image, x, y):
    x1, y1 = int(x), int(y)
    x2, y2 = x1+1, y1+1
    if x2>=image.shape[1]:
        x2 = image.shape[1]-1
    if y2>=image.shape[0]:
        y2 = image.shape[0]-1
    f11 = image[x1][y1]
    f21 = image[x2][y1]
    f12 = image[x1][y2]
    f22 = image[x2][y2]
    return ( f11*(x2-x)*(y2-y) + f21*(x-x1)*(y2-y) + f12*(x2 - x)*(y - y1) + f22*(x-x1)*(y - y1) )

def rotateByBilinearInterpolationImage(img, angle):
    newImg = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            # 旋轉by angle度
            x = (col - img.shape[1]/2) * np.cos(np.deg2rad(angle)) - (row - img.shape[0]/2) * np.sin(np.deg2rad(angle)) + img.shape[1]/2
            y = (col - img.shape[1]/2) * np.sin(np.deg2rad(angle)) + (row - img.shape[0]/2) * np.cos(np.deg2rad(angle)) + img.shape[0]/2

            # Check
            if x>=0 and x<img.shape[1] and y>=0 and y<img.shape[0]:
                newImg[row, col] = getByBilinearInterpolation(img, x, y)
    return newImg

def rotateByNeighborInterpolationImage(img, angle):
    newImg = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            # 旋轉by angle度
            value = np.deg2rad((-1)*angle)
            x = (col - img.shape[1]/2) * np.cos(value) - (row - img.shape[0]/2) * np.sin(value) + img.shape[1]/2
            y = (col - img.shape[1]/2) * np.sin(value) + (row - img.shape[0]/2) * np.cos(value) + img.shape[0]/2

            # Check
            if x>=0 and x<img.shape[1]-1 and y>=0 and y<img.shape[0]-1:
                newImg[round(y),round(x)] = img[row][col]
    return newImg

if __name__ == "__main__":
    img = generateRectangleImage(300, 300)
    cv2.imshow('RectangleImage', img)
    imgByNeighbor = rotateByNeighborInterpolationImage(img, 30)
    cv2.imshow('neighbor interpolation image', imgByNeighbor)
    imgByBilinear = rotateByBilinearInterpolationImage(img, 30)
    cv2.imshow('bilinear interpolation image', imgByBilinear)

    cv2.imwrite('RectangleImage.jpg', img)
    cv2.imwrite('neighbor interpolation image.jpg', imgByNeighbor)
    cv2.imwrite('bilinear interpolation image.jpg', imgByBilinear)
    cv2.waitKey(0)
    cv2.destroyAllWindows()