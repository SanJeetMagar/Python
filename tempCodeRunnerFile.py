
        if not length:
            feedback += "\n- at least 12 character" 
        return feedback
def main():
    password = input("Create password: ")
    result = check_password_strength(password) 
    print("\n" + result)