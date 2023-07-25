import cv2
import matplotlib.pyplot as plt
import numpy as np
vc = cv2.VideoCapture('C:/huwendi/Python/competition1.mp4')
out = cv2.VideoWriter('C:/huwendi/Python/outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 33, (1904,912))
ret,frame = vc.read()
while 1<2:
    ret,frame = vc.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #转换为HSV格式(色调，饱和度，亮度)
    low_blue = np.array([[100,120,120]])
    high_blue = np.array([[124,255,255]])   #设定阈值
    mask=cv2.inRange(hsv,low_blue,high_blue)  #进行掩模运算
    res = cv2.bitwise_and(frame,frame,mask=mask)
    ret,binary = cv2.threshold(mask,25,255,cv2.THRESH_BINARY)
    kernal = np.ones((4,4),np.uint8)
    dilate = cv2.dilate(mask,kernal,iterations=4)
    kernal1 = np.ones((4,4),np.uint8)
    erosion = cv2.dilate(dilate,kernal1,iterations=3)
    contours,a = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    s = cv2.drawContours(frame,contours,-1,(0,0,255),2)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    out.write(s)
    #cv2.imshow('image',s)
    #cv2.resizeWindow ( "image",1904,912)
    #if cv2.waitKey(100) & 0XFF == 27:
        #break

    #sobelx = cv2.Sobel(erosion,cv2.CV_64F,1,0,ksize=5)
    #sobelx = cv2.convertScaleAbs(sobelx)
    #sobely = cv2.Sobel(erosion,cv2.CV_64F,0,1,ksize=5)
    #sobely = cv2.convertScaleAbs(sobely)
    #sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
    #contours,a = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #cnt = contours[0]
    #x,y,w,h = cv2.boundingRect(cnt)
    #img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    #sobelxy = cv2.cvtColor(binary,cv2.CO)
    #final = frame+sobelxy
    #cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    #cv2.imshow('image',img)
    #cv2.resizeWindow ( "image",1904,912)
    #if cv2.waitKey(100) & 0XFF == 27:
        #break
vc.release()
out.release()
cv2.destroyAllWindows
