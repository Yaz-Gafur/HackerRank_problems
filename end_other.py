def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a.endswith(b) or b.endswith(a):     # return (a.endswith(b) or b.endswith(a)) ----> same result
    return True
  return False

