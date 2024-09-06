#!/usr/bin/env python
import time, sys

def collatz(n):
    if n % 2 == 0:
        return n //  2
    else:
        return 3 * n + 1

def main():
    n = input("Enter a interger: ")
    if n.isdigit():
        n = int(n)
        while n != 1:
            n = collatz(n)
            if n % 2 == 0:
                print(f"{n} // 2", "=", n, sep='\t')
                time.sleep(0.1)
            else:
                print(f"3 * {n} + 1", "=", n, sep='\t')
                time.sleep(0.1)
    else:
        print("Please enter an interger. (i.e. 1, 2, ..., n)")
try:
    main()
except KeyboardInterrupt:
    sys.exit
