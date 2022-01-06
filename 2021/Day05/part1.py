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
    if line[0][0] == line[1][0]:
      ymin = min(y1,y2)
      ymax = max(y1,y2)
      for y in range(ymin,ymax+1):
        pixels[(x1,y)] += 1
      #print ("v",x1,ymin,ymax)
    elif line[0][1] == line[1][1]:
      xmin = min(x1,x2)
      xmax = max(x1,x2)
      #print ("h",y1,xmin,xmax)
      for x in range(xmin,xmax+1):
        pixels[(x,y1)] += 1

overlaps = 0
for k,v in pixels.items():
  if v > 1:
    overlaps+=1


print(overlaps)
#print(pixels)
