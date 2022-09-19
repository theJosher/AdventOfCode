import sys
import json
from collections import defaultdict, Counter, deque
import math

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day18/infile.json'

# build a collection of snailfish numbers that we will later do snailfish arithmetic on
snail_number_list = []
with open(infile,'r') as file:
  for line in file:
    snail_number_list.append(json.loads(line))

# Finds the first snailfish number at a depth > 4, along with the left and right values
def find_explosion(obj, depth = 1, s = None, l = None, r = None):
  # we'll only get to an int if it's a pair
  for i in range(len(obj)):
    # #print("=======")
    # #print(obj[i])
    if depth > 4 and s == None and isinstance(obj[i],int) and i<len(obj) and isinstance(obj[i+1],int):
      # #print("DAMN!")
      return True, l, r
    elif r == None:
      # If we have a list other than a pair, recurse and then get left and right values if something is found
      if isinstance(obj[i],list):
        new_s, l, r = find_explosion(obj[i],depth + 1, s, l, r)
        if new_s != None and s == None:
          if isinstance(new_s,bool) and new_s == True:
            s = obj, i
          else:
            s = new_s
      elif isinstance(obj[i], int):
        if s == None:
          l = (obj, i)
        if s != None and r == None:
          r = (obj, i)
          return s, l, r
  return s, l, r

# explodes the first snailfish number (pair) at a depth > 4
def do_explosion(obj):
  #print("----------")
  s, l, r = find_explosion(obj)
  #print("s=" + str(s))
  #print("l=" + str(l))
  #print("r=" + str(r))
  if s == None:
    # Let the caller know a split wasn't found
    return False
  if l != None:
    #print(l[0][l[1]])
    l[0][l[1]] += s[0][s[1]][0]
  if r != None:
    #print(r[0][r[1]])
    r[0][r[1]] += s[0][s[1]][1]
  # Finally, we always set the pair to a 0 if a split was found
  s[0][s[1]] = 0
  # let caller know a split was found
  return True

# Searches for the first normal number that is >=10 and splits it, modifying the referenced object
def do_splits(obj):
  if type(obj) == int:
    if obj >= 10:
      return [math.floor(obj/2),math.ceil(obj/2)]
    return obj
  for i in range(len(obj)):
    #print(obj)
    o2 = do_splits(obj[i])
    if isinstance(o2,bool):
      # already handled in the recursion, so stop seeking and keep passing up True
      return True
    elif o2 != None and obj[i] != o2:
      obj[i] = o2
      # change the referenced object to the split object, and pass up True so we know to stop seeking
      return True
  return None

# Recursively get magnitude of any snailfish number
def get_magnitude(obj):
  if isinstance(obj, int):
    return obj
  elif isinstance(obj,list):
    l = get_magnitude(obj[0])
    r = get_magnitude(obj[1])
    return 3*l + 2*r
