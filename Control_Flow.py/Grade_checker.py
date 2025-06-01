#Basic use of using if elif else.
mask = int(input("Enter Marks You obtained: \n"))
if mask >= 90:
    print("You got A+")
    if mask > 90:
        print("Excellent")
    else:
        print("Good")
elif mask >=80:
    print("You got A.")           
elif mask >= 70:
    print("You got B+")
elif mask >=60:
    print("You got B")
elif mask >=50:
    print("You got C+")
else:
    print("You failed")        
