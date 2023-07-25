import cv2
import numpy as np
import sys
img = cv2.imread('C:/huwendi/Python/aimlab5.jpg',1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #转换为HSV格式(色调，饱和度，亮度)
low_red = np.array([[156,43,46]])
high_red = np.array([[180,255,255]])   #设定阈值
mask=cv2.inRange(hsv,low_red,high_red)  #进行掩模运算
#res = cv2.bitwise_and(img,img,mask=mask)    #进行位运算
#blur = cv2.blur(res,(3,3))  #设置降噪范围
#gray = cv2.cvtColor(blur,cv2.COLOR_HSV2BGR)    #HSV转BGR
#gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)    #BGR转灰度
#two = cv2.threshold(gray,100,255,CV_THRESH_BINARY)
ret,binary = cv2.threshold(mask,25,255,cv2.THRESH_BINARY)   #灰度转二值化

#cv2.imshow('ires',binary)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
s = np.array(binary)

kernel = np.ones((3,3), dtype=np.uint8)
erosion = cv2.erode(binary, kernel, iterations=1)
#rusty = np.hstack((binary, erosion))   #腐蚀

kernel = np.ones((3,3), dtype=np.uint8)
dilate = cv2.dilate(erosion, kernel, 3)

cv2.imshow('irusty',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

list_pixel = []

array_dilate = np.array(dilate)
for first in range(1080):
    for second in range(1920):
        if array_dilate[first][second] == 255:
            for i in range(first,first+100):
                if array_dilate[i][second]:
                    list_pixel.append(i)
            if len(list_pixel) >=20:
                final = (first+list_pixel[-1])/2
                print(second,final)
                r = (list_pixel[-1]-first)/2
                #left_x = second-r
                #left_y = first
                #right_x = second+r
                #right_y = list_pixel[-1]
                sys.exit(0)
            else:
                list_pixel = []
        else:
            continue
        
            


                


#cv2.imshow('image',r)
#cv2.waitKey(30)
#cv2.destroyAllWindows()
