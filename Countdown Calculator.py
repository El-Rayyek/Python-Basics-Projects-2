'''
task :
Build a countdown calculator. Write some code that can take two dates as input,
and then calculate the amount of time between them
'''
import datetime


entry_date1 = input("Enter a First Date at DD/MM/YYYY format :")
entry_date2 = input("Enter a First Date at DD/MM/YYYY format :")

day1,month1,year1 = map(int,entry_date1.split('/'))
day2,month2,year2 = map(int,entry_date2.split('/'))
date1 = datetime.date(year1,month1,day1)
date2 = datetime.date(year2,month2,day2)
delta = date1-date2 
print(f"The Time between these is :{abs(delta.days)} Days")
#count_between_date(date1,date2)