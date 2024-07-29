def lucky_sum(a, b, c):
  sum = 0
  if a != 13 and b != 13 and c != 13:
    sum = a + b + c
  elif a == 13:
    return sum
  elif b == 13:
    sum = a
  else:
    sum = a + b
  return sum
