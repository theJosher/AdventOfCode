
def foldOver(tuple, fold_on_value, fold_on_direction : int):
  my_fold = tuple[fold_on_direction] - (tuple[fold_on_direction] - fold_on_value) * 2
  new_elem = [tuple[0],tuple[1]]
  new_elem[fold_on_direction] = my_fold
  return new_elem

def updateCorner(tuple, fold_on_value, fold_on_direction : int):
  my_fold = fold_on_value - 1
  new_elem = [tuple[0],tuple[1]]
  new_elem[fold_on_direction] = my_fold
  return new_elem

  
def runOnFile(path : str, folds : int):
    transparency = set()
    fold_along_token = 'fold along '
    corner = (0,0)
    with open(path) as file:
        for l in file.readlines():
            s = l.split(',')
            if len(s) == 2:
                t = (int(s[0]),int(s[1]))
                corner = (max(t[0],corner[0]),max(t[1],corner[1]))
                transparency.add(t)
            elif l.startswith(fold_along_token):
                i = len(fold_along_token)
                direction = 0 if (l[i:i+1].strip()) == 'x' else 1
                fold_value = int(l[i+2:].strip())
                min_fold = [0,0]
                remove = set()
                add_folds = set()
                #print(corner)
                corner = updateCorner(corner, fold_value, direction)
                #print(corner)
                for element in transparency:
                  if element[direction] > fold_value:
                    remove.add(element)
                    new_elem = foldOver(element, fold_value, direction)
                    add_folds.add(tuple(new_elem))
                    min_fold = (min(new_elem[0],min_fold[0]),min(new_elem[1],min_fold[1]))
                  elif element[direction] == fold_value:
                    remove.add(element)
                # Remove everything you don't want
                for r in remove:
                  transparency.remove(r)
                for a in add_folds:
                  transparency.add(a)
                print(min_fold)
                folds -= 1
            elif len(l.strip()) > 0:
                print('WTF: ' + l)
            if folds <= 0:
              break
    myPrint(transparency, corner)
    print(len(transparency))
    #print(transparency)
    return len(transparency)

def myPrint(transparency, corner):
  for x in range(corner[0]+1):
    for y in range(corner[1]+1):
      if (x,y) in transparency:
        print('#', end='') 
      else:
        print('.', end='') 
    print('')

# Test Cases:
if __name__ == "__main__":
    print("--------------------------------- TC1 ---------------------------------")
    # assert runOnFile('Day13/example.txt', 1) == 17, "Failed example 1-fold"
    # assert runOnFile('Day13/example.txt', 2) == 16, "Failed example 2-fold"
    # assert runOnFile('Day13/input.txt',1) == 661, "Failed 1-fold"
    # assert runOnFile('Day13/t1.txt', 1) == 1, "TC1 1-fold"
    # assert runOnFile('Day13/t2.txt', 1) == 1, "TC2 1-fold"
    print(runOnFile('Day13/input.txt',99999999))