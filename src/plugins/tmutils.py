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

from libs.timeutils import schedule
from libs.heaputils import heap_get_default, heap_set, heap_unset, exec_cmd
from libs.timeutils import schedule


def msched(*args):
    for a in args:
        delay = int(a[0])
        cmd = str(a[1])
        schedule(delay, cmd)

def schedule_onoff(id, sec_on, sec_off, cmd_on, cmd_off):
    v = heap_get_default(str(id), 'new')
    if v == 'new':
        heap_set(str(id), 'START')
        schedule(sec_on, cmd_on)
        schedule(sec_off, cmd_off)
        schedule(sec_off, "unset('"+str(id)+"')")
