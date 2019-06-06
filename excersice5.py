# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:16:03 2019

@author: Training23
"""

def sumof(n):
  
    s=0
    for i in n:
        s += i
    return s   

def mutl(n):
    s=1
    for i in n:
        s *=i
    return s    

def largest(n):
    n.sort()
    return n[-1]
    


def smal(n):
    n.sort()
    return n[0]



def removedup(n):
    duple = set()
    unique = []
    for x in n:
        if x not in duple:
            unique.append(x)
            duple.add(x)
    return unique


def checkemp(l):
   
    if not l:
        print("List is empty")
     

def clone(n):
    c=list(n)
    return c



def specificlist(n):
    n = [x for(i,x) in enumerate(n) if i not in (0,4,5)]
    return n    
        

def differ(n,c):
    return (list(set(n) - set(c)))
    


def specific(n):
    n=list()
    print (all(x>400 for x in n))
        
def mintuple(n):
    print(min(n, key=lambda x: (x[1], -x[0])))
    
    
def findnth(n):
    
    xlen = len(n)-1
    print(n[xlen])


def lasttolist(n,m):
    n=list(n)
    m=list(m)

    
    n[-1]=m
    return n  

def stringt(n):
    print(all(c == 'army' for c in n))
    
def stringtolist(n):
    return list(n)


def concat(n):
    return (''.join(n))


def multilist():
    obj = {}
    for i in range(1, 21):
        obj[str(i)] = []
    print(obj)
    
    
def common(n,m):
    n=list(n)
    m=list(m)
    return(set(m) & set(n))
 
    
from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs    


def uniquelist(n):
    n=set(n)
    r=list(n)
    return r