import cv2
import Adafruit_PCA9685
import numpy as np
import multiprocessing as mp
from multiprocessing import Process, Value
import time
import threading as td
import Queue
import sys

pwm = Adafruit_PCA9685.PCA9685()
cap = cv2.VideoCapture(0)

def Job_PWM (q) :
  eO = 0
  I_R = 0
  I_L = 0
  Np = 1
  Nd = 0.1125 #0.125
  while(__name__ == '__main__'):
    cx = q.get()
    if abs(320-cx) < 200:
      Np = 0
    else:
      Np = 1
    print(Np)
    if 240 < cx < 400:
      eO = 0
      Np = 0
      pwm.set_pwm(15 ,0 ,448)
      print(cx,'mid')
    elif cx > 400:
      cx_R = 0
      eR = (cx-400)
      cx_R = (eR*0.067)*Np #640-400 = 240 /14 = 20 Kp
#      cx_R = (eR/12)
      if(I_R > 5):
        I_R =(I_R+eR)*0.01
      else:
        I_R = 5
      D_R = (eR-eO)*Nd # Kd/8
      if D_R < -10 :
        D_R = -10
      PID_R = 448+(cx_R+D_R)
      pwm.set_pwm(15 ,0 ,int(PID_R))
      eO = eR
      print(PID_R, D_R , cx ,'right')

    else:
      cx_L = 0
      eL = (240-cx)
      cx_L = (eL*0.083)*Np # 240/16 = 15 PWM15 = 50
#      cx_L = (eL/15)
      if(I_L > 5):
        I_L = I_L+eL
      else:
        I_L = 5
      D_L = (eL-eO)*Nd
      if D_L < -10 :
        D_L = -10
      PID_L = 448-(cx_L+D_L)
      pwm.set_pwm(15 ,0 ,int(PID_L))
      eO = eL
      print(PID_L, D_L , cx ,'left')

def Vision_ () :
    global B_cx
    ret1, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.GaussianBlur(gray ,(5,5),1.5 )
    cv2.line(result, (280, 0), (280, 480),(0, 0, 255), 2)
    cv2.line(result, (360, 0), (360, 480),(0, 0, 255), 2)
    ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY_INV)
    _, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)
    max_area = 0
    max_cnt = 0
    for i in range(len(contours)):
      cnt = contours[i]
      area = cv2.contourArea(cnt)
      if (area>max_area):
        max_area = area
        max_cnt = cnt
    M = cv2.moments(max_cnt)
    cx = int((M['m10']+1)/(M['m00']+1))
    cy = int((M['m01']+1)/(M['m00']+1))
    if (max_area < 10000):
      if B_cx > 320:
        cx = 630
      else:
        cx = 10
    q.put(cx)
    cv2.circle(thresh, (cx,cy), 2,(0, 0, 255), 2)
    qT.put(thresh)
    B_cx = cx
    if max_area>150000 :
      print ('Stop' , max_area)


pwm.set_pwm_freq(67)
q = Queue.Queue()
qT = Queue.Queue()
#N = td.Thread(target = Job_N)
V = td.Thread(target = Job_PWM,args = (q,))
#N.start()
V.setDaemon(True)
V.start()
B_cx = 0

try:
  while(__name__ == '__main__'):
    Vision_()
    thresh = qT.get()

finally:
  cap.release()
  cv2.destroyAllWindows()
