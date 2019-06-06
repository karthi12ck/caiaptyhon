# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:32:29 2019

@author: Training23
"""

#class

class name():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print("welcome {} and your age is {} ".format(self.name,self.age))
        
#return

class sqt():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        c=self.radius*self.radius
        return c    

#try catch finally return as

class sqt1():
     def __init__(self,radius):
         self.radius=radius
     def are(self):
         try:
             c=self.radius*self.radius
             r=(self.radius/0)
             
         except Exception as err:
             print(err)
         finally:
             print("executed")
         return c    
             
#continue break if elif else            
def oddnum(n):
    for i in range(n):
        
        if i == 5:
            continue
        elif i == 33:
            break
        else:
            print(i)
         
#true false in not 
def boolean(n):
    l=[]
    for i in range(n):
        l.append(i)
    print(bool(200 not in l))
    print(bool(4 not in l))
        
                
# del or  
def delete(n):
    l=[]
    for i in range(n):
        l.append(i)
    if l[0] == 0 or l[10] ==9:
        del l[0]
        del l[4]
    return l  


#import from raise 
def maths(n):
    import math
    from random import randrange
    math.floor(n)
    print(n)
    c=randrange(0,100,2)
    print(c)
    try:
        r=n/0
        raise Exception('This is the exception you expect to handle')
    except ZeroDivisionError:
        print("divisible by zero")
    try:
        raise ValueError
    except ValueError:
        print("there is a exception")
      
        
#pass while
def passwhile(n):
    a=10
    while a < n:
        n-=n
        if a == 3:
            pass
        else:
            pass
    print(a)    
         
#none            
def nonevalue():
    c=None
    print(c)        
#yeild

    
def countdown(num):
    
    print('starting')
    while num > 0:
        
        yield num
        
        num -=1`
    
 #lambda

c = lambda x,y: x*y
   
 s="karthick"      
def glot():
    global s
    print(s)
    s='nagaraj'
    print(s)

  
        
#is
def agecheck(age):
    try:
        assert age !=0
    except AssertionError:
        print("assert error")
    return age 

def outer(x):
    x='local'
    def inner():
        nonlocal x
        x="non local"
        print('inner',x)
    inner()
    print('outer',x)    
  #non local value will ater the local variable value in outerfunction
 
        
#2
'''identifiers
 1.create identifier using only albabets ,numeric and underscore 
 2.special characters are not allowed
 3.numeric value should not at the begin 
 4.case sensitive
   
        
          