import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread('human.jpg')
    cv2.imshow("before",img)
    for row in img:
        for pixel in row:
            val = (pixel[0]/3+pixel[1]/3+pixel[2]/3)
            pixel[0]=val
            pixel[1]=val
            pixel[2]=val

    cv2.imwrite('output.jpg', img)
    cv2.imshow("after",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()