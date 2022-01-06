
def doExplodes(obj,depth, prev_ref):
  #print(depth, obj)
  replacement_obj = []
  split_left = None
  split_right = None
  skip_next = False
  this_prev_ref = prev_ref
  for i in range(len(obj)):
    if skip_next:
      skip_next = False
      continue
    o = obj[i]
    if type(o) == int:
      this_prev_ref = (replacement_obj,len(replacement_obj))
      replacement_obj.append(o if split_right == None else o + split_right)
      continue 
    split_left, split_right, child_o = doExplodes(o,depth+1,this_prev_ref)
    if split_left == None and split_right == None:
      replacement_obj.append(child_o)
    if split_left != None:
      prev = replacement_obj.pop() if len(replacement_obj) > 0 and type(replacement_obj[-1]) == int else None
      if prev != None:
        replacement_obj.append(prev + split_left)
      else:
        #print("o",o)
        if this_prev_ref != None:
          this_prev_ref[0][this_prev_ref[1]] += split_left
          #print("tis ref",this_prev_ref[0][this_prev_ref[1]])
        replacement_obj.append(0)
      split_left = None
    if split_right != None:
      next = obj[i+1] if i < len(obj)-1 and type(obj[i+1]) == int else None
      if next != None:
        skip_next = True
        replacement_obj.append(next + split_right)
        split_right = None
      else:
        replacement_obj.append(0)
  print("Split_right",split_right)
  print(obj,"->",replacement_obj)
  # if we're at a pair...
  if(len(obj) == 2 and type(obj[0]) == int and type(obj[1]) == int):
    if depth >= 4:
      return obj[0] if split_right == None else obj[0] + split_right, obj[1], None
  return split_left, split_right, replacement_obj