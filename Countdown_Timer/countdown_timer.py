import time 
import datetime

microsecond = 420
second = 40
minute = 5
hour = 12
day = 30
month = 8
year = 2020

current_time = datetime.datetime.now()  
c_year = current_time.year 
c_month = current_time.month
c_day = current_time.day 
c_hour = current_time.hour
c_minute = current_time.minute
c_second = current_time.second
c_microsecond = current_time.microsecond

# print(current_time)
 
def countdown(difference): 
    d_year = difference.year
    d_month = difference.month
    d_day = difference.day
    d_hour = difference.hour
    d_minute = difference.minute
    d_second = difference.second
    d_microsecond = difference.microsecond

    t = 1
    while t != 0: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        if(d_year <= 0 and d_month <= 0 and d_day <= 0 and d_hour <= 0 and d_minute <= 0 and d_second <= 0 and d_microsecond <= 0):
            print("pooasd")
            t = 0
      
    print('Fire in the hole!!') 



dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
time.mktime(dt.timetuple())

difference = dt - current_time
count_hours, rem = divmod(difference.seconds, 3600)
count_minutes, count_seconds = divmod(rem, 60)
print(difference)
print(difference.seconds)

print(difference.total_seconds)
countdown(difference)