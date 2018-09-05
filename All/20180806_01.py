import threading
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
my_pwm11=GPIO.PWM(11,72)
my_pwm13=GPIO.PWM(13,72)
my_pwm15=GPIO.PWM(15,72)
my_pwm16=GPIO.PWM(16,72)
my_pwm18=GPIO.PWM(18,72)
my_pwm11.start(10.8)
my_pwm13.start(10.8)
my_pwm15.start(6.8)
my_pwm16.start(10.8)
my_pwm18.start(6.5)

cap = cv2.VideoCapture(0)


def job():

 a=7
 for k in range(100):
  if a>=7 and a<=10:
   a=a+0.5
  elif a>10:
   a=a-0.5
  print("Go",a)
  my_pwm15.ChangeDutyCycle(a)
  time.sleep(0.2)



t = threading.Thread(target = job)

t.start()

while(True) :
  Ts = time.time()
  ret1, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  result = cv2.GaussianBlur(gray ,(5,5),1.5 )
  ret2, thresh = cv2.threshold(result,100,255,cv2.THRESH_BINARY)
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

  cx = int(M['m10']+1/M['m00']+1)
  cy = int((M['m01']+1)/(M['m00']+1))

  print(cy, cx)
  if 315< cy <325:
    print(cy, 'mid')

  elif cy < 315:
    print(320-cy,'right')

  else:
    print(cy-320, 'left')

  cv2.imshow('frame', thresh)
  Te = time.time()
  print( Te-Ts )

  if cv2.waitKey(1) & 0xFF ==ord('q'):
    break

cap.release()

cv2.destroyAllWindows()

print("Done.")
