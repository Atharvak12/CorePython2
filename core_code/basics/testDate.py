# import datetime
# cd=datetime.datetime.now()
# print(cd)

# import datetime as dt
# cd=dt.datetime.now()
# print(cd)

from datetime import datetime
cd=datetime.now()
print(cd)
y=cd.year
m=cd.month
d=cd.day
print("year: " , y)
print("Month: " ,m)
print("Day: " , d)
print("Date :{}/{}/{}".format(d,m,y) )
print("Date:",cd.strftime("%d/%m/%Y"))
print("Date:",cd.strftime("%D"))
print(cd.strftime("%Y"))
print(cd.strftime("%m"))
print(cd.strftime("%d"))
print("Day:",cd.strftime("%a"))
print("Day:",cd.strftime("%A"))
print("Month Name:",cd.strftime("%b"))
print("Month Name:",cd.strftime("%B"))
print("Short Year:",cd.strftime("%y"))
print("Hours:",cd.strftime("%H"))
print("Seconds:",cd.strftime("%S"))
print("Weekday:",cd.strftime("%w"))
print("WeekDay:",cd.strftime("%W"))
print("Month Day:",cd.strftime("%e"))
print("Time period:",cd.strftime("%p"))
print("Time:",cd.strftime("%X"))
print("Zone:",cd.strftime("%Z"))
print("YearDay:",cd.strftime("%j"))

print(cd.strftime("%a %d/%m/%Y %H:%M:%S %p"))

#Write a program to calculate the age 

bdate=datetime(2000,8,12)

print(bdate)