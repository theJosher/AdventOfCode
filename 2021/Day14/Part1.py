import sys
import itertools
from collections import defaultdict, Counter, deque

def defval():
  return 0

def insdefval():
  return []


def runOnFile(filepath : str, iterations : int):
  insertions = []
  pairs_count = defaultdict(defval)
  chars_count = defaultdict(defval)
  with open(filepath) as file:
    string_value = file.readline().strip()
    for c in string_value:
      chars_count[c] += 1
    for i in range(len(string_value)-1):
      char_pair = string_value[i:i+2]
      pairs_count[char_pair] += 1
    for line in file.readlines():
      s = line.split(' -> ')
      if len(s) != 2:
        continue
      char_pair = s[0]
      insertion_char = s[1][0]
      insertions.append([char_pair,insertion_char])

  print(pairs_count)
  print(chars_count)

  for i in range(iterations):
    print("--------------------")
    changes = defaultdict(defval)
    for obj in insertions:
      search_pair = obj[0]
      c = obj[1]
      print("---------")
      if search_pair in pairs_count:
        first_new_pair = search_pair[0] + c
        second_new_pair = c + search_pair[1]
        new_val = pairs_count[search_pair]
        chars_count[c] += new_val
        changes[first_new_pair] += new_val
        changes[second_new_pair] += new_val
        changes[search_pair] -= new_val
        print(search_pair)
        print(pairs_count)
        print(chars_count)
    for k, v in changes.items():
      pairs_count[k] += v
    
  print(pairs_count)
  mini = 999999999999
  maxi = -99999999999
  for k, v in chars_count.items():
    mini = min(mini, v)
    maxi = max(maxi, v)
  print(chars_count)
  print(maxi - mini)

if __name__ == "__main__":
  runOnFile('Day14/ex.txt', 10)
  runOnFile('Day14/input.txt', 40)
