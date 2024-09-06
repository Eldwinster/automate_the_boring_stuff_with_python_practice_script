#!/usr/bin/env python
# https://realpython.com/python-while-loop/#the-python-break-and-continue-statements
# I tried to reproduce the diagram page 64 on emacs and 22 on the book.
print("Hi there, I'm here to help you decide what's best for you!")
weather = input("How's today weather? Sunny or rainy ")
while True:
    weather = input("How's the weather now? Sunny or rainy ")
    if weather.strip().isdigit():
        print("Come on, don't be like that, just tell me")
        continue
    else:
        if weather.lower() == "rainy":
            itemRain = input("Hopefully, you have an umbrella around, somewhere, right? [y/n]")
            if itemRain.lower() == "y":
                break
            elif itemRain.lower() == "n":
                print("There is no other way than to wait then..")
                continue
        elif weather.lower() == "sunny":
            break
        else:
            print("Sorry, I'm not competent yet")
    continue
print("Just go outside then, what are you waiting for?")
