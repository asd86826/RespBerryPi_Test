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
  while(True):
    if (q.empty() == False) :
      cx = q.get()
      print(cx)
    else :
      print('Empty')
    time.sleep(0.01)

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
V = td.Thread(target = Job_PWM,args = (q,))
V.start()
B_cx = 0

while(__name__ == '__main__'):
  Vision_()
  thresh = qT.get()
  cv2.imshow('frame', thresh)
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break
    cap.release()
    cv2.destroyAllWindows()

