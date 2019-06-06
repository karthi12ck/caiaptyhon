#scope of variable

def my_second_func():
	a = 10
    print('I see "a" = ', a, 'from "my_second_func"')
	
	
print(a)
NameError                                 Traceback (most recent call last)
<ipython-input-10-3f786850e387> in <module>()
----> 1 a

NameError: name 'a' is not defined	

Scope	        It is declared inside a function.	It is declared outside the function.
Value	        If it is not initialized            If it is not initialized zero is stored as default.
                 a garbage value is stored	


#3
def f():
    print s
 s = "I love Geeksforgeeks"
f()

s is the global variable it is not used inside the function


#Write a program using Lambda in python.
x = lambda a, b : a * b
print(x(5, 6))

#Write python program using Positional parameters or required parameters
def postion(a,b):
	c=a/b
	print(c)
	

#Write python program using positional only
def postion(x,y,z):
	c=x*y/z
	print(c)
	
#Write python program using Keyword Parameters or default parameters

def defaults(a=2,b):
	c=a+b
	print(c)
	
#Write python program using variable length positional parameter	
def variable(*args,**kwargz):
   retrun 
 #9.Write python program using Variable length keyword parameter  
 
def sum(*args):
    print(type(args))
    print(args)
 
 #Write python program using keyword parameter

 
  format_attributes(name="Trey", website="http://treyhunner.com", color="purple") 
  format_attributes(name="Trey", website="http://treyhunner.com", color="purple")
#Write a program for command line arguments in python

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)



	

	



