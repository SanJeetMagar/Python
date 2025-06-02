import random
import string
import hashlib
def generate_password(length = 12, uppercase = True, lowercase =True, digit = True, special = True):  
    char = []
    if uppercase:
        char += string.ascii_uppercase
    if lowercase:
        char += string.ascii_lowercase    
    if digit:
        char += string.digits
    if special:
        char += string.punctuation
    if (length <=8):
        print("Weak Password")
    elif(length ==12):
        print("Strong password")

    password = ''
    for i in range(0,length):
        password += random.choice(char)
    return password

password = generate_password(length = 7 , uppercase = True, lowercase =True, digit = True, special = True)  

print("Password:", password)


hashed_password = hashlib.sha256(password.encode())

print('hashed password',hashed_password.hexdigest())

hashed_password = hashlib.sha256(password.encode())

print('hashed password',hashed_password.hexdigest())

