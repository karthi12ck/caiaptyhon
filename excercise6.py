# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:07:09 2019

@author: Training23
"""

def tuplecreate(n):
    n=tuple(n)
    return n


def tuplediff(n):
    n=tuple(n)
    return n
    

def tupleadd(n,m):
    c=tuple(n)+tuple(m)
   
    return c
    

def tupeltolist(n):
    c=str()
    c=''.join(n)
    return c



def tocheck():
    c=list(input("enter  tuple"))
    c=tuple(c)
    print(c)
    t=input("enter character")
    
    print(c)
    print('3' in c)
 

def convertlist(n):
    c=tuple(n)
    c=list(c)
    return c


def toremove():
    n=input("enter tuple")
    m=input("enter item to remove")
    n=tuple(n)
    
    c=list(n)
    c.remove(m)
    return c
    
def length(n):
    n=tuple(n)
    return len(n)

def tupletodect(n):
    return (dict(x,y) for x,y in n)

x = ("karthick")

y = reversed(x)
print(tuple(y))


