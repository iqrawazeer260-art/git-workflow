def login (username, password):
   # simple authentication logic
   if username == "admin" and password == "password:
      return True
   return False

def logout():
     return "user logged out"
