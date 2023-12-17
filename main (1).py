def create(tsklist):
    task=input("Enter the task Name\n")
    tsklist.append(task)
    print("Task Successfully Created\n")
def edit(tsklist):
    for i in range(len(tsklist)):
        print(i,tsklist[i-1])
    tasknum=int(input("\nWhich task\n"))
    print("Editing Task",tsklist[tasknum],"\n")
    new=input("New Name")
    tsklist[tasknum]=new
    print("Task Successfully Edited\n")
def show_task(tsklist):
    print(tsklist)
def del_task(tsklist):
    for i in range(len(tsklist)):
        print(i,tsklist[i-1])
    tasknum=int(input("\nWhich task\n"))
    print(tsklist)    
    print("Deleting Task",tsklist[tasknum],"\n")
    print("Task Deleted Successfully","\n")
    
#main

print("-------------------------------------------------------------------------")
print("Welcome to the TASK MANAGER\n")
print("-------------------------------------------------------------------------")
tlist=[]
while True:
    print("1.Create")
    print("2.Edit") 
    print("3.List")
    print("4.Delete")
    print("5.Exit\n")
    ch=int(input("Enter the choice\n"))
    if ch==1:
        create(tlist)
    elif ch==2:
        edit(tlist)
    elif ch==3:
        show_task(tlist)
    elif ch==4:
        del_task(tlist)    
    elif ch==5:
        break
    else:
        print("Enter the Valid Choice")
        continue
print("Thanks For Using Task Manager")    
print("-------------------------------------------------------------------------------------------------")