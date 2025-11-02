import random#
import string

def generate_password(length=None):
    lowercase = string.ascii_lowercase 
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = lowercase + uppercase + digits + symbols
    
    if length is None:
        try:
            length_input = input("Enter password length: ")
            length = int(length_input.strip())
            
            if length < 8:
                print("Password must be at least 8 characters long for security.")
                return None
                
        except ValueError:
            print("Please enter a valid number.")
            return None

    password_list = []
    for _ in range(length):
        random_char = random.choice(all_characters)
        password_list.append(random_char)
    
    password = "".join(password_list)
    
    print(f"Here is your password: {password}") 
    return password

if __name__ == "__main__":
    generate_password()