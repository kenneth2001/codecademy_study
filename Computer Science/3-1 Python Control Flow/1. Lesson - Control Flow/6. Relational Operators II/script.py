def greater_than(x, y):
  if x > y:
    return x
  elif x < y:
    return y
  elif x == y: 
    return "These numbers are the same"

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

print(graduation_reqs(120))