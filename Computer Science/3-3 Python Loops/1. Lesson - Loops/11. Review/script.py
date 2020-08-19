single_digits = range(10)
squares = []
cubes = [temp ** 3 for temp in single_digits]

for num in single_digits:
  print(num)
  squares.append(num*num)

print(squares)
print(cubes)
