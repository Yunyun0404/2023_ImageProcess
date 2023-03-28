import cv2
import numpy as np

k = 0.7

if __name__=="__main__":
    img = cv2.imread('human.jpg',cv2.IMREAD_GRAYSCALE)
    averageBlur = cv2.blur(img,(9,9))
    mediumBlur = cv2.medianBlur(img,9)

    cv2.imshow("origin",img)
    cv2.imshow("blur",averageBlur)
    cv2.imshow("mediumBlur",mediumBlur)
    cv2.imwrite('blur.jpg', averageBlur)
    cv2.imwrite('mediumBlur.jpg', mediumBlur)

    unsharpMaskingAverage = (img - averageBlur)*k + img
    unsharpMaskingMedian = (img - mediumBlur)*k + img
    cv2.imshow("unsharpMaskingAverage",unsharpMaskingAverage.astype(np.uint8))
    cv2.imshow("unsharpMaskingMedian",unsharpMaskingMedian.astype(np.uint8))
    cv2.imwrite('unsharpMaskingAverage.jpg', unsharpMaskingAverage.astype(np.uint8))
    cv2.imwrite('unsharpMaskingMedian.jpg', unsharpMaskingMedian.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
