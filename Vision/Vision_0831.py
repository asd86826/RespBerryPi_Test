import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

def Job_Vision ():
  while (__name__ == '__main__'):
    St = time.time()
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.GaussianBlur(gray ,(5,5),1.5 )
    ret2, thresh = cv2.threshold(result,120,255,cv2.THRESH_BINARY_INV)
    Roi1 = thresh[0:240, 0:640]
    Roi2 = thresh[241:480,0:640]
    _,contour1,hierarchy = cv2.findContours(Roi1 ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)
    _,contour2,hierarchy = cv2.findContours(Roi2 ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_NONE)
    max_area1 , max_area2 , max_cnt1 , max_cnt2= 0 , 0 , 0 , 0
#    for i in range(0,3):
#      locals()["max_area%s"%i] = 0
    for i in range(len(contour1)):
      cnt = contour1[i]
      area = cv2.contourArea(cnt)
      if (area > max_area1):
        max_area1 = area
        max_cnt1 = cnt
    for i in range(len(contour2)):
      cnt = contour2[i]
      area = cv2.contourArea(cnt)
      if (area > max_area2):
        max_area2 = area
        max_cnt2 = cnt

    M1 = cv2.moments(max_cnt1)
    M2 = cv2.moments(max_cnt2)
    cx1 = int((M1['m01']+1)/(M1['m00']+1))
    cx2 = int((M2['m01']+1)/(M2['m00']+1))

    Et = time.time()
    print('Roi1:',cx1, M1['m10'])
    print('Roi2:',cx2, M2['m10'])
    print(Et-St)

if(__name__ =='__main__'):
  try:
    Job_Vision()

  except KeyboardInterrupt:
    print('Stop')

  finally:
    cap.release()
    cv2.destroyAllWindows()
