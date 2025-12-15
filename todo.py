print("Do you want to create a task list?")
ans=input("Yes/No:").lower()

TaskList=[]
if ans=="yes":
    n=int(input("Enter the number of tasks:"))
    print("Enter the tasks:")
    for i in range(n):
        TaskList.append(input())
    
    print(TaskList)

    print("Do you want to add a task ?")
    ans1=input("Yes/No:").lower()

    if ans1=="yes":
        Task_name=input("Enter the task name:")
        TaskList.append(Task_name)
        print("Task list has been updated")
        print(TaskList)

    print("Do you want to remove a task ?")
    ans2=input("Yes/No:").lower()

    if ans2=="yes":
        task_number=int(input("Enter the task number:"))
        if task_number>=1 and task_number<=len(TaskList):
            TaskList.pop(task_number-1)
            print("Task list has been updated")
            print(TaskList)
        else:
            print("Invalid task number")
elif ans=="no":
    print("Thank you")