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

import os
import sys
import imp
import glob

from libs.utils import load_properties
from libs.heaputils import set_libs
from libs.logutils import log

import libs
from plugins import *

SCRIPTING_CONFIG_FILE = 'scripting.properties'


def init_plugins(config_dir):
    sl = load_properties(config_dir + '/' + SCRIPTING_CONFIG_FILE)
    ll = {}
    for l in sl:
        try:
            ll[l] = eval(sl[l])
        except:
            log(1, "Error loading plugin '" + sl[l] + "'")
            sys.exit()
    set_libs(ll)

def printlog(level, message):
    log(level, str(message))

def nop():
    pass
