import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret1, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  result = cv2.GaussianBlur(gray ,(5,5),1.5 )
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

  print(cy, cx)
  if 315< cy <325:
    print(cy, 'mid')

  elif cy < 315:
    print(320-cy,'right')

  else:
    print(cy-320, 'left')

  cv2.imshow('frame', thresh)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
