"""
Section:
    datetime

Author:
    Simon Ward-Jones

Description:
    How to convert strings to datetimes and back again

Tags:
    datetime, pytz
"""
import datetime
import pytz

#############################################
# Converting from datetime to string
#############################################

# let's make one date object and a couple of datetimes

today = datetime.date.today()
now_utc = datetime.datetime.now(tz=pytz.utc)
now = datetime.datetime.now()
# note pytz has lot's of timezones
# see pytz.all_timezones
pytz.utc is pytz.timezone('UTC')


# We can use the isoformat function to get string in ISO 8601 format
iso_today = today.isoformat()
iso_now = now.isoformat()
iso_now_utc = now_utc.isoformat(sep=' ')

print(f'iso_today is {iso_today}')
print(f'iso_now is {iso_now}')
print(f'iso_now_utc is {iso_now_utc}')


# we can use strftime to string format time
print(now.strftime('%Y-%m-%dT%H:%M:%SZ.%f'))

for formatter in ['%a', '%A', '%w', '%d', '%b', '%B', '%m', '%y', '%Y',
                  '%H', '%I', '%p', '%M', '%S', '%f', '%z', '%Z', '%j', 
                  '%U', '%W', '%c', '%x', '%X']:
    print(f'now_utc formatted with {formatter} '
          f'gives {now_utc.strftime(formatter)}')


#############################################
# Converting from string to datetime.datetime
#############################################

datestring = '2018-03-12T10:12:45Z'
datestring_2 = '2018/07/21 11:54:15.631000'

datetime_obj = datetime.datetime.strptime(
    datestring, '%Y-%m-%dT%H:%M:%SZ')
datetime_obj_2 = datetime.datetime.strptime(
    datestring_2, '%Y/%m/%d %H:%M:%S.%f')

print(f'datetime_obj is {datetime_obj.isoformat()}')
print(f'datetime_obj_2 is {datetime_obj_2.isoformat()}')

# More examples:
# "Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"
# "September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"
# "Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"
# "Mon, 21 March, 2015" -> "%a, %d %B, %Y"
# "2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"
