def add(a,b):
  if not isinstance(a, (int, float)) or isinstance(a, bool):
    raise TypeError("Both values must be numbers.")
  if not isinstance(b, (int, float)) or isinstance(b, bool):
    raise TypeError("Both values must be numbers.")
  return a + b