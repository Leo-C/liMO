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

import sys

from utils import merge_dicts, load_properties
from libs.logutils import log
import mqttutils
import timeutils

HEAP_PRESET_FILE = 'heap.properties'
heap = {} #heap for called handlers; special values: TOPIC, PAYLOAD
_libs = {}


def heap_init(config_dir):
    global heap
    heap = load_properties(config_dir + '/' + HEAP_PRESET_FILE)

def set_libs(l):
    global _libs
    _libs = l

def merge_heap(d):
    global heap
    heap = merge_dicts(heap, d)

def exec_cmd(cmd, custom_heap):
    global heap, _libs
    d = None
    env = merge_dicts(heap, _libs, custom_heap, {'_d': d})
    log(4, "Executing [%s]" % (cmd))
    try:
        exec "_d="+cmd in env, env
        if type(d) is dict:
            merge_heap(d)
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        sys.stderr.write("ERROR executing [%s]: %s - %s\n" % (cmd,e,v))

def eval_cmd(cmd, custom_heap):
    global heap, _libs
    env = merge_dicts(heap, _libs, custom_heap)
    log(4, "Evaluating [%s]" % (cmd))
    try:
        d = eval(cmd, env, env)
        return d
    except:
        e = sys.exc_info()[0]
        v = sys.exc_info()[1]
        sys.stderr.write("ERROR evaluating [%s]: %s - %s\n" % (cmd,e,v))
        return None

def heap_get_default(varname, default):
    global heap
    if varname in heap:
        return heap[varname]
    else:
        return default

def heap_get(varname):
    return heap_get_default(varname, None)

def heap_set(varname, varvalue):
    global heap
    heap[varname] = varvalue

def heap_unset(varname):
    global heap
    if varname in heap:
        del heap[varname]
