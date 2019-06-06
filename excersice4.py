# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:26:07 2019

@author: Training23
"""

#program to calculate len 
def lenth(n):
    a=0
    for i in range(len(n)):
      a+=1
    return a  




#write program to find freq of character
    

def freqstring():
    s = str(input("enter the string"))
    result={}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i]=1
    return result   

#3

def firstlast(n):
    
    if len(n) < 2:
        return 

    return n[0:2] + n[-2:]
#swapping
    
def swap(a, b):
  newa = b[:2] + a[2:]
  newb = a[:2] + b[2:]

  return newa + ' ' + newb
#changing
def changechar(n):
    char=n[0]
    n=n.replace(char,'$')
    n=char+n[1:]
    return n
    
#conver ing to ly


def ing(n):
    if len(n) >3:
        if n[-3:] == 'ing':
            
            n += 'ly'
    else:
        n += 'ing'
    return n

 #poor not

def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1   

#largest word in stri
def longestword(wordslist):  
    word_len = []  
    for n in wordslist:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]  



def remove_char(s,n):
    firststr=s[:n]
    laststr=s[n+1:]
    return firststr + laststr


def remove_odd(s):
    result= ""
    for i in range(len(s)):
        if i % 2 == 0:
            result = result + s[i]
    return result        

def countfreq(str):
    count=dict()
    words=str.split()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    print(count)        
def changelet(n):
    
     
    return n[-1:] + n[1:-1] + n[:1]
 
    
def upperlower(n):
    print(n.upper())
    print(n.lower())
    
def commacheck():
    
    item = [ c for  c in input().split(',')]
    t=set(item.sort())
    return t
        

    
def html(tag,n):
    
     
    return "   <%s>%s<%s>"%(tag,n,tag)

def middle(str, word):
	return str[:2] + word + str[2:]

def insert2(n):
	sub = n[-2:]
	return sub * 4

def reverse(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1


def uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1


def find(n):
    return n.startswith('we') 
