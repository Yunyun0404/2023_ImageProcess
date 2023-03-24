import cv2
import numpy as np

D1 = np.array([[0,56],
               [84,28]])
D2 = np.array([[0,128,32,160],
               [192,64,224,96],
               [48,176,16,144],
               [240,112,208,80]])

if __name__ == "__main__":
    img = cv2.imread('human.jpg',cv2.IMREAD_GRAYSCALE)
    imgB = img.copy()

    cv2.imshow("before",img)
    # (A)
    for row in img:
        # padding
        while row.size%4!=0:
            row.append(0)
        # dithering
        for index in range(0,row.size):
            row_position=row.size%4
            col_position=index%4

            # print(pixel)
            if D2[row_position][col_position]>row[index]:
                row[index]=0
            else:
                row[index]=255
    # (B)
    for row in range(0,np.size(imgB,0)):
        Q = imgB//85

        # dithering
        for index in range(0,np.size(imgB,1)):
            row_position=row%2
            col_position=index%2

            # print(pixel)
            if imgB[row][index]-85*Q[row][index] > D1[row_position][col_position]:
                imgB[row][index]=Q[row][index]+1
            else:
                imgB[row][index]=Q[row][index]

            imgB[row][index]*=85

    cv2.imwrite('output.jpg', img)
    cv2.imwrite('outputB.jpg', imgB)
    cv2.imshow("(A)",img)
    cv2.imshow("(B)",imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()