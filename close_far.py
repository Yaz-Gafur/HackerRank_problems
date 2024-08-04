def close_far(a, b, c):
  close_b_far_c = abs(b - a) <= 1 and abs(c -a) >= 2 and abs(c - b) >= 2
  
  close_c_far_b = abs(c - a) <= 1 and abs(b -a) >= 2 and abs(b - c) >= 2
  
  return close_b_far_c or close_c_far_b
