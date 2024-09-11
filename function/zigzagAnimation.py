#!/usr/bin/env python
# TODO problème de gestion droite, gauche
import random, time, sys

SYMBOL = "*"
i = 0
k = 76
x = " "
timeToSleep = 0.1
directionState = True

def block():
    print(SYMBOL * 85)

try:
    block()
    while True:
        if directionState:
            print(SYMBOL, x * i, SYMBOL * 8, sep='')
            time.sleep(timeToSleep)
            i += 2
            k -= 2
            if i == 76:
                block()
                directionState = False
        elif directionState == False:
            print(x * i, SYMBOL * 8, x * k, SYMBOL, sep='')
            time.sleep(timeToSleep)
            i -= 2
            k += 2
            if i == 1:
                block()
                directionState = True
except KeyboardInterrupt:
    sys.exit()
