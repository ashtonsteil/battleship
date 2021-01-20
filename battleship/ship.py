class Ship(object):
  def __init__(self, start, end):
    self.start, self.end = start, end  # ('A', 1), ('A', 2)
    self.state = [False] * self.length

  def check_sunk(self):
    return all(self.state)

  @property
  def length(self):
    return abs(ord(self.end[0]) - ord(self.start[0])) + abs(self.end[1] - self.start[1])
  
  def hit(self, location):
    if self.orientation == 'horizontal':
      if self.position[0] != location[0]:
        return False
      for i in range(self.length):
        if self.position[1] + i == location[1]:
          self.state[i] = True
          return True
      return False

    if self.orientation == 'vertical':
      if self.position[1] != location[1]:
        return False
      for i in range(self.length):
        if chr(ord(self.position[0]) + i) == location[0]:
          self.state[i] = True
          return True
      return False

  @property   
  def orientation(self):
    if self.start[0] == self.end[0]:
      return 'horizontal'
    return 'vertical'

  @property
  def position(self):
    return sorted([self.start, self.end])[0]