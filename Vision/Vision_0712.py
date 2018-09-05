import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while(True):
  tStart = time.time()
  ret1, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  result = cv2.GaussianBlur(gray ,(5,5),1.5 )

  ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY)

  cnt = thresh[0]
  M = cv2.moments(cnt)

  area = M['m00']

  #cx = int(M['m10']/M['m00'])
  cy = int((M['m01']+1)/(M['m00']+1))

  print(cy, M['m10'],M['m00'], M['m01'])
  if 315< cy <325:
    print(cy, 'mid')

  elif cy < 315:
    print(320-cy,'right')

  else:
    print(cy-320, 'left')

  cv2.imshow('frame', thresh)
  tEnd = time.time()
  print(tEnd - tStart)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
