import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

enhance_number_times = 50

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day20/input.txt'

def binarify(s):
    return s.replace(".", "0").replace("#","1")

def get_kernel(g, x, y, default_bit):
    k = []
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
          k.append(g.get((i,j), default_bit))
    return "".join(k)
      
def minimax(G):
  minx = 9999999
  maxx = -1
  miny = 9999999
  maxy = -1
  for g in G:
    minx = min(g[0],minx)
    maxx = max(g[0],maxx)
    miny = min(g[1],miny)
    maxy = max(g[1],maxy)
  return minx, maxx, miny, maxy

def pretty_print(G, default_bit):
  minx, maxx, miny, maxy = minimax(G)
  for y in range(miny-3, maxy+5):
      for x in range(minx-3, maxx+5):
          print("#" if G.get((x,y),default_bit) == '1' else '.', end='')
      print('')
  print("\n-----------------------\n")

def enhance(G, enhancement_algo, default_bit):
  minx, maxx, miny, maxy = minimax(G)
  G2 = dict()
  for y in range(miny-1, maxy+2):
      for x in range(minx-1, maxx+2):
        G2[(x, y)] = enhancement_algo[int(get_kernel(G, x, y, default_bit),2)]
  return G2

G = {}
i = 0
width = 0
enhancement_algo = ""
for line in open(infile):
    line = line.strip()
    if i == 0:
        enhancement_algo = binarify(line)
        #print(enhancement_algo)
    elif i != 1 and line != "":
        bline = binarify(line)
        for x in range(len(bline)):
            G[(x, i)] = bline[x]
    i+=1

print(str(G.values()).count('1'))


default_bit = "0"
#pretty_print(G,default_bit)
for i in range(enhance_number_times):
  G = enhance(G,enhancement_algo, default_bit)
  #pretty_print(G,default_bit)
  default_bit = "0" if default_bit == "1" else "1"

print(str(G.values()).count('1'))