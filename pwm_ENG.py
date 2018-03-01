#!/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "0.1"

import sys
import os
import shutil

import RPi.GPIO as GPIO 
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) # BCM mean use Broadcom SOC channel (GPIO18), not the pin number. If use GPIO.BOARD then use the pin numer.
GPIO.setup(12, GPIO.OUT) # In this example I use the PIN 12

dc = 50 # duty cycle
fq = 1  # frequency 
y = 4   # Its just a number for the "ZeroDivisionError" error 
z = 0

p = GPIO.PWM(12, fq) 

p.start(dc) # Start PWM with 1Hz and 50% duty cycle

os.system('clear')

try:
    while True:
        os.system('clear')
        z = 0
        print ("-" * 80)
        print ("Ctrl-c will interrupt the program and exit.".center(80))
        print ("-" * 80)
        print (" The value of the duty cycle : ", dc, "%")
        print (" The value of the frequency  : ", fq, "Hz")
        print ("-" * 80)
#
# duty cycle
#
        while (z != 1):
            try:
                dc = int(input(' How many percentage should be the duty cycle (1-100%): '))
                if dc in range(1,101):
                   z = 1
                   pass
                else:
                   print(" The number is in out of range!")
                   z =0
            except ValueError:
                print (" This is not a number or not an integer value!")
                z = 0
            except KeyboardInterrupt:#control-c will interrupt the program
                p.stop()
                GPIO.cleanup()
                sys.exit(0)
#
# frequency
#
        while True:
            try:
                fq = int(input(' How many should be the frequency? (1-19200Hz)        : '))
                if fq < 0:
                   fq = 0
                else:
                    pass
                w = y/fq
                break
            except ValueError:
                print (" This is not a number or not an integer value!")
            except ZeroDivisionError:
                print (" The specified value is zero or negative!")
            except KeyboardInterrupt:#control-c will interrupt the program
                p.stop()
                GPIO.cleanup()
                sys.exit(0)
        p.ChangeDutyCycle(dc)
        p.ChangeFrequency(fq)
except KeyboardInterrupt:#control-c will interrupt the program
    pass
p.stop() # Stop PWM
GPIO.cleanup() # Clean up all the ports you’ve used
