import cv2


cap = cv2.VideoCapture(0)

thresh1 = [0,0,0]

while(True):
  ret, frame = cap.read()
  gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ret2, thresh = cv2.threshold(gary,100,255,cv2.THRESH_BINARY)
  cv2.imshow("frame", frame)
  print(thresh[0])
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()

cv2.destroyAllWindows()
