# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:48:45 2019

@author: Training23
"""

def printstar(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end='')
        print('\r')
        
def addcomplex(a,b):
    a=complex(a)
    b=complex(b)
    c=a+b
    return c
            
def fib(n):
    result=[]
    a,b=0,1
    while a < n:
        a,b=b,a+b
        result.append(a)
    return result    
        
add = lambda x ,y : x+y

def boolcheck():
    print(bool('a' in r))
    print(bool(3 in r))

    
     
l=[3,3,3,2,3,3,3,23]
c=tuple(l)

integer=34343
c=str(integer)

def prin(n):
   for i in range(n):
       if i == 3:
           continue
       print(i)
       
a=2.1234
round(a,2)
math.floor(round(a,2))

import random as r
c=r.randrange(0,100,3)
print(c)
       
    





        