score=0
print("Which day is observed as the independence day of Bangladesh?")
print("Note: Write dates in 'DDst/nd/rd month' format")
ans1=input().lower()
if ans1=="26th march":
    score+=1

print("Which day is observed as the victory day of Bangladesh?")
ans2=input().lower()
if ans2=="16th december":
    score+=1
    
print("In which year did Bangladesh get independent?")
ans3=input()
if ans3=="1971":
    score+=1

print("Which day is observed as international mother language day?")
ans4=input().lower()
if ans4=="21st february":
    score+=1

print("Which is the capital of Bangladesh?")
ans5=input().lower()
if ans5=="dhaka":
    score+=1

print("Your score is:",score,"/5")
