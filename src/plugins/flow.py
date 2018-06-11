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

from libs.heaputils import eval_cmd, exec_cmd, heap_get_default, heap_set


def ifte(cond, if_true, if_false):
    tf = eval_cmd(cond, {})
    if tf:
        exec_cmd(if_true, {})
    else:
        exec_cmd(if_false, {})

def ifundef(var, val, cmd):
    if heap_get_default(var, "") == "":
        heap_set(var, val)
        exec_cmd(cmd, {})
