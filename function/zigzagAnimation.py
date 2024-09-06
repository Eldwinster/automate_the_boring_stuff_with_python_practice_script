#!/usr/bin/env python
import random, time, sys

a = "*"
i = 0
k = 76
x = " "
t = 0.1
m = True
def block():
    print(a * 85)

try:
    block()
    while True:
        if m:
            print(a, x * i, a * 8, sep='')
            time.sleep(t)
            i += 2
            k -= 2
            if i == 76:
                block()
                m = False
        else:
            print(x * i, a * 8, x * k, a, sep='')
            time.sleep(t)
            i -= 2
            k += 2
            if i == 1:
                block()
                m = True
except KeyboardInterrupt:
    sys.exit()
