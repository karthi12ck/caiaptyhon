# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:07:52 2019

@author: Training23
"""

#arithmetic function

class Arithmetic():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
  
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod(self):
        return self.a % self.b
    def exp(self):
        return self.a ** self.b
    def floor(self):
        return self.a // self.b
    
    
        
          
#assignment operator
        
class assignment():
    def __init__(self,a):
        self.a=a
        
        
    def eql(self):
        self.a=5
        return self.a
    def ast2(self):
        self.a+=3
        return self.a
    def ast3(self):
        self.a-=3
        return self.a
    def ast4(self):
        self.a*=3
        return self.a
    def ast5(self):
        self.a/=3
        return self.a
    def ast6(self):
        self.a%=3
        return self.a
    
class compare():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def eql(self):
      return (self.x == self.y )
    
    def noteql(self):
        return (self.x != self.y)
    def grt(self):
        return (self.x > self.y)
    def les(self):
        return (self.x < self.y)
    def grte(self):
        return (self.x >= self.y)
    def lese(self):
        return (self.x <= self.y)


class logical():
    def __init__(self,x):
        self.x=x
    def and1(self):
        return self.x < 5 and self.x < 10
    def or1(self):
        return self.x < 5 or self.x < 33
    def note(self):
        return not(self.x <5 and self.x >10)
    
class identity():
    def __init__(self,a,b):
        self.b=b
        self.a=a
    def iss(self):
        return self.a is self.b
    def isnot(self):
        return self.a is not self.b
    
    
class membership():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ins(self):
        
    
        self.a = [x*2 for x in range(self.a)]
        self.b = [x*3 for x in range(self.b)]
        print(2 in self.a)
        print(3 not in self.a)
        
class bitwise():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def and1(self):
        return self.a & self.b
    def or1(self):
        return self.a | self.b
    def xor(self):
        return self.a ^ self.b
    def note(self):
        return  ~ self.a 
    
           
  #string literals
print(s)
print(r)



s="kar" "thick" 
print(s)


#numeric literals

n1=3243
n2=32.34
n3=(343+3j)
print(n1,n2,n3)


#boolean literals
flag=True
flag1=False
print(flag1)
print(flag)

#special literals

val1=0
val1=None
print(val1)         
        


#literal collections

lists =[343,343,34,'karthick']
     
lists1=['343',343,'ere',3]
print(lists1+lists)
print(lists1*3)   
       
    
    
        
       
from time import sleep  
def gener(n):
   
    for i in range(n):
        yield i
        def rang():
            nonlocal n
            for item in gener():
                print(item)
    return rang()            
   
        
    
        
        
        
for item in gener():
    sleep(3)
    print(item)
    
    