number=int(input("Enter a number:"))
if number%2==0:
    print(number,"is an even number")
elif number%2!=0:
    print(number,"is an odd number")
else:
    print("You just entered an invalid number")

if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
elif number==0:
    print("The number is zero")
else:
    print("The number is invalid")