import cv2
import numpy as np
import multiprocessing as mp
import time

cap = cv2.VideoCapture(0)

def Vision_Line () :
    
  while(__name__ =='__main__'):
    frame = q_V.get()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.GaussianBlur(gray ,(5,5),1.5 )
    ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY)
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
    cx = int(M['m10']/M['m00'])
    cy = int((M['m01']+1)/(M['m00']+1))
    q_Line.put(cx)
    
    
q_Line = mp.Queue()
q_V = mp.Queue()

V1 = mp.Process(target = Vision_Line )
V1.start()

while(__name__ == '__main__'):
    
  ret1, frame = cap.read()
  q_V.put(frame)
  cv2.imshow('frame', frame)
  cx = q_Line.get()
  print(cx)
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break

cap.release()

cv2.destroyAllWindows()
