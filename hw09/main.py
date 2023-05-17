import cv2
import numpy as np

def lantuejoul_skeletonization(image):
    # 將影像轉換為灰度圖
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 初始化骨架
    skeleton = np.zeros(gray.shape, dtype=np.uint8)
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
    prev_skeleton = np.copy(skeleton)

    # 迭代過程，直到沒有像素值改變
    while True:
        opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        temp = cv2.subtract(gray, opened)
        eroded = cv2.erode(gray, kernel)
        skeleton = cv2.bitwise_or(skeleton, temp)
        gray = eroded.copy()

        if cv2.countNonZero(gray)==0:
            break
        if np.equal(skeleton, prev_skeleton).all():
            break

        prev_skeleton = np.copy(skeleton)
        
    return skeleton

if __name__=='__main__':
    # 讀取圖像
    img = cv2.imread('image.png', cv2.IMREAD_COLOR)
    after = lantuejoul_skeletonization(img)

    cv2.imwrite('skeleton.png', after)
    # 顯示圖像
    cv2.imshow('Original', img)
    cv2.imshow('Skeleton', after)
    cv2.waitKey(0)
    cv2.destroyAllWindows()