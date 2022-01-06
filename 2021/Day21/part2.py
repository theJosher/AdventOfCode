import sys
import itertools
from collections import defaultdict, Counter, deque
import heapq
from functools import lru_cache

# we use the call stack along with the lru_cache to "create all the universes" without duplicating any ;-)
# Note that we convert between list and tuple a lot because list isn't hashable and tuple is immutible and thus can't have indices changed
# Regardless of the conversions, the code is more concise and easier to read this way
@lru_cache(maxsize=None)
def get_winning_player(turn_of_player : int, rolls : tuple, pos : tuple, score : tuple):
  if score[0] >= 21:
    return (1,0)
  if score[1] >= 21:
    return (0,1)
  roll_index = None
  these_rolls = list(rolls)
  if these_rolls[0] < 0:
    roll_index = 0
  elif these_rolls[1] < 0:
    roll_index = 1
  elif these_rolls[2] < 0:
    roll_index = 2
  else:
    these_pos = list(pos)
    these_score = list(score)
    these_pos[turn_of_player] = (these_pos[turn_of_player] + sum(rolls)) % 10
    these_score[turn_of_player] += (these_pos[turn_of_player] + 1)
    turn_of_player = 0 if turn_of_player == 1 else 1
    return get_winning_player(turn_of_player,(-1,-1,-1),tuple(these_pos),tuple(these_score))
  these_rolls[roll_index] = 1
  a = get_winning_player(turn_of_player,tuple(these_rolls),pos,score)
  these_rolls[roll_index] = 2
  b = get_winning_player(turn_of_player,tuple(these_rolls),pos,score)
  these_rolls[roll_index] = 3
  c = get_winning_player(turn_of_player,tuple(these_rolls),pos,score)
  return (a[0] + b[0] + c[0], a[1] + b[1] + c[1])

def play(pos):
  global ddie
  ddie = 0
  score = (0,0)
  for i in range(len(pos)):
    pos[i] -= 1
  return get_winning_player(0,(-1,-1,-1),tuple(pos),score)
  
number_universes_won = play([10,9])
print(max(number_universes_won[0],number_universes_won[1]))