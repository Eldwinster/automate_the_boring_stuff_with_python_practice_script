#!/usr/bin/env python
import random, sys, time

SENTENCES = [
    "sentence 1",
    "sentence 2",
    "sentence 3",
    "sentence 4",
    "sentence 5",
    "sentence 6",
    "sentence 7",
    "sentence 8",
]

def main():
    r = random.randint(0, len(SENTENCES) - 1)
    print(SENTENCES[r])

main()
