sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0


for location in sales_data:
  print(location)
  for i in range(3):
    scoops_sold += location[i]

print(scoops_sold)
