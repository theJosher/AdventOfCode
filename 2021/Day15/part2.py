import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day15/input.txt'

array = []
for line in open(infile):
    line = line.strip()
    array.append([int(c) for c in line.strip()])

def enquePoint(cur_weight, weights, to_visit, visited, x, y):
  if x >= 0 and x < 5*len(weights) and y >= 0:
    nx = x % len(weights)
    if y < 5*len(weights[nx]) and not (x,y) in visited: 
      ny = y % len(weights[0])
      xw = int(x / len(weights))
      yw = int(y / len(weights[0]))
      pos_weight = weights[nx][ny] + xw + yw
      if pos_weight > 9:
        pos_weight -= 9
      #print('(' + str(weights[nx][ny]) + ')', end='')
      #print(pos_weight, end = '')
      heapq.heappush(to_visit, (pos_weight + cur_weight, x, y))
      visited.add((x,y))


# Heap elements can be tuples! 
# weight,x,y
h = []
v = set()
# for x in range(40,50):
#   for y in range(40,50):
#     enquePoint(0,array,h,v,x,y)
#   print()
# #print(h)
# exit()
heapq.heappush(h,(0,0,0))
while True:
  pos = heapq.heappop(h)
  print(pos)
  w = pos[0]
  x = pos[1]
  y = pos[2]
  if x == len(array)*5-1 and y == len(array[0])*5-1:
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