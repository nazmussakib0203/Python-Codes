dailyTasks = ["Wake Up","Study","Gym","Walk","Sleep"]

dailyTasks.append("Pray")
dailyTasks.insert(1,"Pray")
dailyTasks.pop()
dailyTasks.remove("Sleep")
dailyTasks.append("Sleep")
print(dailyTasks)

for i in dailyTasks:
    print(i)

status = {"Name":"Safwan",
          "Goal":"To learn Python",
          "Level":"Beginner"
          }

status["Level"]="Basic"
status["Age"]=22
#status.pop("Age")
del status["Age"]
print(status)
print(status.values())
print(status.keys())
print(status.items())

for key in status:
    print(key,status[key])