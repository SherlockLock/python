import datetime


#Get the current time

now = datetime.datetime.now()

print(now)

#Now contains information about the year, month, day, hour, minute, second, and microsecond
#all of which can be accessed as properties


#We can create custome date objects
uncle_sams_birthday = datetime.datetime(1776,7,4)

#We can format these these dates in a variety of ways using the following method
now.strftime("") #Search Documentation for specifics
