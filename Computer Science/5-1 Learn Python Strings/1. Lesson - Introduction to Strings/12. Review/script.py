def username_generator(first_name, last_name):
  if len(first_name) < 3 and len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  pw = username[-1] + username[:-1]
  return pw