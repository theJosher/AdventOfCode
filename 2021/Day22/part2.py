import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq
from dataclasses import dataclass
import bisect

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day22/example.txt'

@dataclass 
class ReducedSpace:
  x_map: list 
  y_map: list 
  z_map: list
  space: list

@dataclass
class Instruction:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    val: bool

instructions = []

for line in open(infile):
  l = line.strip()
  to_replace = [' x=','..',',y=', ',z=']
  for s in to_replace:
    l = l.replace(s,' ')
  splitline = l.split(' ')
  instructions.append(Instruction(int(splitline[1]), int(splitline[2]), int(splitline[3]), int(splitline[4]), int(splitline[5]), int(splitline[6]), True if splitline[0] == 'on' else False))
  
#Setup the 3-d matrix that defines the space
space = ReducedSpace(list(),list(),list(),list())
x_set = set()
y_set = set()
z_set = set()
for i in instructions:
  x_set.add(i.x1)
  x_set.add(i.x2)
  y_set.add(i.y1)
  y_set.add(i.y2)
  z_set.add(i.z1)
  z_set.add(i.z2)
space.x_map = sorted(x_set)
space.y_map = sorted(y_set)
space.z_map = sorted(z_set)
print(space.x_map)
print(space.y_map)
print(space.z_map)

volume = 0
for x in range(len(space.x_map)):
  space.space.append([])
  for y in range(len(space.y_map)):
    space.space[x].append([])
    for z in range(len(space.z_map)):
      space.space[x][y].append(False)
      
for i in instructions:
  for x in range(bisect.bisect_left(space.x_map,i.x1),bisect.bisect_left(space.x_map,i.x2)+1):
    for y in range(bisect.bisect_left(space.y_map,i.y1),bisect.bisect_left(space.y_map,i.y2)+1):
      for z in range(bisect.bisect_left(space.z_map,i.z1),bisect.bisect_left(space.z_map,i.z2)+1):
        #print("x,y,z=" + str(x) + "," + str(y) + "," + str(z) + " = " + str (i.val))
        space.space[x][y][z] = i.val
  
for x in range(len(space.x_map)):
  for y in range(len(space.y_map)):
    for z in range(len(space.z_map)):
      if space.space[x][y][z] == True and x > 0 and y > 0 and z > 0:
        xdiff = space.x_map[x] - space.x_map[x-1] + 1
        ydiff = space.y_map[y] - space.y_map[y-1] + 1
        zdiff = space.z_map[z] - space.z_map[z-1] + 1
        # print("----------------")
        # print("xdiff=" + str(xdiff))
        # print("ydiff=" + str(ydiff))
        # print("zdiff=" + str(zdiff))
        # print(xdiff * ydiff * zdiff)
        volume += (xdiff * ydiff * zdiff)
  
print(volume)
#2835452121880734
#vs the expected result
#2758514936282235
