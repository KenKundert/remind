Alarm - Schedule Notification Reminders
=======================================

:Author: Ken Kundert
:Version: 0.0.0
:Released: 2019-01-16


Alarm schedules notification reminders. You can specify the time either using 
a specific time, such as 3:30pm, or you can specify it by the time from now in 
minutes or hours, or you can use both. So, you can say::

    alarm 4pm

    alarm 4pm -15m

    alarm 10m

In the first case the alarm goes off at 4pm, in the second it goes off at 
3:45pm, and in the third it goes off in 10 minutes.  When the alarm goes off 
a notification is raised. You can specify the message in the notification using 
the -m or --msg option.

You can specify the time from now using seconds, minutes, hours, etc.  When 
specifying the time of day, you can use the following formats::

    'h:mm:ss A': ex. 1:30:00 PM, 1:30:00 pm
    'h:mm:ssA': ex. 1:30:00PM, 1:30:00pm
    'h:mm A': ex. 1:30 PM, 1:30 pm
    'h:mmA': ex. 1:30PM, 1:30pm
    'hA': ex. 1PM or 1pm
    'hA': ex. 1PM or 1pm
    'HH:mm:ss': ex. 13:00:00
    'HH:mm': ex. 13:00

To install this program, run the following::

    git clone https://github.com/KenKundert/alarm.git
    cd alarm
    pip3 install --user .
