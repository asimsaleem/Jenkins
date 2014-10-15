import sys

def largest(list):
  if len(list) == 0:
    raise ValueError("Cannot call largest on empty list")
  max = -sys.maxint # "smallest" possible int
  print "Just adding a new print staxxxxxtement"
  #max = 0
  for index in range(len(list)):
    if (list[index] > max):
      max = list[index]
  return max
