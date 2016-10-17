# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:37:12 2016

@author: njuzc
"""

#! /usr/bin/python
# 014.py
import math
#number = int(raw_input("Enter a number: "))

#while number != 1:
#
#    for i in range(1, number + 1):
#        if (number % i) == 0 and i != 1:
#            number = number / i
#            if number == 1:
#                print " %d" %i
#            else:
#                print " %d*" %i,
#            break
        
        
import sys
n = int(sys.stdin.readline().strip())

s = []
for i in range(n):
	s.append(int(sys.stdin.readline().strip()))

s = [17,36]

def prime(number):
    output = ""
    if number!=1:
        square = int(number/2) + 1
        for i in range(2,square+1):
            k = 0
            while (number % i) == 0:
                k = k+1
                number = number/i
            if k!=0: output = output+str(i)+" "+str(k)+" "
    return output if output!="" else str(number)+" "

for j in range(len(s)):
#    result = "Case"
	print "Case "+str(j)+": "+prime(s[j])[:-1]




        
        
# 智静的程序        
#import math    
#
#def getFactor(num):
#    res = {} 
#    i = 2  
#    square = int(math.sqrt(num)) + 1  
#    while i <= square:
#        while num % i == 0:
#            res[i] = res.get(i, 0)+1  
#            num = num/i 
#        i += 1   
#    return res
#
#number = int(raw_input("Enter a number: "))
#
#res = getFactor(number)        
        
        
        