import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while(True):
  tS = time.time()
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lower_red = np.array([-10 ,100 ,100 ])
  upper_red = np.array([10 ,255 ,255 ])
  mask_red = cv2.inRange(gray ,lower_red ,upper_red )

  img ,contours,hierarchy = cv2.findContours(mask_red ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)

  c_max = []
  max_area = 0
  max_cnt = 0

  for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)

    if(area>max_area):
      max_area = area
      max_cnt = cnt


  cv2.imshow("Roi", img)
  tE = time.time()
  if max_area > 150 :
    print("STOP")

  print(max_area , i, tE - tS)


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
