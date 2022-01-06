import sys
import itertools
import json
from collections import defaultdict, Counter, deque
import heapq
import math

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day18/example.txt'

# If any pair is nested inside four pairs, the leftmost such pair explodes.
# If any regular number is 10 or greater, the leftmost such regular number splits.
obj = json.load(open(infile))

# def split(o):
#   if len(o) == 2 and type(o[0]) and type(o[1]) == int:
#     if depth > 4:
#       return 0
#     else:
#       return 1 #

# 

def doSplits(obj):
  if type(obj) == int:
    if obj >= 10:
      return [math.floor(obj/2),math.ceil(obj/2)]
    return obj
  new_obj = []
  for o in obj:
    new_obj.append(doSplits(o))
  return new_obj

# returns next, obj
def doExplodes(obj, depth, prev):
  this_prev = prev
  for i in range(len(obj)):
    o = obj[i]
    next, obj = doExplodes(o, depth + 1, this_prev, )

    this_prev = (obj,i)

if __name__ == "__main__":
  o = obj
  prev = None
  i = 0
  print(o)
  while str(prev) != str(o) and i < 4:
    prev = o
    l,r,o = doExplodes(o,0,None)
    print(str(o))
    o = doSplits(o)
    i+=1
    print(str(o))
#   after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
# after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
# after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
# after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]