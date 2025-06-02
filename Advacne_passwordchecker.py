import string
def check_password_strength(password):
    has_lowercase = any(char in string.ascii_lowercase for char in password)
    has_uppercase = any(char in string.ascii_uppercase for char in password)
    has_special = any(char in string.punctuation for char in password )
    has_digit = any(char in string.digits for char in password)
    length = len(password) >= 12
    if has_lowercase and has_uppercase and has_digit and has_special and length:
        return "Strong password"
    else:
        feedback = "Weak password "
        if not has_lowercase:
            feedback += "\n- at least add one Lowercase letter"
        if not has_uppercase:
            feedback += "\n- at least add one Uppercase letter"
        if not has_special:
            feedback += "\n- at least add one Special"
        if not has_digit:
            feedback += "\n- at least add one Digit" 
        if not length:
            feedback += "\n- at least 12 character" 
        return feedback
def main():
    password = input("Create password: ")
    result = check_password_strength(password) 
    print("\n" + result)
if __name__ == "__main__":                    
    main()      
