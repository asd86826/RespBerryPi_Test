import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  Gaussian = cv2.GaussianBlur(gray ,(3,3) ,2 )
  lower_red = np.array([156 ,43 ,46 ])
  upper_red = np.array([180 ,255 ,255 ])
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

  if max_area > 20 :
    print("STOP")

  print(max_area , )


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
