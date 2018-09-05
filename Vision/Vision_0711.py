import cv2


cap = cv2.VideoCapture(0)

while(True):
  ret1, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  ret2, thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

  cv2.imshow('frame', thresh)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
