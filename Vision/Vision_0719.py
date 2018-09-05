import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  result = cv2.GaussianBlur(gray ,(5,5),1.5 )
  ret2, thresh = cv2.threshold(result,120,255,cv2.THRESH_BINARY_INV)

  Roi1 = frame[0:240, 0:640]
  Roi2 = frame[241:480,0:640]

  cnt1 = Roi1[0]
  cnt2 = Roi2[0]

  M1 = cv2.moments(cnt1)
  M2 = cv2.moments(cnt2)
  cy1 = int((M1['m01']+1)/(M1['m00']+1))
  cy2 = int((M2['m01']+1)/(M2['m00']+1))

  cv2.imshow("Roi", Roi1)
  cv2.imshow("Roi2", Roi2)

  print(cy1, M1['m10'])
  print(cy2, M2['m10'])

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
