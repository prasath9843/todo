import json 
import os
file_name="todo_project.json"
if not os.path.exists(file_name):
    with open(file_name,"w") as f:
        json.dump([],f)
def load():
    with open(file_name,"r")as f:
        return json.load(f)
def save_task(t):
    with open(file_name,"w") as f:
        json.dump(t,f)
def create():
    a=input("enter the task that u want to add:")
    loading_task=load()
    loading_task.append({"id":len(loading_task)+1,"task":a,"status0":False})
    save_task(loading_task)
    print("task added")
def show():
    x=load()
    if not x:
        print("no task are available in your to do list")
    else:
        for i in x:
            status1=i["status0"]
            if status1:
                print(i["id"]," ",i["task"]," Completed")
            else:
                print(i["id"]," ",i["task"]," Not completed")
def update_task():
    show()
    n=int(input("Enter the task id to update the task"))
    task3=load()
    for i in task3:
        if n==i["id"]:
            print("1:change the status of the task \n2:change the name of the task")
            ch=int(input("enter the option"))
            if ch==1:
                i["status0"]=True
                save_task(task3)
            if ch==2:
                stri=input("enter the new task name that u want to edit")
                i["task"]=stri
                save_task(task3)
            else:
                print("ur choice is wrong")
        else:
            print("no task is found to upadate todo list")
def delete_task():
    show()
    ch=int(input("enter the task number to delete the task in the todo"))
    task4=load()
    k=1
    new_task=[]
    for i in task4:
        if ch!=i["id"]:
            new_task.append({"id":k,"task":i["task"],"status0":i["status0"]})
            k+=1
    save_task(new_task)
    print("your task is deleted")
def main():
    while True:
        print("To DO app")
        print("1: create task")
        print("2: show task")
        print("3: Update the task")
        print("4: Delete the task")
        print("5: exit the to do app")
        ch=int(input("Enter the operation that u want to perform:"))
        if ch==1:
            create()
        elif ch==2:
            show()
        elif ch==3:
            update_task()
        elif ch==4:
            delete_task()
        elif ch==5:
            print("thank u")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()