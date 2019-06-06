# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:08:41 2019

@author: Training23
"""

#syntax


try:
    print("")
    
except Exception as err:
    print(err)
finally:
    print("final")
          
    
    
    
#2

def exception(n,m):
    try:
        c=n/m
        print(c)
    except Exception as err:
        print(err)
        print("enter n>0")
    finally:
        print("finished")
    
    
def findexception(n,m):
    try:
        c=n/m
        print(c)
        if c == 10:
            raise Exception("10 is not used")
    except ZeroDivisionError:
        print("zero error")       
    except SyntaxError:
        print("try valid syntax")
    finally:
        print("finished")




def rasingexception(n,m):
    try:
        import numpy as np
        c=np.random.randint(10)
        t=n/10
        print(c)
        if t != c:
            raise Exception("try again")
    except ZeroDivisionError:
        print("error happened")
        
        
def game(n,m):
    import numpy as np
    c=n/m
    t=np.random.randint(1,10)
    if c != t:
        print("try again")
        print("value got",c)
        print("value excepted",t)
    else:
        print("super")
        
        
class usererror(Exception):
    print("user defined error happend")

class zeroerror(usererror):
    print("divisible by zero error happen")
class typeerror(usererror):
    print("data type error happen")    

def inputs(n,m):
    try:
        if m == 0:
            raise zeroerror
        else:
            c=n/m
            print(c)
    except zeroerror:
        print("happened")
    
    
def inputage(age):
   try:
       assert int(age) > 18
   except ValueError:
       return 'ValueError: Cannot convert into int'
   else:
       return 'Age is saved successfull'