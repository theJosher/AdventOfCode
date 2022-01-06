import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day05/input.txt'

def defaultPixel():
  return 0

lines = []
for line in open(infile):
    line_points = line.strip().split('->')
    start = line_points[0].split(',')
    end   = line_points[1].split(',')
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])
    lines.append([[x1,y1],[x2,y2]])

pixels = defaultdict(defaultPixel)
for line in lines:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    #print(x1,y1,x2,y2)
    if x1 == x2:
      for y in range(min(y1,y2),max(y1,y2)+1):
        pixels[(x1,y)] += 1
        #print (x1,y)
    elif y1 == y2:
      for x in range(min(x1,x2),max(x1,x2)+1):
        pixels[(x,y1)] += 1
        #print (x,y1)
    else:
      #Guaranteed 45 degrees
      m = int((y2-y1) / abs(x2 - x1))
      #print("m",m)
      y = y1
      inc = 1 if x2>x1 else -1
      for x in range(x1,x2+inc,inc):
        pixels[(x,y)] += 1
        #print (x,y)
        y += m

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# print(" 0123456789")
# for y in range(-1,10):
#   for x in range(0,10):
#     if y == -1:
#       print(x,end='')
#       continue
#     if (x,y) in pixels:
#       print(pixels[(x,y)],end='')
#     else:
#       print('.',end='')
#   print('')

overlaps = 0
for k,v in pixels.items():
  if v > 1:
    overlaps+=1


print(overlaps)
