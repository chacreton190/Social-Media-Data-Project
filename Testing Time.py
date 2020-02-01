from datetime import datetime as dt
import datetime
import sys
date = datetime.date(2016, 7, 24)
date_time = datetime.datetime(2016, 7, 24, 12, 30, 45, 100000)#(YEAR, DAY, MONTH, HOUR, MINUTE, SECOND, MILISECOND)
print("_"*50 + "OUTPUT" + "_"*50)
print(f"The created date is: {date}")
print(f"The type for the created date is: {type(date)}\n")

today = datetime.date.today()
print(f"The today is: {today}")
print(f"The month today is: {today.month}")
print(f"The date today is: {today.day}")
print(f"The day of the week today is: {today.weekday()}")#Monday = 0, Sunday = 6 (.isoweekday() works the same, but is adds 1 to each weekday number
print(f"The year today is: {today.year}")
print(f"The type for today is: {type(today)}\n")

start = dt.time(dt.now())
print(f"The start time is: {start}")
print(f"The type for start time is: {type(start)}\n")

next_week = datetime.timedelta(days=7)
print(f"The start time + the endtime: {today + next_week}") #this is the date 7 days from today
print(f"The type for next_week is: {type(next_week)}\n")
end = datetime.time(2, 30, 00)
begin = datetime.time(3, 30+4, 00)
print(end == begin)
#endtime = dt.time(start + end)


# for i in range(1000000000):
#     print("hello")
#     end = datetime.time(datetime.now()).minute
#     if end - start > 0:
#         sys.exit()