def test(z):
    z = 12 #It is a local variable
    print(z)
z = 13 #It is a gobal vairaible
print(z)

# How to modify gobal varible
def modifyGlobal():
    global x
    x = 12
x = 1
modifyGlobal()
print(x)