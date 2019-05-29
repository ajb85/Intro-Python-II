def setID():
  id = 0
  def incrementID():
    nonlocal id 
    id += 1
    return id
  return incrementID