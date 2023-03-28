import cv2
import numpy as np

k = 0.7

if __name__=="__main__":
    img = cv2.imread('human.jpg', cv2.IMREAD_COLOR)
    averageBlur = cv2.blur(img,(15,15))
    mediumBlur = cv2.medianBlur(img,15)

    cv2.imshow("origin",img)
    cv2.imshow("averageBlur",averageBlur)
    cv2.imshow("mediumBlur",mediumBlur)
    cv2.imwrite('averageBlur.jpg', averageBlur)
    cv2.imwrite('mediumBlur.jpg', mediumBlur)

    unsharpMaskingAverage = cv2.addWeighted(img,k+1,averageBlur,-k,0)
    unsharpMaskingMedian = cv2.addWeighted(img,k+1,mediumBlur,-k,0)
    cv2.imshow("unsharpMaskingAverage",unsharpMaskingAverage.astype(np.uint8))
    cv2.imshow("unsharpMaskingMedian",unsharpMaskingMedian.astype(np.uint8))
    cv2.imwrite('unsharpMaskingAverage.jpg', unsharpMaskingAverage.astype(np.uint8))
    cv2.imwrite('unsharpMaskingMedian.jpg', unsharpMaskingMedian.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
