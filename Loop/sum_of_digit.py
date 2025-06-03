num = int(input("Enter the number u want to sum? "))
orginal = num
digit = 0
while num > 0:
    value = num % 10
    digit += value
    num //= 10
print(f"sum of all number of {orginal} is {digit}")

