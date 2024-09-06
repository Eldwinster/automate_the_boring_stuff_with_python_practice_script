#!/usr/bin/env python

l= ['apples', 'bananas', 'tofu', 'cats']

def func(a):
    for index, item in enumerate(a):
        if index == len(a) - 1:
            print("and", item)
        else:
            print(item, end=', ')
func(l)
