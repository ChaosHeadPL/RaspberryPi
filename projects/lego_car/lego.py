#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

IN1 = 11  # pin11
IN2 = 12
IN3 = 13
IN4 = 15

degre = {"360": 512, "180": 256, "90": 128, "45": 64, "22": 32, "11": 16}


def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)


def stop():
    setStep(0, 0, 0, 0)


def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)


def backward(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)  # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def turn_right(move):
    print("Turning RIGHT")
    print("backward...")
    backward(0.003, move)  # 512 steps --- 360 angle

    print("stop...")
    stop()  # stop
    time.sleep(3)  # sleep 3s

    print("forward...")
    forward(0.005, move)

    print("stop...")
    stop()
    time.sleep(3)


def turn_left(move):
    print("Turning LEFT")
    print("forward...")
    forward(0.005, move)

    print("stop...")
    stop()
    time.sleep(3)

    print("backward...")
    backward(0.003, move)  # 512 steps --- 360 angle

    print("stop...")
    stop()  # stop
    time.sleep(3)  # sleep 3s


def loop():
    move = degre["180"]
    while True:
        turn_left(move)
        turn_right(move)


def destroy():
    GPIO.cleanup()  # Release resource


if __name__ == "__main__":  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        destroy()

