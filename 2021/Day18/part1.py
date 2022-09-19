import snailfishmath

running_total = snailfishmath.snail_number_list[0]
for snail_number in snailfishmath.snail_number_list[1:]:
  running_total = [running_total,snail_number]
  #print("***************")
  #print(rolling_total)
  #print("***************")
  did_an_op = True
  while did_an_op:
    did_an_op = snailfishmath.do_explosion(running_total)
    if not did_an_op:
      did_an_op = snailfishmath.do_splits(running_total)
    #print("***************")
    #print(rolling_total)
    #print("***************")
print("***************")
print(running_total)
print(snailfishmath.get_magnitude(running_total))