import numpy as np
import cv2

def generateRectangleImage(imgRow, imgCol):
    img = np.zeros((imgRow, imgCol, 3), np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if row>=imgRow/3 and row<=imgRow/3*2 and col>=imgCol/3 and col<=imgCol/3*2:
                img[row, col] = [255, 255, 255]

    return img

def rotateImage(img, angle):
    newImg = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            # 旋轉by angle度
            x = (col - img.shape[1]/2) * np.cos(np.deg2rad(angle)) - (row - img.shape[0]/2) * np.sin(np.deg2rad(angle)) + img.shape[1]/2
            y = (col - img.shape[1]/2) * np.sin(np.deg2rad(angle)) + (row - img.shape[0]/2) * np.cos(np.deg2rad(angle)) + img.shape[0]/2

            # Check
            if x>=0 and x<img.shape[1] and y>=0 and y<img.shape[0]:
                newImg[row, col] = img[int(y), int(x)]
    return newImg

if __name__ == "__main__":
    img = generateRectangleImage(300, 300)
    cv2.imshow('RectangleImage', img)
    newImg = rotateImage(img, 30)
    cv2.imshow('RotatedImage', newImg)

    cv2.imwrite('RectangleImage.jpg', img)
    cv2.imwrite('RotatedImage.jpg', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()