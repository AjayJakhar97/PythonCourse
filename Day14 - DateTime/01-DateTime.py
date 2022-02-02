# The datetime module supplies classes for manipulating dates and times.

#%% Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
# The date contains year, month, day, hour, minute, second, and microsecond
# The datetime module has many methods to return information about the date object
#%% Return the year and 
x.year

# %% name of weekday
x.strftime("%A")

# %% Let's create a date using datetime constructor. The year, month and day arguments are required. The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone)
x = datetime.datetime(2020, 5, 17)
print(x)

# %% The strftime() method is for formatting date objects into readable strings and takes one parameter to specify the desired format of the returned string. Visit https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes to find more info about format codes

x.strftime("%B")
# %% 
import datetime
x = datetime.tim
x.year
# %% datetime.combine method to Construct a datetime from a given date and a given time.
from datetime import datetime,date,time,timezone
d = date(2020, 5, 17)
t = time(12, 30)
print(datetime.combine(d, t))
# %% display current date and time with time zone
datetime.now(timezone.utc)
# %%
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)
for i in dt.timetuple():
    print(i)
# %%

