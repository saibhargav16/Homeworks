def bunnyEars2(bunnies):
  if (bunnies == 0):
    return 0
  else:
    if (bunnies % 2 == 0):
      return 3 + bunnyEars2 (bunnies - 1)
    else:
      return 2 + bunnyEars2 (bunnies - 1)


print(bunnyEars2(0)) 
print(bunnyEars2(1)) 
print(bunnyEars2(2)) 