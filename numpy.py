# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:58:00 2019

@author: Training23
"""

def importnumpy():
    import numpy as np
    
    
def mat3x3():
    import numpy as np
    c=np.random.randint(5,13,(3,3))
    return c
    

c=np.zeros(10)
c[5]=11


c=np.arange(12,38)


c=np.arange(12,38)
c[::-1]   


c=np.arange(12,38)
c=np.asfarray(c)


c=np.ones((5,5))


x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


def convert(n):
    c=np.asarray(n)
    return c

def apppen(n):
    r=np.append(r,n)
    return r


fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)


print(5*F/9 - 5*32/9)


#14

def findreal(n):
    x=np.sqrt(n)
    print(x.real)
    print(x.imag)
    
    
#15
def compare(n,m):
    print(np.in1d(n,m))
     
#16
def findcm(n,m):
    print(np.intersect1d(n,m))    


#17
    
def unique(n):
    print(np.unique(n))


#18
def checkall(m:list):
    c=np.all(m)
    return c
    
    

#19
    
def checkone(m:list):
    c=np.any(m)
    return c

#20
    
def repeat(m:list,n : int ) ->list:
    c=np.repeat(m,n)
    return c
    
    
#21
def find1andn(n:list):
    c=np.argmax(n)
    d=np.argmin(n)
    print('max',c)
    print('min',d)

#22
def compare(a:list,b:list):
    print(np.greater(a, b))
    print("a >= b")
    print(np.greater_equal(a, b))
    print(("a < b"))
    
    print(np.less(a, b))
    print("a <= b")
    print(np.less_equal(a, b))
 

#23
    
def filesave():
    a=np.arange(1,32,32)
    np.savetxt('fileout',a,delimiter=',')
    
    
    
def flat():
    n=[(i) for i in input("enter value")]
    
    print(n)
    c=np.ravel(n) 
    return c

    


c=[[[33,3,3,],[3,3,2]][[3,34,32],[3,3,3,3]]]
t=np.sum(c)
s=np.max(c)
r=np.min(c)
    
    




    