class insertion:
  surrounding_chars : str
  insertion_char : str

def generateValTree(s : str):
  d = dict()
  for i in range(len(s)-1):
    d[s[i:i+1]] = []
  return d

def stringFromValTree(d : dict):
  s = []
  for k in d.keys:
    s.append(k[0])
    for v in d[k]:
      s.append[v]
  return "".join(s)

def runOnFile(filepath : str, iterations : int):
  string_value = ""
  insertions = []
  with open(filepath) as file:
    string_value = file.readline()
    for line in file.readlines():
      s = line.split(' -> ')
      if len(s) != 2:
        continue
      new_insert = insertion()
      new_insert.surrounding_chars = s[0]
      new_insert.insertion_char = s[1][0]
      insertions.append(new_insert)
      
  for i in range(iterations):
    val = generateValTree(string_value)
    for insert in insertions:
      val[insert.surrounding_chars].append(insert.new_insert)
    string_value = stringFromValTree(val)
    print(string_value)
    


if __name__ == "__main__":
  runOnFile('Day14/ex.txt', 1)