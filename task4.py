tasks=[]
print("welcome to the to_do list abb")


while True:
    print("choose an option:")
    print("1:add task")
    print("2:view task")
    print("3:delet task")
    print("4:Exit")
    

choice=input("enter your choice 1-4:")
if choice=="1":
    value=input("enter your task:")
    tasks.append(value)
    print("task added!")

elif choice=="2":
    if not tasks:
        print("no tasks yet")
    else:
        print("your tasks")
        i=1
        for data in tasks:
            print(i,data)
            i+=1
elif choice=="3":
    if not tasks:
        print("No Tasks to delete : ")
    else:
        i =1
        for data in tasks:
            print (i, data)
            i+=1


        task_number=input("enter task number to delete")
        task_number=int(task_number)
        if task_number>=1 and task_number<=len(tasks):
            delete=tasks.pop(task_number-1)
            print(f"deleted task is{deleted}")
        else:
            print("invalid value")

elif choise==4:
    print("God bye")
    break
    
