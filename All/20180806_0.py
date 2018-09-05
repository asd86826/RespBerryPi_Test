import threading
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
my_pwm11=GPIO.PWM(11,72)
my_pwm12=GPIO.PWM(12,72)
my_pwm15=GPIO.PWM(15,72)
my_pwm16=GPIO.PWM(16,72)
my_pwm18=GPIO.PWM(18,72)
my_pwm11.start(10.8)
my_pwm12.start(10.8)
my_pwm15.start(6.8)
my_pwm16.start(10.8)
my_pwm18.start(6.5)

global cx

def Job_pwm ():
  global cx
  if 240< cx <400:
    print(cx, 'mid')
  elif cx > 400:
    print(320-cx,'right')
  else:
    print(cx-320, 'left')



def Vision_():
 red = (0, 0, 255)
 cap = cv2.VideoCapture(0)
 while(__name__ == '__main__'):

  Ts = time.time()
  ret1, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  result = cv2.GaussianBlur(gray ,(5,5),1.5 )
  cv2.line(result, (240, 0), (240, 480) , red ,2)
  cv2.line(result, (400, 0), (400, 480) , red ,2)
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

  cv2.circle(thresh, (cx,cy), 2, red, 2)
  print(cx, cy)
  if 240< cx <400:
    print(cx, 'mid')
    my_pwm12.ChangeDutyCycle(10.2)
  elif cx > 400:
    print(320-cx,'right')
    my_pwm12.ChangeDutyCycle(10.4)
  else:
    print(cx-320, 'left')
    my_pwm12.ChangeDutyCycle(9.7)
  cv2.imshow('frame', thresh)
  Te = time.time()
  print( Te-Ts )

  if cv2.waitKey(1) & 0xFF ==ord('q'):
    cap.release()
    cv2.destroyAllWindows()
    break

V = threading.Thread(target = Vision_)

V.start()


print("Done.")
