def typeFunction(a, b, c = 12):
    return a + b + c
d = typeFunction(12, 12)
print(d)

def intro(name, age, level):
    return f"Name: {name} \nAge: {age} \nlevel: {level}"
a = intro("Sanjeet thapa", 21, "Bachelor")
print(a)

def intro(Name):
    Name = input("Enter your name: ")
    print(f"My name is {Name}")
intro("")