import sys

p = sys.maxsize
n = 0
f = open("Day1/input.txt", 'r')
for l in f.readlines():
    if int(l) > p:
        n += 1
    p = int(l)
print(n)