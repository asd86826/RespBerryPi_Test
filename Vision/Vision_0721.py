import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  lower_red = np.array([-10 ,100 ,100 ])
  upper_red = np.array([10 ,255 ,255 ])
  mask_red = cv2.inRange(gray ,lower_red ,upper_red )

  img ,contours,hierarchy = cv2.findContours(mask_red ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)

  cnt1 = contours[1]

  M1 = cv2.moments(cnt1)
  area = M1['m00']
  cv2.imshow("Roi", img)

  if area > 50 :
    print("STOP")

  print(contours)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
