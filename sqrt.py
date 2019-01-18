# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:12:32 2019

@author: MrZik
"""

def sqrt(x):
    return (round(x**0.5,3))

def Heron(value):
    if value < 0:
        value = abs(value) #Value must stay positive
    closeness = 0.01 #sharpness
    guess = value / 3.0  #initial value of the suite
    while(True):
        to_find = (guess * guess) - value 
        absTo_find = abs(to_find) #to_find must stay positive
        if absTo_find <= closeness: 
            return round(guess,3)
        guess = (guess + (value/guess))/2.0  #main formula
        
print(Heron(15))
        