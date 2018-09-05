import time
import Adafruit_PCA9685
import cv2
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

pwm = Adafruit_PCA9685.PCA9685()
power = 300
def severo_set() :
  pwm.set_pwm(15, 0 ,power)
  print ('ON')
  time.sleep(0.1)

pwm.set_pwm_freq(67)

def get_distance():
  GPIO.output(TRIG,False)
  time.sleep(0.01)
  GPIO.output(TRIG,True)
  time.sleep(0.01)
  GPIO.output(TRIG,False)
  while GPIO.input(ECHO)==0:
    start = time.time()
  while GPIO.input(ECHO)==1:
    end = time.time()
  return (end - start) * 17150

while(__name__ == '__main__'):
  severo_set()
  print get_distance(),"cm"
  iwhile(__name__ == '__main__'):
  severo_set()
  print get_distance(),"cm"
  if get_distance() < 30:
      if power < 430:
        power = power+10
      else :
        power = power+1
  elif 150 > get_distance() > 30:
    power=453
    pwm.set_pwm(15, 0 ,power)
    print('Stop',get_distance())
    time.sleep(10)
    for i in range(0,50,10):
      power = 420 - i
      pwm.set_pwm(15, 0 ,power)
      print(power, get_distance())
      time.sleep(3)
    pwm.set_pwm(15, 0 ,300)
    break
  print power
GPIO.cleanup()f get_distance() < 30:
      if power < 430:
        power = power+10
      else :
        power = power+1
  elif 60 > get_distance() > 30:
    power=453
      if get_distance > 60:
        power = 420
        pwm.set_pwm(15, 0 ,power)
    print('Stop',get_distance())
    time.sleep(10)
    for i in range(0,50,10):
      power = 420 - i
      pwm.set_pwm(15, 0 ,power)
      print(power, get_distance())
      time.sleep(3)
    pwm.set_pwm(15, 0 ,300)
    break
  print power
GPIO.cleanup()
