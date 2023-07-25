import cv2
import numpy as np
import sys
import pyautogui as auto
from PIL import ImageGrab as gr
import time
import win32api as api
import win32con
import pydirectinput as direct
from numba import jit


#def screen():
#    img = gr.grab()
#    array = np.array(img)
 #   image = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
#    return(image)

def picture():
    img = gr.grab()
    #img.save('C:/huwendi/Python/aimlab7.jpg')
    array = np.array(img)
    image = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    #image = cv2.imread('C:/huwendi/Python/aimlab4.jpg',1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #转换为HSV格式(色调，饱和度，亮度)
    low_red = np.array([[156,43,46]])
    high_red = np.array([[180,255,255]])   #设定阈值
    mask=cv2.inRange(hsv,low_red,high_red)  #进行掩模运算
    ret,binary = cv2.threshold(mask,25,255,cv2.THRESH_BINARY)   #灰度转二值化
    s = np.array(binary)
    kernel = np.ones((3,3), dtype=np.uint8)
    erosion = cv2.erode(binary, kernel, iterations=1)
    kernel = np.ones((3,3), dtype=np.uint8)
    dilate = cv2.dilate(erosion, kernel, 3)
    return(np.array(dilate))
def move(list_in):
    direct.moveTo(int(0.6640625*list_in[0]),int(0.6712*list_in[1])) 
    api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05) 
    api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

@jit(nopython = True)
def recog(dilate):
    list_pixel = [0]
    first = 0
    second = 0
    array_dilate = dilate
    for first in range(1080):
        for second in range(1920):
            if array_dilate[first][second] == 255:
                for i in range(first,first+100):
                    if array_dilate[i][second] == 255:
                        list_pixel.append(i)
                if len(list_pixel) >=20:
                    final = (first+list_pixel[-1])/2
                    print(int(0.6640625*second),int(0.6640625*final))
                    #auto.moveTo(second,first)
                    #auto.dragTo(second,first,0.05)
                    list_out = [second,int(final)]
                    return(list_out)
                else:
                    list_pixel = [0]
            else:
                continue

    
time.sleep(5)
while(1):
    move(recog(picture()))
    #recog(picture())



            


                


