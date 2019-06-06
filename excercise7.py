# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:15:43 2019

@author: Training23
"""

def createdic(n):
    n=dict(n)
    return n 
    
    
def acessdic(n):
    c={2:2,3:2,1:2}
    return c[n]
        

def update(n,m):
    c={2:2,3:2,1:2}
    c[n]=m
    return c

    

def delete():
    c={2:2,3:2,1:2}
    print(c)
    del c
   
    print("deleted")
    
    
def copy(n):
    c=dict(n)
    return c
    


def deletekey(n):
    c={2:2,3:2,1:2}
    if n in c:
        del c[n]
    return c    
    


def sorting():
    c={2:2,3:2,1:2}
    print(c)
    c=dict(sorted(c.items()))
    print(c)
    