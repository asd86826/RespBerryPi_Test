import cv2
import numpy as np
import multiprocessing as mp
import time

cap = cv2.VideoCapture(0)

def Vision_ (q_Vision) :
  ret1, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  result = cv2.GaussianBlur(gray ,(5,5),1.5 )
  ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY)
  q_Vision.put(thresh)

def Vision_Line(q_thresh) :
  thresh = q_thresh
  cnt = thresh[0]
  M = cv2.moments(cnt)
  area = M['m00']
  cx = int(M['m10']/M['m00'])
  cy = int((M['m01']+1)/(M['m00']+1))
  print(cy, cx)
  if 315< cy <325:
    print(cy, 'mid')
  elif cy < 315:
    print(320-cy,'right')
  else:
    print(cy-320, 'left')

q_Vision = mp.Queue()
q_thresh = mp.Queue()
V1 = mp.Process(target = Vision_ , args = (q_Vision,))
V2 = mp.Process(target = Vision_Line , args = (q_thresh,))
V1.start()
V2.start()

while(__name__ == '__main__'):
  tStart = time.time()

  thresh = q_Vision.get()
  cv2.imshow('frame', thresh)
  tEnd = time.time()
  print(tEnd - tStart)
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break

cap.release()

cv2.destroyAllWindows()
