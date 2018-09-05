import cv2


cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  Roi1 = frame[0:240, 0:640]
  Roi2 = frame[241:480,0:640]

  cv2.imshow("Roi", Roi1)
  cv2.imshow("Roi2", Roi2)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
