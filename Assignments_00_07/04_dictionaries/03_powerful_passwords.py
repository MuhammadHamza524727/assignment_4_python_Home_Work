from hashlib import sha256

def login(email, stored_logins, password_to_check):
    if stored_logins.get(email) == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "muhammadhamza524727@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  
        # password
        
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, stored_logins, password):
        print("\033[1;3;32m Login successful! \033[0m \n")
    else:
        print(" Incorrect email or password.")

if __name__ == '__main__':
    main()


