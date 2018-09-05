import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

pwm1 = GPIO.PWM(32,72)
pwm2 = GPIO.PWM(33,72)
pwm3 = GPIO.PWM(12,72)
pwm4 = GPIO.PWM(35,72)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

while True:
 pwm1.ChangeDutyCycle(10.2)
 pwm2.ChangeDutyCycle(10.2)
 pwm3.ChangeDutyCycle(10.2)
 pwm4.ChangeDutyCycle(10.2)
