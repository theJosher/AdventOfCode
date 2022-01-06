import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else 'DayXX/example.txt'

# Returns a 0-based position of the player (0-9) that then needs 1 added to it
ddie = 0
def get_pos_moved_to(cur_pos):
  global ddie
  for _ in range(3):
    real_moves = (ddie % 10) + 1
    cur_pos = (cur_pos + real_moves) % 10
    print( str(ddie % 100 + 1) + ', ', end='')
    ddie += 1
  return cur_pos


def play(pos):
  global ddie
  ddie = 0
  score = [0 for i in range(len(pos))]
  for i in range(len(pos)):
    pos[i] -= 1
  while True:
    for player in range(len(pos)):
      pos[player] = get_pos_moved_to(pos[player])
      space_number = (pos[player] + 1)
      score[player] += space_number
      #Player 1 rolls 1+2+3 and moves to space 10 for a total score of 10.
      print('Player ' + str(player + 1) + " moves to space " + str(space_number) + " for a total score of " + str(score[player]))
      if score[player] >= 1000:
        return min(score[0],score[1]) * ddie
    
  
print(play([10,9]))