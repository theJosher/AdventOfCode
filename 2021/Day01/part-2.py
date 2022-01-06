# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H

import sys

p = sys.maxsize
n = 0
history = []
f = open("Day1/input.txt", 'r')
for l in f.readlines():
    value = int(l)
    history.append(value)
    if len(history) > 3:
      h = history.pop(0)
      if value > h:
        n += 1
print(n)