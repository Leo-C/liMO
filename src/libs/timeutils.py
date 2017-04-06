'''
Copyright 2017 - LC

This file is part of liMO.

liMO is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

liMO is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with liMO.  If not, see <http://www.gnu.org/licenses/>.
'''

import time
import datetime

from libs.logutils import log

schedules = {} #scheduled events with keys in format of GMT 'YYYYMMDDhhmmss' and command as string


def sched_init():
    global schedules
    schedules = {}

def strtime(t):
    if type(t) is time.struct_time:
        return time.strftime("%Y%m%d%H%M%S", t)
    elif type(t) is datetime.datetime:
        return time.strftime("%Y%m%d%H%M%S", t.timetuple())
    else:
        return None

def strnow():
    return strtime(datetime.datetime.utcnow())

def timeleft(str_t): #return seconds
    now = datetime.datetime.utcnow()
    t = parse_strtime(str_t)
    return (t - now).total_seconds()

def parse_strtime(str_t):
    return datetime.datetime.strptime(str_t, "%Y%m%d%H%M%S")

def schedule(delay_sec, cmd):
    global schedules
    trig_time = datetime.datetime.utcnow() + datetime.timedelta(seconds = delay_sec)
    if strtime(trig_time) in schedules:
        l = schedules[strtime(trig_time)]
    else:
        l = []
        schedules[strtime(trig_time)] = l
    l.append(cmd)

def scheduler():
    import heaputils
    global schedules
    sched = sorted(schedules.keys())
    for str_t in sched:
        t = parse_strtime(str_t)
        if t < datetime.datetime.utcnow() + datetime.timedelta(microseconds = 500000):
            tl = schedules[str_t]
            for t in tl:
                log(4, "Scheduled task [%s] @ '%s'" % (t,str_t))
                heaputils.exec_cmd(t, {})
            del schedules[str_t]
        else:
            break
