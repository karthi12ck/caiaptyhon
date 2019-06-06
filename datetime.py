# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:02:13 2019

@author: Training23
"""

#1


 def totaltime():
    import time
    import datetime
    print("current date",datetime.datetime.now())
    print("day of year",datetime.date.today().strftime("%j"))
    print("day of month",datetime.date.today().strftime("%A"))
    print("current year",datetime.date.today().strftime("%Y"))
    print("month of year",datetime.date.today().strftime("%B"))
    print("week number of year",datetime.date.today().strftime("%W"))
    print("day of year",datetime.date.today().strftime("%j"))
    print("day of the month",datetime.date.today().strftime("%d"))
    print("day of the week",datetime.date.today().strftime("%A"))    
    
    
    
 def leapyear(l:int):
     if l %4 == 0 and l % 100 !=0 or l % 400 ==0 :
         print("{} is leap year".format(l))
     else:
         print("{} is not a leap year".format(l))
         
         
def stringtodate(n):
    c=datetime.strptime(n,'%b %d %y ')
    return c         


def currentdate():
    from datetime import date
    today=date.today()
    return today


def diffdate(n):
    from datetime import date,timedelta
    date=date.today()-timedelta(n)
    return date
    

def unixtime(n):
    import datetime
    print(datetime.datetime.fromtimestamp(int(n)).strftime('%Y-%m-%d %H:%M:%S'))
    
    
def tomtoday():
    import datetime 
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    tomorrow = today + datetime.timedelta(days = 1) 
    print("today",today)
    print("yesterday",yesterday)
    print("tommorrow",tomorrow)
    
    
def convert():
    from datetime import datetime,date
    dt=date.today()
    print(datetime.combine(dt,datetime.min.time()))  
    
    
  
def nextfive():
    import datetime
    t=datetime.datetime.today()
    for x in range(0,5):
        print(t+datetime.timedelta(days=x))
        
    
def fivesec():
    import datetime
    t=datetime.datetime.today()
    print(t)
    print(t+datetime.timedelta(0,5))
    
def yearof():
    import datetime
    today=datetime.datetime.today()
    year = (today - datetime.datetime(today.year, 1, 1)).days + 1
    print(year)
    
    
def timetomili():
    import time
    milli=int(round(time.time()*1000))
    print(milli)   
    
def weektime():
    import datetime
    print(datetime.date(2019,3,3).isocalender()[1])
        
   
    
def findmonday():
    import time
    print(time.asctime(time.strptime('2019 22 1', '%Y %W %w')))    
    
    
    
def findsunday(year):
    from datetime import date, timedelta



    dt = date(year, 1, 1)
     
    dt += timedelta(days = 6 - dt.weekday())  
    while dt.year == year:
        yield dt
        dt += timedelta(days = 7)
          
    for s in all_sundays(2020):
        print(s)    
        
        
        
def finddiff():
    
    from datetime import date
    from_date=date(2019,2,2)
    to_date=date(2019,4,4)
    delta=to_date-from_date
    print(delta.days
          
          
          
def findtuesday():
    from datetime import date
    from datetime import timedelta
    today = date.today()
    offset = (today.weekday() - 1) % 7
    last_tuesday = today - timedelta(days=offset)
    print(last_tuesday)
    
    
    
def findspecific(year,month):
    import calendar
    print(calendar.monthrange(year,month)[1])
    
def stamptime(s):
    import time
    import datetime
    s = "01/10/2016"

    print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
  
def time(n):
    import time
    import datetime
    print(time.mktime(datetime.datetime.strptime(n, "%d/%m/%Y").timetuple()))
 

def date_diff(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds
def tocheck(l:list,r:int) -> int:
    
    print(r)    