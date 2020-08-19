def grade_converter(gpa):
  if gpa >= 4:
    return "A"
  elif gpa >= 3:
    return "B"
  elif gpa >= 2:
    return "C"
  elif gpa >=1:
    return "D"
  else:
    return "F"

grade = grade_converter(3.1)
print(grade)

