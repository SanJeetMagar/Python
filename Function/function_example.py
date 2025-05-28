#Greeting
# def greeting(Name):
#     return f"Hello, {Name}"
# nam = greeting("Sanjeet")
# print(nam)
# print("Hello,", nam)
#To calculate the area
# def calculate_area(length, breadth):
#     area = length * breadth
#     print(area)
#     return(area)
# area = calculate_area(10 , 10)
# print(area * 2)
#To change celsius to fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = ((celsius * (9/5)) + 32)
#     print(fahrenheit)
#     return fahrenheit
# add = celsius_to_fahrenheit(32)
# print(add + 100)

#Debugging Practice
# def greet(name):
#     return f"{name}"
# info = greet("Sanjeet")
# print("You are the best" ,info , "Best luck for your future:>")

#Advance reuse of function
# def apply_discount(price, discount_percent):
#     print("Orginal price: ", price)
#     after_discount_price = (price *0.9)
#     print("Price after discount: ", after_discount_price)
#     return after_discount_price
# further_discount = apply_discount(100, 20)
# print("Further 10% discount:", further_discount*0.9)

# import math
# def circle_stats(radius):
#     circumference = 2 * math.pi * radius
#     area = math.pi * (radius ** 2)
#     return circumference , area
# stats = circle_stats(10)
# print("Circumference: ", stats[0])
# print(circumference)
# print(area)
# print("Circumference:" , f"{circumference:.2f}")
# print(f"area: {area:.3f}")

# import math

# def circle_stats(radius):
#     area = math.pi *(radius**2)
#     print(area)
#     return area
# stats = circle_stats(3)
# # print("Circumference:", stats[0])  # Should print ~18.85
# print("Area:", f"{stats:.2f}")           # Should print ~28.27



# def sum(x,y):
#     z = x + y
#     return z
# print(sum(12,12))
# a = sum(12, 21)

def add_numbers(a, b):
    result = a + b
    return result  # Returns the value to the caller

sum_result = add_numbers(5, 3)  # sum_result gets the value 8
print(sum_result)  # Output: 8