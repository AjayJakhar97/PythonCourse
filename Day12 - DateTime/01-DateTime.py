# The datetime module supplies classes for manipulating dates and times.

#%% Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
# The date contains year, month, day, hour, minute, second, and microsecond
# The datetime module has many methods to return information about the date object
#%% Return the year and 
print(x)
print(x.year)
print(x.day)
print(x.month)
print(x.hour)
print(x.weekday())

# %% name of weekday
x.strftime("%A")

# %% Let's create a date using datetime constructor. The year, month and day arguments are required. The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone)
x = datetime.datetime(2020, 5, 17)
print(x)

# %% datetime.combine method to Construct a datetime from a given date and a given time.
from datetime import datetime,date,time,timezone
d = date(2020, 5, 17)
t = time(12, 30)
print(datetime.combine(d, t))

# %% display current date and time with time zone
print(datetime.now(timezone.utc))

# %%
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
for i in dt.timetuple():
    print(i)

# %% The strftime() method is for formatting date objects into readable strings and takes one parameter to specify the desired format of the returned string. Visit https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes to find more info about format codes

x = datetime.now()

print(f'Weekday, short version : {x.strftime("%a")}')
print(f'Weekday, full version : {x.strftime("%A")}')
print(f'Weekday as a number 0-6, 0 is Sunday : {x.strftime("%w")}')
print(f'Day of month 01-31 : {x.strftime("%d")}')
print(f'Month name, short version : {x.strftime("%b")}')
print(f'Month name, full version : {x.strftime("%B")}')
print(f'Month as a number 01-12 : {x.strftime("%m")}')
print(f'Year, short version, without century : {x.strftime("%y")}')
print(f'Year, full version : {x.strftime("%Y")}')
print(f'Hour 00-23 : {x.strftime("%H")}')
print(f'Hour 00-12 : {x.strftime("%I")}')
print(f'AM/PM	 : {x.strftime("%p")}')
print(f'Minute 00-59 : {x.strftime("%M")}')
print(f'Second 00-59 : {x.strftime("%S")}')
print(f'Microsecond 000000-999999 : {x.strftime("%f")}')
print(f'Day number of year 001-366 : {x.strftime("%j")}')
print(f'Week number of year, Sunday as the first day of week, 00-53 : {x.strftime("%U")}')
print(f'Week number of year, Monday as the first day of week, 00-53 : {x.strftime("%W")}')
print(f'Local version of date and time	Mon Dec 31 17:41:00 : {x.strftime("%c")}')
print(f'Century : {x.strftime("%C")}')
print(f'Local version of date : {x.strftime("%x")}')
print(f'Local version of time : {x.strftime("%X")}')
print(f'A % character : {x.strftime("%%")}')
print(f'ISO 8601 year : {x.strftime("%G")}')
print(f'ISO 8601 weekday (1-7) : {x.strftime("%u")}')
print(f'ISO 8601 weeknumber (01-53) : {x.strftime("%V")}')

#%% Write a function to calculate the difference between two dates in days.

def diffDate(start,end): 
    '''
    This function returns the difference between two dates in days
    '''
    start = datetime.datetime.strptime(start,"%d/%m/%Y")
    end = datetime.datetime.strptime(end,"%d/%m/%Y")
    return (end-start).days

diffDate("01/01/2019","01/01/2020")

