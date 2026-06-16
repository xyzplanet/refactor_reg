users = {"user1": "password1", "user2": "password2"}

def is_valid_user(username):
    return username in users
    
def check_password(username, password):
    return users.get(username) == password
    
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if not is_valid_user(username):
        print("Username and/or password not found")
        return
        
    if check_password(username, password):
        print("Login successful!")
    else:
        print("Incorrect password.")
    
# Example usage
login()
