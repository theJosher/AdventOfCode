import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

print(int(" 12"))

infile = sys.argv[1] if len(sys.argv) > 1 else 'Day04/input.txt'

def emptylist():
  return []

G = {}
i = 0
nums = None
boards = []
boardi = -1
for line in open(infile):
    i += 1
    line = line.strip()
    if i == 1:
      nums = line.split(',')
      continue
    if len(line) == 0:
      boardi += 1
      boards.append([])
      continue
    boards[boardi].append(line.split()) # without arguments, split() will treat all whitespace as a single separator
nums.reverse()

def check_won(board):
  for row in range(len(board)):
    won = True
    for col in range(len(board[row])):
      if board[row][col] != '':
        won = False
        break
    if won:
      return True
  for col in range(len(board[0])):
    won = True
    for row in range(len(board)):
      if board[row][col] != '':
        won = False
        break
    if won:
      return True
  return False


def score(board):
  s = 0
  for row in range(len(board)):
    for v in board[row]:
      if v != '':
        s += int(v)
  return(s)
  
def mark(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == called_number:
        board[row][col] = ''

havent_won = set()
for b in range(len(boards)):
  havent_won.add(b)
while len(nums) > 0:
  called_number = nums.pop()
  for b in range(len(boards)):
    mark(boards[b])
  for b in range(len(boards)):
    if check_won(boards[b]) and b in havent_won:
      if len(havent_won) <= 1:
        print(score(boards[b]) * int(called_number))
        exit()
      havent_won.remove(b)
