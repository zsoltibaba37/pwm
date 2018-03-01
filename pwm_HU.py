#!/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "0.1"

import sys
import os
import shutil
import time

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) # A BOARD mód azt jelenti, hogy a láb nevét használod. BCM módban pedíg Broadcom SOC csatorna nevét.
GPIO.setup(12, GPIO.OUT) # Ebben a példában a 12-es lábat használom.

dc = 50 # kitöltési tényező
fq = 1  # frekvencia
y = 4   # Ez csak egy szám a "ZeroDivisionError" ellenörzéséhez
z = 0

p = GPIO.PWM(12, fq)

p.start(dc) # A PWM indítása 1Hz és 50% kitöltési tényezővel

os.system('clear')

try:
    while True:
        os.system('clear')
        z = 0
        print ("-" * 80)
        print ("A 'Ctrl-c'-re megszakítja a programot és kilép.".center(80))
        print ("-" * 80)
        print (" A kitöltési tényező értéke : ", dc, "%")
        print (" A frekvencia értéke        : ", fq, "Hz")
        print ("-" * 80)
#
# kitöltési tényező
#
        while (z != 1):
            try:
                dc = int(input(' Mennyi legyen a kitöltési tényező? (1-100%): '))
                if dc in range(1,101):
                   z = 1
                   pass
                else:
                   print(" A szám az adott tartományon kívül esik!")
                   z =0
            except ValueError:
                print (" Ez nem egy szám, vagy nem egész érték van megadva!")
                z = 0
            except KeyboardInterrupt:#control-c -re kilép a programból
                p.stop()
                GPIO.cleanup()
                sys.exit(0)
#
# frekvencia
#
        while True:
            try:
                fq = int(input(' Mennyi legyen a frekvencia? (1-19200Hz)    : '))
                if fq < 0:
                   fq = 0
                else:
                    pass
                w = y/fq
                break
            except ValueError:
                print (" Ez nem egy szám, vagy nem egész érték van megadva!")
            except ZeroDivisionError:
                print (" A megadott érték nulla vagy negatív!")
            except KeyboardInterrupt:#control-c -re kilép a programból
                p.stop()
                GPIO.cleanup()
                sys.exit(0)
        p.ChangeDutyCycle(dc)
        p.ChangeFrequency(fq)
except KeyboardInterrupt:#control-c -re kilép a programból
    pass
p.stop() # Megállítja a PWM-et
GPIO.cleanup() # Visszaálítja az összes portot alapértékre
