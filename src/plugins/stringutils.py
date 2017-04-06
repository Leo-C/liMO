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

def substring(text, start, length):
    if start < 1:
        b = len(text) + start + 1
        e = b + length
    else:
        b = start + 1
        if length < 1:
            e = len(text) + length
    
    return text[b-1:e]

def strlen(text):
    return len(text)

def tostr(any):
    return str(any)

def tonum(text, default):
    try:
        return float(str(text))
    except:
        return default
