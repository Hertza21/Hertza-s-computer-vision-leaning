#碰撞模拟
#初始化
import numpy as np
import cv2 
img1 = np.zeros((600,1200,3),np.uint8)
img1[:] = [255,255,255]
cv2.line(img1,(0,300),(1200,300),(0,0,0))
ans = 0
ans1 = 0
#状态显示
def show(x1b,x2b,x1,x2):
    global ans1
    global M1
    global M2
    word = 'Collide times'+str(ans1)+' Ma is'+str(M1/M2)+'times more than Mb'
    cv2.rectangle(img1,(0,0),(1200,200),(255,255,255),thickness = -1)
    cv2.rectangle(img1,(x1b,280), (x1b+20,299), (255, 255, 255), thickness = -1)
    cv2.rectangle(img1, (x2b,280), (x2b+20,299), (255, 255, 255),thickness = -1)
    cv2.rectangle(img1,(x1,280), (x1+20,299), (255, 0, 0), thickness = -1)
    cv2.rectangle(img1, (x2,280), (x2+20,299), (0,0,255),thickness = -1)
    font = cv2.FONT_HERSHEY_DUPLEX  # 设置字体
    cv2.putText(img1,word, (20, 100), font, 1, (0,0,0), 1)
    cv2.namedWindow('img1', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('img1',img1)
    cv2.waitKey(10)
#运动学数据模拟
def cal(m1,m2,x1,x2,v1,v2):
    global ans
    global ans1
    if x1-x2<=20.1 and -19.9<=x1-x2 and ans == 0:
        #print(x1,x2,((m1-m2)/(m1+m2))*v1+(2*m2/(m1+m2)*v2),((m2-m1)/(m1+m2))*v2+(2*m1/(m1+m2)*v1))
        ans = 1
        ans1 = ans1+1
        return(x1,x2,((m1-m2)/(m1+m2))*v1+(2*m2/(m1+m2)*v2),((m2-m1)/(m1+m2))*v2+(2*m1/(m1+m2)*v1))
    elif x1<0 and ans==0:
        ans = 1
        ans1 = ans1+1
        return(x1,x2,-v1,v2)
    elif x2<0 and ans==0:   
        ans = 1
        ans1 = ans1+1
        return(x1,x2,v1,-v2) 
    else:
        #print(x1+v1*0.01,x2+v2*0.01,v1,v2)
        ans = 0
        return(x1+v1*0.01,x2+v2*0.01,v1,v2)
#主程序
M1 = 10000
M2 = 1
s = cal(M1,M2,50,20,-10,0)
while 1:
    p1 = s[0]
    p2 = s[1]
    s = cal(M1,M2,s[0],s[1],s[2],s[3])
    show(int(p1),int(p2),int(s[0]),int(s[1]))
    if s[0]-s[1]>=100 and s[2]>=0 and s[3]>=0 and s[2]>s[3]:
        cv2.waitKey(0)
        break
print(ans1)
    


