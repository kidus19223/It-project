tasks=[]
def DPT():
    if len(tasks)== 0:
        print("No current task.")
        return
    
    print("Current task:")
    for index, task in enumerate(tasks):
        if task["completed"]:
            stat = "Done."
        else:
            stat = "Not Done."
        print(f"• {task['title']} is {stat}.")

def add():
    nt= input("add a new task: ")
    tasks.append({"title": nt, "completed": False})
    print("Task added!")

def rem():
        rem= int(input("enter task number to remove (First task index is 0): "))
        tasks.pop(rem)
        print("Task removed.") 

def edit():
    edit= int(input("enter task number to edit(First task index is 0): "))
    newtt = input("enter new task title: ")
    tasks[edit]["title"] = newtt
    print("Task updated.")    

def mark():
    index= int(input("enter task number to mark completed(First task index is 0): "))
    tasks[index]["completed"] = True
    print("Task marked completed.")
    
def exit():
    print("Goodbye!")

def menu():
    print("1) display tasks")
    print("2) add new task")
    print("3) remove task")
    print("4) edit task")
    print("5) mark task as completed")
    print("6) exit application")

def hc(choice):
    if choice == "1":
        DPT()
    elif choice == "2":
        add()
    elif choice == "3":
        rem()
    elif choice == "4":
        edit()
    elif choice == "5":
        mark()
    elif choice == "6":
        exit()

def man():
    DPT()
    while True:
        menu()
        choice= input("Choose an option: ")
        hc(choice)

man()
