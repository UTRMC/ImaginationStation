# This code is to be used for the imagination station
# This program will ask for a set of instructions to run with the options "Forward, Backward, Turn Left, Turn Right
import os
import sys

import RPi.GPIO as GPIO  # Pin setup for Entire Pi
import time

# Disable Warnings
GPIO.setwarnings(False)

# pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# motor variables
FR = GPIO.PWM(13, 50)  # Front Right Motor #The value 50 is the Frequency
FL = GPIO.PWM(22, 50)  # Front Left Motor #The value 12 is the GPIO pin
RR = GPIO.PWM(15, 50)  # Rear Right Motor
RL = GPIO.PWM(18, 50)  # Rear Left Motor
FR.start(100)
FL.start(100)
RR.start(100)
RL.start(100)

x = True


# Define functions for kids to use

def forward(self):
    if x == True:
        return
    else:
        FR.ChangeDutyCycle(6.5)
        FL.ChangeDutyCycle(8)
        RR.ChangeDutyCycle(6.5)
        RL.ChangeDutyCycle(8)
        time.sleep(self)
        FR.ChangeDutyCycle(100)
        FL.ChangeDutyCycle(100)
        RR.ChangeDutyCycle(100)
        RL.ChangeDutyCycle(100)


def reverse(self):
    if x == True:
        return
    else:
        FR.ChangeDutyCycle(8)
        FL.ChangeDutyCycle(6.5)
        RR.ChangeDutyCycle(8)
        RL.ChangeDutyCycle(6.5)
        time.sleep(self)
        FR.ChangeDutyCycle(100)
        FL.ChangeDutyCycle(100)
        RR.ChangeDutyCycle(100)
        RL.ChangeDutyCycle(100)


def turn_right():
    if x == True:
        return
    else:
        FR.ChangeDutyCycle(10)
        FL.ChangeDutyCycle(10)
        RR.ChangeDutyCycle(10)
        RL.ChangeDutyCycle(10)
        time.sleep(.51)
        FR.ChangeDutyCycle(100)
        FL.ChangeDutyCycle(100)
        RR.ChangeDutyCycle(100)
        RL.ChangeDutyCycle(100)


def turn_left():
    if x == True:
        return
    else:
        FR.ChangeDutyCycle(5)
        FL.ChangeDutyCycle(5)
        RR.ChangeDutyCycle(5)
        RL.ChangeDutyCycle(5)
        time.sleep(.51)
        FR.ChangeDutyCycle(100)
        FL.ChangeDutyCycle(100)
        RR.ChangeDutyCycle(100)
        RL.ChangeDutyCycle(100)


def stop():
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)


def can_compile(self):
    try:
        eval(self)
    except:
        print("System Crash! Restarting...")
        time.sleep(5)
        os.execl(sys.executable, sys.executable, *sys.argv)


# Print instructions
print("To go forward type forward(Time) and press enter. Where time is how long the robot runs")
print("To go backwards type reverse(Time) and press enter. Where time is how long the robot runs")
print("To turn right 90 degrees type turn_right() and press enter")
print("To turn left 90 degrees type turn_left() and press enter")
print("Using these functions program the robot through the obstacle course!")
print("Type all your instructions in at once. When you enter Start, your program will run. Good Luck!")

# Obtain inputs and push them to an array
command = 0
instructions = []  # Array that stores the kids code
while command != "Start":  # While the command is not Start continue taking commands and save them to the array
    command = input()
    instructions.append(command)

# Remove Start
instructions.pop()

# Check to see if the code compiles
for x in instructions:
    can_compile(x)

x = False

# Read the instructions given and run the functions
print("Your output is:")
for x in instructions:
    print(x)
    eval(x)

# Restart program
os.execl(sys.executable, sys.executable, *sys.argv)
