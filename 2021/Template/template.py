import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'DayXX/example.txt'

G = {}
for line in open(infile):
    line = line.strip()
    x,y = [int(v) for v in line.strip().split(',')]
    G[(x,y)] = True