def reversed_list(lst1, lst2):
  a = 0
  for i in range(len(lst1)):
    if lst1[i] == lst2[len(lst1)-1-i]:
      a += 1
     
  if a == len(lst1):
    return True
  else:
    return False 


#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))