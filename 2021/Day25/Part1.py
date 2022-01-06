import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq
from copy import copy, deepcopy


def step_east(state):
  next_state = deepcopy(state)
  moved = False
  for i in range(len(state)):
    for j in range(len(state[i])):
      next_j = (j+1) % len(state[i])
      if state[i][next_j] == '.' and state[i][j] == '>':
        next_state[i][next_j] = '>'
        next_state[i][j] = '.'
        moved = True
        #print("east",i,j,next_j)
  return moved, next_state
        
def step_south(state):
  next_state = deepcopy(state)
  moved = False
  for i in range(len(state)):
    next_i = (i+1) % len(state)
    for j in range(len(state[i])):
      if state[next_i][j] == '.' and state[i][j] == 'v':
        next_state[next_i][j] = 'v'
        next_state[i][j] = '.'
        moved = True
        #print("south",i,j,next_i)
  return moved, next_state

def pretty_print(state):
  for i in range(len(state)):
    for j in range(len(state[i])):
      print(state[i][j],end='')
    print('')
  print('---------------------')

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day25/input.txt'

s = []
for line in open(infile):
  line = line.strip()
  s.append([c for c in line])

pretty_print(s)
b = True
i = 0
while b:
  b, s = step_east(s)
  #pretty_print(s)
  bi, s = step_south(s)
  b = b or bi
  i+=1
pretty_print(s)
print("iterations ",i)

# After 1 step:
# ..vv>..
# .......
# >......
# v.....>
# >......
# .......
# ....v..

# After 2 steps:
# ....v>.
# ..vv...
# .>.....
# ......>
# v>.....
# .......
# .......

# After 3 steps:
# ......>
# ..v.v..
# ..>v...
# >......
# ..>....
# v......
# .......

# After 4 steps:
# >......
# ..v....
# ..>.v..
# .>.v...
# ...>...
# .......
# v......