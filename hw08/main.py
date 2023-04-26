import cv2


if __name__=='__main__':
    # 讀取圖像
    img = cv2.imread('flower.jpeg', 0)

    # 應用Otsu閾值處理
    th1, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # 顯示圖像
    cv2.imshow('Original', img)
    cv2.imshow('Otsu Thresholded', th2)
    cv2.imwrite('Otsu Thresholded.jpg', th2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
