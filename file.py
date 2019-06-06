import csv


with open(r'D:\tablueau\circuits.csv') as csvfile:
    dialect = 'excel'
    reader = csv.reader(csvfile,dialect)
    for row in reader:
        print(row)
    


#write to csv file
with open(r'D:\tablueau\circuits.csv',mode='w') as file:
    writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for i in range(0,10):
        writer.writerow(['karthick','nagaraj','g','k'])
        


        
#program for registered diaelet
import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open(r'D:\tablueau\circuits.csv', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
    for i in reader:
        print(i)
        


#program for unregister dialect

csv.list_dialects()
csv.unregister_dialect("excel-tab")
print csv.list_dialects()



#Write a python program using csv.get_dialect

get_dialect(...)
    Return the dialect instance associated with name.
    dialect = csv.get_dialect(name)


c=csv.get_dialect(name)


#Write a python program using csv.list_dialects()


c=csv.list_dialects()


#Write a python program using import sys
import csv

csv.field_size_limit(sys.maxsize)

#Write a python program using csv.QUOTE_ALL

with open(r'C:\Users\USEERZ\Documents\name.csv.xlsx') as f:
	


	writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
	for i in range(1,10):
		writer.write(["karthick","nagaraj"])
		

#Write a python program using csv.QUOTE_MINIMAL
with open(r'D:\tablueau\circuits.csv',mode='w') as file:
    writer=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for i in range(0,10):
        writer.writerow(['karthick','nagaraj','g','k'])
#Write a Python program to read an entire text file
with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx','r') as f:
  c=f.read()
  for i in c:
    print(c)
	
#Write a Python program to read first n lines of a file	
with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx','r') as f:
  c=f.readline()
  for i in c:
    print(c)


with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx' , "a") as myfile:
    
	myfile.write("appended text")
	output=open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx'')
	print(output.read())
	
	
#Write a Python program to read last n lines of a file.


import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break
	

#Write a Python program to read a file line by line and store it into a list.

def file_read(fname):
        with open(fname) as f:
                list=list()   
                list = f.readlines()
                print(list)
				

#Write a Python program to read a file line by line store it into a variable.
	

def file_read(fname):
        with open(fname) as f:
                  
                var = f.readlines()
                print(var)				
				



#Write a Python program to read a file line by line store it into an array

def file_read(fname):
        array = []
        with open(fname) as f:
                    
                for line in f:
                        array.append(line)
                print(array)


#Write a python program to find the longest words


def longestword(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

#Write a Python program to count the number of lines in a text file

fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)

#Write a Python program to count the frequency of words in a file
from collections import Counter
def wordcount(fname):
        with open(fname) as f:
                return Counter(f.read().split())



#Write a Python program to get the file size of a plain file

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

#Write a Python program to write a list to a file.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)


#Write a Python program to copy the contents of a file to another file

with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx') as f:
    with open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx', "w") as f1:
        for line in f:
            f1.write(line)

#Write a Python program to combine each line from first file with the corresponding line in second file.

with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        
        print(line1+line2)
		

#Write a Python program to read a random line from a file

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))


f=open(r'C:\Users\USEERZ\Documents\DESCRIPTION.xlsx')

print(f.closed)
f.close()
print(f.closed)

#Write a Python program to remove newline characters from a file


def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]