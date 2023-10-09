import cv2
import time
import numpy as np
#a function to show pictures
def show(i):
    cv2.namedWindow("img",0)
    cv2.resizeWindow("img",5440,3648)
    cv2.imshow("img",i)
    cv2.waitKey(0)
for i in range(1,9):
    #import pirctures
    #number = str(input("Please input the number of the picture:"))
    name = 'C:/huwendi/Tumours/'+str(i)+'.jpg'
    #print(name)
    img = cv2.imread(name)
    #process pictures
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,img1=cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)
    kernal = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(img1,kernal,0)
    #show(img1)
    #identify cells
    circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT_ALT, 1.5, 50, param1=1000, param2=0.1, minRadius=50, maxRadius=1000)
    #mark
    if str(circles) != 'None':
        for i in range(len(circles[0])):
            x = int(int(circles[0][i][0]))
            y = int(circles[0][i][1])
            r = int(int(circles[0][i][2]))
            pt1 = (x-r,y-r)
            pt2 = (x+r,y+r)
            cv2.rectangle(img,pt1,pt2,(255,255,0),20,4) 
        #show(img)
        word = str('There are '+str(len(circles[0]))+' tumour cells in the picture.')
        if len(circles[0])<=0:
            word = str(word+'This sample is healthy')
        else:
            word = str(word+'This sample is likely to have a tumour.')
    else:
        word = 'There is no tumour cells in this picture.'+'This sample is healthy.'
    font = cv2.FONT_HERSHEY_DUPLEX  # 设置字体
    img = cv2.putText(img,word, (20, 100), font, 1, (255,255,255), 1)
    #show(img)
    cv2.imwrite('C:/huwendi/Tumours output/'+str(i)+'.jpg',img)
#This program is only a demo.The accuracy may not be so high.
#made by Hertza Hu

   


