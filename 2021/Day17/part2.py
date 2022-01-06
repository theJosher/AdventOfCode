import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day17/example.txt'


# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.

def step(pos_init : tuple, v_init : tuple):
  pos = (pos_init[0] + v_init[0], pos_init[1] + v_init[1])
  vel = (v_init[0]-1 if v_init[0] > 0 else (v_init[0]+1 if v_init[0] < 0  else 0) ,v_init[1]-1)
  return pos, vel

def in_target(pos, tgt):
  ((x0, x1), (y0, y1)) = tgt
  x, y = pos
  return x >= x0 and x <= x1 and y >= y0 and y <= y1


# pos always starts at 0,0
# target area: x=20..30, y=-10..-5
global_max_y = -9999999
soln = None
distinct = set()

# The search space needs to be tweaked depending on target area
tgt = ((211,232), (-124,-69))
for x_vel in range(0,400):
  for y_vel in range(-150,300):
    max_y = -99999
    pos = (0,0)
    init_vel = vel = (x_vel,y_vel)
    for steps in range(1000):
      pos, vel = step(pos,vel)
      max_y = max(max_y, pos[1])
      if in_target(pos,tgt):
        distinct.add(init_vel)
print(len(distinct))