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
import glob

all_list = list()
for f in glob.glob(os.path.dirname(__file__)+"/*.py"):
    if os.path.isfile(f) and not os.path.basename(f).startswith('_'):
        all_list.append(os.path.basename(f)[:-3])

__all__ = all_list
