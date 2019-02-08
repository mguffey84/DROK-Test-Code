import RPi.GPIO as GPIO
import time

MotorPin1   = 16    # pin36
MotorPin2   = 19    # pin35
MotorEnable = 12    # pin32


GPIO.setmode(GPIO.BCM)          # Numbers GPIOs by BCM
GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
GPIO.setup(MotorPin2, GPIO.OUT)
GPIO.setup(MotorEnable, GPIO.OUT)
GPIO.output(MotorEnable, GPIO.LOW) # motor stop
pwm = GPIO.PWM(MotorEnable, 1) # configuring Enable pin (MotorEnable) for PWM)

pwm.start(50) #starting pwm with 50% duty cycle

print 'Press Ctrl+C to end the program...'
print 'Raising...'        
GPIO.output(MotorPin1, GPIO.HIGH)  # clockwise
GPIO.output(MotorPin2, GPIO.LOW)
GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
time.sleep(2.5)

GPIO.output(MotorEnable, GPIO.LOW) # motor stop
time.sleep(0.5)

print 'Dropping...'
pwm.ChangeDutyCycle(20) #decreasing dutycycle to 20
GPIO.output(MotorPin1, GPIO.LOW)   # counter-clockwise
GPIO.output(MotorPin2, GPIO.HIGH)
GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
time.sleep(1.5)

GPIO.output(MotorEnable, GPIO.LOW) # motor stop
time.sleep(0.5)

pwm.stop()
GPIO.cleanup()                     # Release resource
