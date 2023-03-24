import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

if __name__ == '__main__':
    img_gray = cv2.imread('flower2.jpeg', cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread('flower2.jpeg', cv2.IMREAD_COLOR)

    cv2.imshow('before', img_color)
    # 1. gray image
    table = []
    for i in range(256):
        table.append(0)
    histDataInput = []
    histDataOutput = []

    for row in img_gray:
        for index in range(0,row.size):
            val = row[index]
            histDataInput.append(val)
            table[val] += 1
            table[val] = float(table[val])

    # 生成InputHE直方圖
    plt.hist(histDataInput, color = 'lightblue', cumulative = False)
    plt.title('Input Histogram')
    plt.xlabel('Gray Level')
    plt.ylabel('Number of Pixels')
    plt.savefig('./InputHE', transparent=False, bbox_inches='tight', pad_inches=1.0)

    for index in range(256):
        table[index] /= img_gray.size
        table[index] *= 255

    table[0] = round(table[0])
    for i in range(1,256):
        table[i] += table[i-1]
        table[i] = round(table[i])

    for row in img_gray:
        for index in range(0,row.size):
            row[index] = table[row[index]]
            histDataOutput.append(row[index])

    # 生成outputHE直方圖
    plt.hist(histDataOutput, density=False, color = 'lightblue', cumulative = False)
    plt.title('Output Histogram')
    plt.savefig('./OutputHE', transparent=False, bbox_inches='tight', pad_inches=1.0)

    # 2. color image
    # 先轉成灰階
    img_colorTogray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    # 用灰階做直方圖均衡(HE)
    table.clear()
    for i in range(256):
        table.append(0)

    for row in img_colorTogray:
        for index in range(0,row.size):
            val = row[index]
            table[val] += 1
            table[val] = float(table[val])

    for index in range(256):
        table[index] /= img_colorTogray.size
        table[index] *= 255

    table[0] = round(table[0])
    for i in range(1,256):
        table[i] += table[i-1]
        table[i] = float(round(table[i]))

    for i in range(1,256):
        table[i] /= i

    # 再把值寫回彩色
    for row in range(np.size(img_color,0)):
        for col in range(np.size(img_color,1)):
            img_color[row][col][0] *= table[ img_colorTogray[row][col] ]
            img_color[row][col][1] *= table[ img_colorTogray[row][col] ]
            img_color[row][col][2] *= table[ img_colorTogray[row][col] ]

    cv2.imwrite('Gray.jpg', img_gray)
    cv2.imwrite('Color.jpg', img_color)
    cv2.imshow('Color', img_color)
    cv2.imshow('Gray', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
