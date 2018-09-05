import threading as td
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO
import multiprocessing as mp
import Queue
import sys
from multiprocessing import Process, Value

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
my_pwm12=GPIO.PWM(12,72)
my_pwm12.start(10.8)


def Job_PWM (cx) :
  while(__name__ == '__main__'):
    if 240< cx <400:
      print(cx, 'mid')
      my_pwm12.ChangeDutyCycle(10.2)
    elif cx > 400:
      print(320-cx,'right')
      my_pwm12.ChangeDutyCycle(10.4)
    else:
      print(cx-320, 'left')
      my_pwm12.ChangeDutyCycle(9.7)
    if cv2.waitKey(1) & 0xFF ==ord('c'):
      break



def Vision_ () :
  cap = cv2.VideoCapture(0)
  global q
  red = (0, 0,255)
  while (1) :
    ret1, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.GaussianBlur(gray ,(5,5),1.5 )
    cv2.line(result, (240, 0), (240, 480) , red ,2)
    cv2.line(result, (400, 0), (400, 480) , red ,2)
    ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY_INV)
    _, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)

    qT.put(thresh)
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
    q.put(cx)
    cv2.circle(thresh, (cx,cy), 2, red, 2)
    print(cy, cx)
    cv2.imshow('frame', thresh)
    if cv2.waitKey(1) & 0xFF ==ord('c'):
      cap.release()
      cv2.destroyAllWindows()
      break

V = td.Thread(target = Vision_ )
V.start()
q = Queue.Queue()
qT = Queue.Queue()

#alive.value = True

while(__name__ == '__main__'):
  tStart = time.time()
  cx = q.get()
  thresh = qT.get()
  Job_PWM(cx)
  tEnd = time.time()
  print(tEnd - tStart)
  if cv2.waitKey(1) & 0xFF == ord('c'):
#    alive.value = False
    cap.release()
    cv2.destroyAllWindows()
    break
