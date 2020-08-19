def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  temp = []
  for c in string_one:
    if c in string_two and c not in temp:
      temp.append(c)
      continue
  return temp

print(common_letters('manhattan', 'san francisco'))