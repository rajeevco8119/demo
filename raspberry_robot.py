import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # To use GPIO number convention/ Other is BOARD convention

TRIG = 17
ECHO = 27

led = 26

m1a = 23
m1b = 24
m2a = 25
m2b = 8

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO(m1a, GPIO.OUT)
GPIO(m1b, GPIO.OUT)
GPIO(m2a, GPIO.OUT)
GPIO(m2b, GPIO.OUT)

time.sleep(5)

def stop():
    GPIO.output(m1a,0)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 0)

def forward():
    GPIO.output(m1a, 1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 1)
    GPIO.output(m2b, 0)

def left():
    GPIO.output(m1a,1)
    GPIO.output(m1b, 0)
    GPIO.output(m2a, 0)
    GPIO.output(m2b, 0)

stop()

while True:
    GPIO.output(TRIG, 0)
    time.sleep(0.1)
    GPIO.output(TRIG, 1)
    time.sleep(0.0001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        GPIO.output(led,False)

    pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        GPIO.output(led,True)

    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance,2)
    print(distance)

    if distance < 15:
        left()
        time.sleep(1)
    else:
        forward()
