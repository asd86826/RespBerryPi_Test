import cv2
import numpy as np
import multiprocessing as mp
from multiprocessing import Process, Value
import time
import threading as td
import Queue
import sys

cap = cv2.VideoCapture(0)


def Vision_ () :
  global q
  while (__name__ == '__main__') :
    ret1, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.GaussianBlur(gray ,(5,5),1.5 )
    ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY_INV)
    _, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)
    q.put(contours)
    qT.put(thresh)
    #if cv2.waitKey(1) & 0xFF ==ord('c'):

def Vision_Line(contours) :
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

  print(cy, cx)

V = td.Thread(target = Vision_ )
V.start()
q = Queue.Queue()
qT = Queue.Queue()

#alive.value = True

while(__name__ == '__main__'):
  tStart = time.time()

  contours = q.get()
  thresh = qT.get()
  Vision_Line(contours)
  cv2.imshow('frame', thresh)
  tEnd = time.time()
  print(tEnd - tStart)
  if cv2.waitKey(1) & 0xFF == ord('c'):
#    alive.value = False
    break

cap.release()

cv2.destroyAllWindows()
