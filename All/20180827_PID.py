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
  Na = 1.1
  while(__name__ == '__main__'):
    cx = q.get()
    if 240 < cx < 400:
      eO = 0
      pwm.set_pwm(15 ,0 ,448)
      print(cx,'mid')

    elif cx > 400:
      cx_R = 0
      eR = (cx-400)
      cx_R = (eR*0.083)*Na #640-400 = 240 /14 = 20 Kp
#      cx_R = (eR/12)
      if(I_R > 5):
        I_R =(I_R+eR)*0.01
      else:
        I_R = 5
      D_R = (eR-eO)*0.2 # Kd/8
      PID_R = 448+(cx_R+D_R)
      pwm.set_pwm(15 ,0 ,int(PID_R))
      eO = eR
      print(PID_R, D_R , I_R ,'right')

    else:
      cx_L = 0
      eL = (240-cx)
      cx_L = (eL*0.067)*Na # 240/16 = 15 PWM15 = 50
#      cx_L = (eL/15)
      if(I_L > 5):
        I_L = I_L+eL
      else:
        I_L = 5
      D_L = (eL-eO)*0.2
      PID_L = 448-(cx_L+D_L)
      pwm.set_pwm(15 ,0 ,int(PID_L))
      eO = eL
      print(PID_L, D_L , I_L ,'left')

def Vision_ () :
    global B_cx
    Ts = time.time()
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
      cx = B_cx
    q.put(cx)
    cv2.circle(thresh, (cx,cy), 2,(0, 0, 255), 2)
    qT.put(thresh)
    B_cx = cx
    Te = time.time()
    print (Te-Ts)
    if max_area>150000 :
      print ('Stop' , max_area)


pwm.set_pwm_freq(67)
q = Queue.Queue()
qT = Queue.Queue()
#N = td.Thread(target = Job_N)
V = td.Thread(target = Job_PWM,args = (q,))
#N.start()
V.start()
B_cx = 0

try:
  while(__name__ == '__main__'):
    Vision_()
    thresh = qT.get()
    if cv2.waitKey(1) & 0xFF == ord('c'):
      break
      cap.release()
      cv2.destroyAllWindows()
finally:
  cap.release()
  cv2.destroyAllWindows()
