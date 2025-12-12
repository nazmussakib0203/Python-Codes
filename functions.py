def add(a,b):
    return a+b

sum=add(10,10)
print("The sum is:",sum)

def is_even(num):
    if num%2==0:
        return True
    elif num%2!=0:
        return False
    
result=is_even(43)
print("Is_Even:",result)

def square_list(numbers):
    for i in range(len(numbers)):
        numbers[i]=numbers[i]*numbers[i]
    return numbers

numbers = square_list([1,2,3,4,5])
print("Square numbers are:",numbers)