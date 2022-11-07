Remind — Schedule Notification Reminders
========================================

.. image:: https://img.shields.io/pypi/v/schedule-reminder.svg
    :target: https://pypi.python.org/pypi/schedule-reminder

.. image:: https://img.shields.io/pypi/pyversions/schedule-reminder.svg
    :target: https://pypi.python.org/pypi/schedule-reminder/


:Author: Ken Kundert
:Version: 1.1
:Released: 2022-11-07


Remind schedules notification reminders. You can specify the time either using 
a specific time, such as 3:30pm, or you can specify it by the time from now in 
minutes or hours, or you can use both. So, you can say::

    remind 4pm

    remind 4pm -15m

    remind 10m

In the first case the reminder goes off at 4pm, in the second it goes off at 
3:45pm, and in the third it goes off in 10 minutes.  When the time expires
a notification is raised. You can specify the message in the notification using 
the -m or --msg option.  Or you can add the message after specifying the time.  
Any argument that cannot be processed as a time switches the argument processing 
from time to message, and all subsequent arguments are taken to be part of the 
message::

    remind 1h meet Maria

You can specify the time from now using seconds, minutes, hours, etc.  For 
example::

    remind 3h 15m

You can use *noon* and *midnight* as aliases for 12PM and 12AM.

When specifying the time of day, you can use the following formats::

    'h:mm:ss A': ex. 1:30:00 PM, 1:30:00 pm
    'h:mm:ssA': ex. 1:30:00PM, 1:30:00pm
    'h:mm A': ex. 1:30 PM, 1:30 pm
    'h:mmA': ex. 1:30PM, 1:30pm
    'hA': ex. 1PM or 1pm
    'HH:mm:ss': ex. 13:00:00
    'HH:mm': ex. 13:00

Be aware that *remind* runs in the background until the appointed time, issues 
the notification, and only then terminates.  If the process is killed or some 
how lost, perhaps by restarting the computer, the reminder is also lost.  
However, you can put the computer to sleep.  When the computer wakes, you will 
either receive a past due notification with an indication that it is being given 
late, or the process will resume waiting for the appointed time.

You can use pip to install the program::

    pip3 install --user schedule-reminder


Releases
--------

**Latest development release**:
    | Version: 1.1
    | Released: 2022-11-07


**1.1 (2022-11-07)**:
    - Enhance implementation so reminders re-synchronize after computer wakes.

**1.0 (2020-07-19)**:
    - Initial production release.
