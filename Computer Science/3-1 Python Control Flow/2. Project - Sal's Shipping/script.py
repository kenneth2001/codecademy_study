def ground_cost(weight):
  if weight <= 2:
    return weight*1.50+20
  elif weight >2 and weight <= 6:
    return weight*3.00+20
  elif weight >6 and weight <= 10:
    return weight*4.00+20
  else:
    return weight*4.75+20

def drone_cost(weight):
  if weight <= 2:
    return weight*4.50
  elif weight >2 and weight <= 6:
    return weight*9.00
  elif weight >6 and weight <= 10:
    return weight*12.00
  else:
    return weight*14.25

def premium_cost(weight):
  return 125.00;

weight = 41.5

if ground_cost(weight) <= drone_cost(weight) and ground_cost(weight) <= premium_cost(weight):
  print("Ground Shipping is the cheapest")
  print(ground_cost(weight))
elif drone_cost(weight) <= ground_cost(weight) and drone_cost(weight) <= premium_cost(weight):
  print("Drone Shipping is the cheapest")
  print(drone_cost(weight))
else:
  print("Premium Ground Shipping is the cheapest")
  print(premium_cost(weight))


