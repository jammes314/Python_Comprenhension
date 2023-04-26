import numbers
from sqlite3 import Timestamp
import sys
from unittest import result

print(sys.path)

import re

text = 'mi numero es 3222 234 234, el codigo es +593'

result = re.findall('[0-9]+', text)
print(result)

import time 
Timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

print(Timestamp)

import collections
numbers = [1,2,3,4,5,6,7,8,9,10,11,1,1,2]

counter = collections.Counter(numbers)
print(counter)