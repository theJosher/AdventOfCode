import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day15/example.txt'

array = []
for line in open(infile):
    line = line.strip()
    array.append([int(c) for c in line.strip()])

def enquePoint(cur_weight, weights, to_visit, visited, x, y):
  if x >= 0 and x < len(weights) and y>=0 and y < len(weights[x]) and not (x,y) in visited: 
    heapq.heappush(to_visit, (weights[x][y] + cur_weight, x, y))
    visited.add((x,y))


# Heap elements can be tuples! 
# weight,x,y
h = []
v = set()
heapq.heappush(h,(0,0,0))
while True:
  pos = heapq.heappop(h)
  w = pos[0]
  x = pos[1]
  y = pos[2]
  print(w)
  if x == len(array)-1 and y == len(array[x])-1:
    print(w)
    exit()
  #Left
  enquePoint(w, array, h, v, x-1,y  )
  #Right
  enquePoint(w, array, h, v, x+1,y  )
  #Up
  enquePoint(w, array, h, v, x,  y-1)
  #Down
  enquePoint(w, array, h, v, x,  y+1)


print(array)