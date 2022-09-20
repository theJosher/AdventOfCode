import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq
from dataclasses import dataclass
import bisect

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day22/example.txt'

@dataclass
class Instruction:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int
    val: bool

def trim(val):
  return max(min(int(val),50),-50)

instructions = []

for line in open(infile):
  l = line.strip()
  to_replace = [' x=','..',',y=', ',z=']
  for s in to_replace:
    l = l.replace(s,' ')
  splitline = l.split(' ')
  instructions.append(Instruction(int(splitline[1]), int(splitline[2]), int(splitline[3]), int(splitline[4]), int(splitline[5]), int(splitline[6]), True if splitline[0] == 'on' else False))
  
removes = list()
for i in instructions:
  if i.x2 > 50 and i.x1 > 50 or i.x1 < -50 and i.x2 < -50:
    removes.append(i)
  elif i.y2 > 50 and i.y1 > 50 or i.y1 < -50 and i.y2 < -50:
    removes.append(i)
  elif i.z2 > 50 and i.z1 > 50 or i.z1 < -50 and i.z2 < -50:
    removes.append(i)
  i.x1 = min(max(i.x1,-50),50)
  i.x2 = min(max(i.x2,-50),50)
  i.y1 = min(max(i.y1,-50),50)
  i.y2 = min(max(i.y2,-50),50)
  i.z1 = min(max(i.z1,-50),50)
  i.z2 = min(max(i.z2,-50),50)
    
for i in removes:
  instructions.remove(i)
#Setup the 3-d matrix that defines the space
space = dict()
print(instructions[-1])
exit
for x in range(-50,51):
  space[x] =dict()
  for y in range(-50,51):
    space[x][y] = dict()
    for z in range(-50,51):
      space[x][y][z] = False
      
for i in instructions:
  for x in range(i.x1,i.x2+1):
    for y in range(i.y1,i.y2+1):
      for z in range(i.z1,i.z2+1):
          space[x][y][z] = i.val
  
volume = 0

for x in range(-50,51):
  for y in range(-50,51):
    for z in range(-50,51):
      if space[x][y][z] == True:
        volume += 1
  
print(volume)
