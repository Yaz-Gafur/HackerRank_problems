def make_bricks(small, big, goal):
  max_big_bricks = goal // 5
  
  use_big_bricks = min(max_big_bricks, big)
  
  remaining_goal = goal - (use_big_bricks * 5)

  return remaining_goal <= small
