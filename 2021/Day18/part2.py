import snailfishmath
import copy

bigly = -1
for i in range(len(snailfishmath.snail_number_list)):
  for j in range(len(snailfishmath.snail_number_list)):
    if i == j:
      continue
    running_total = [copy.deepcopy(snailfishmath.snail_number_list[i]),copy.deepcopy(snailfishmath.snail_number_list[j])]
    did_an_op = True
    while did_an_op:
      did_an_op = snailfishmath.do_explosion(running_total)
      if not did_an_op:
        did_an_op = snailfishmath.do_splits(running_total)
    bigly = max(snailfishmath.get_magnitude(running_total),bigly)
    # print("***************")
    # print(snail_number_list[i])
    # print(snail_number_list[j])
    # print(running_total)
    # print("=")
    # print(bigly)
    # print("***************")
print(bigly)