# Authentication Module

def login(username, password):
    # Simple authentication logic
    if username == "admin" and password == "password":
        return True
    return False

def logout():
    return "User logged out"

def validate_input(username, password):
    if not username or not password:
        return False
    return True