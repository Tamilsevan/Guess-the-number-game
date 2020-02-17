# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:02:03 2020

@author: Tamil"""
import random
print("Welcome to game")
n=1
yes=['YES','yes','Yes','Y','y']
no=['NO','No','no','N','n']
while(n==1):
    response=input('Would you like to play the guessing game?')
    if response in yes:
        n=1
    elif response in no:
        n=0
        print('Thank you for playing')
        break
    else:
        print("wrong choice please choose y/n")
        continue
    cmp=random.randint(1,10)
    for i in range(4,-1,-1):
        choice=input("Enter your guess:")
        if cmp==choice:
            print("you won")
            break
        else:
            print("you lost try again")
            print("remaining chances:",i)

    