def xyz_there(str):
  index = 0
    
  while True:
      index = str.find("xyz", index)
      if index == -1:
          return False  # No more "xyz" found, return False
        
      # Check the character before "xyz"
      if index == 0 or str[index - 1] != ".":
          return True  # Either "xyz" is at the beginning or not preceded by a period
        
      index += 1  # Move past this "xyz" and continue searching

