#Exercise 4
def chunking_by(list, size):
  for i in range (0, len(list), size):
    print(list[i:i+size])


chunking_by([5, 4, 7, 3, 4, 5, 4], 3)
    