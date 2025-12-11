for i in range(1,21):
    print (i)

numbers=[10,30,50,20,40]

i=0
sum=0
while i<5:
    sum=sum+numbers[i]
    i+=1

print ("The sum is:",sum)

j=0
max=numbers[0]
while j<4:
    if max<numbers[j+1]:
        max=numbers[j+1]    
    j+=1

print ("The max value is =",max)

k=1
min=numbers[0]
while k<5:
    if min>numbers[k]:
        min=numbers[k]    
    k+=1

print ("The min value is =",min)