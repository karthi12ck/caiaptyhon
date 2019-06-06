import operator
a=3
b=4
c=operator.lt(a,b)
print(c)
c=operator.le(a,b)
print(c)
c=operator.eq(a,b)
print(c)
c=operator.ne(a,b)
print(c)
c=operator.ge(a,b)
print(c)
c=operator.gt(a,b)
print(c)
c=operator.__lt__(a,b)
print(c)
c=operator.__le__(a,b)
print(c)
c=operator.__eq__(a,b)
print(c)
c=operator.__ne__(a,b)
print(c)
c=operator.__ge__(a,b)
print(c)
c=operator.__gt__(a,b)
print(c)




from itertools import *


for i in chain([x*2 for x in range(0,10)],['a','b','c','d']):
    print(i)
    
    

#itertools combination
for i in combinations([x for x in range(0,10)],3):
    print(i)
    
#compress

for i in compress('karthick',[1,0,1,0,1,0,0,1]):
    print(i)


    


#count

for i in count(30):
    print(i)

#cylce

for i in cycle('124'):
    print(i)

    
#drophile


def should_drop(x):
    print 'Testing:', x
    return (x<1)

for i in dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print 'Yielding:', i


#group by


things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print "A %s is a %s." % (thing[1], key)  

