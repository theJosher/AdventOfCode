import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq
import math
from copy import copy, deepcopy

def runOnInput(input):
  infile = sys.argv[1] if len(sys.argv) > 1 else 'Day24/input.txt'
  vars = {'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
  for line in open(infile):
    line = line.strip()
    instr = [v for v in line.strip().split()]
    if instr[0] == 'inp':
      # inp a - Read an input value and write it to variable a.
      vars[instr[1]] = input.pop()
    else:
      op, a, b = instr
      if b.isnumeric() or (b[0] == '-' and b[1:].isnumeric()):
        b = int(b)
      else:
        b = vars[b]
      if op == 'add':
        # add a b - Add the value of a to the value of b, then store the result in variable a.
        vars[a] = vars[a] + b
      elif op == 'mul':
        # mul a b - Multiply the value of a by the value of b, then store the result in variable a.
        vars[a] = vars[a] * b
      elif op == 'div':
        # div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
        vars[a] = math.floor(vars[a] / b)
      elif op == 'mod':
        # mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
        vars[a] = vars[a] % b
      elif op == 'eql':
        # eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
        vars[a] = 1 if vars[a] == b else 0
  #print(vars['w'],vars['x'],vars['y'],vars['z'])
  return vars['z']

def toBase9(val):
  ret = []
  while val > 0:
    ret.append(val % 9)
    val = math.floor(val / 9)
  return ret

def toSerialNumberList(val):
  l = list(toBase9(max_val))
  for i in range(len(l)):
    l[i] = int(l[i]) + 1
  return l

max_val = int("88888888888888",9)
while max_val > 0: # int("88888888888800",9):
  max = toSerialNumberList(max_val)
  #print(max)
  #print(toBase9(max_val))
  if runOnInput(max) == 0:
    print(max)
    exit()
  max_val -= 1
  