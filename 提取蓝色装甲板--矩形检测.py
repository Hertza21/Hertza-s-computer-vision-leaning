import cv2
import matplotlib.pyplot as plt
import numpy as np
vc = cv2.VideoCapture('C:/huwendi/Python/xiaotuoluo.mp4')
out = cv2.VideoWriter('C:/huwendi/Python/outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 33, (1904,1080))
ret,frame = vc.read()
#img = cv2.imread('C:/huwendi/Python/ep.jpg')
while 1<2:
    ret,frame = vc.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #转换为HSV格式(色调，饱和度，亮度)
    low_blue = np.array([[100,150,100]])
    high_blue = np.array([[124,255,255]])   #设定阈值
    mask=cv2.inRange(hsv,low_blue,high_blue)  #进行掩模运算
    res = cv2.bitwise_and(frame,frame,mask=mask)
    ret,binary = cv2.threshold(mask,25,255,cv2.THRESH_BINARY)
    kernal = np.ones((4,4),np.uint8)
    dilate = cv2.dilate(mask,kernal,iterations=5)
    kernal1 = np.ones((4,4),np.uint8)
    erosion = cv2.dilate(dilate,kernal1,iterations=0)
    contours = cv2.findContours(erosion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    list_output = []
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',erosion)
    cv2.waitKey(30)
    for k in range(len(contours[0])):
        listx = []
        listy = []
        s = contours[0][k]
        for i in range(len(contours[0][k])):
            listx.append(s[i][0][0])
            #print(i)
        for j in range(len(contours[0][k])):
            listy.append(s[j][0][1])
        listx.sort()
        listy.sort()
        if (listx[-1]-listx[0])/(listy[-1]-listy[0])>=1 and (listx[-1]-listx[0])/(listy[-1]-listy[0])<=3 and listx[-1]-listx[0]>10 and listx[-1]-listx[0]<=900 and listy[-1]-listy[0]>5 and listy[-1]-listy[0]<=990:
            list_output.append(listx[0])
            list_output.append(listx[-1])
            list_output.append(listy[0])
            list_output.append(listy[-1])
            for c in range(int(len(list_output)/4)):
                img = cv2.rectangle(frame,(list_output[c],list_output[c+2]),(list_output[c+1],list_output[c+3]),(0,0,255),2)
            out.write(img)
            
            list_output =[]
            break
        else:
            out.write(frame)
            break
    #print(len(list_output))
    
    
#contours = np.array(contours,np.int32)

#for l in range(len(list_output)):
#    s = cv2.drawContours(img,contours,list_output[l],(0,0,255),2)
#sobelxy = cv2.cvtColor(binary,cv2.CO)
#final = frame+sobelxy



cv2.destroyAllWindows
vc.release()
out.release()
    