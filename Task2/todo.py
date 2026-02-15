
tasks = []

def show_menu():
    print("--- Main Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete a Task")
    print("5. Exit Program")

#Function to Add a New Task
def add_task():
    task = input("Enter a New Task: ")
    tasks.append({"Task": task, "Status": "Pending"})
    print(f"Task '{task}' Added Successfully!\n")

#Function to View All Tasks
def view_tasks():
    if not tasks:
        print("No task added!")
        return 
    print("Your To-do List")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task['Task']} - {task['Status']}")
    print("\n")
   
#Function to Mark Task as Done
def mark_done():
    view_tasks()
    if not tasks:
        print("The List is Empty!")
        return
    try: 
        index = int(input("Enter the Task Number You Completed:")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['Status'] = 'done'
        else:
            print("Invalid Task Number!\n")
    except ValueError:
        print ("Please Enter a Valid Number.")


#Function to Delete a Task
def delete_task():
    view_tasks()
    if not tasks:
        print("List is Empty!")
        return 
    try:
        index = int(input("Enter a Task Number to Delete: ")) -1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Deleted task: {removed_task['Task']}")
        else:
            print("Invalid Task Number!")
    except ValueError:
        print ("Please Enter a Valid Task Number.")


#Program Control Loop
while True:
    show_menu()    
    print("\n")
    choice = input("Choose an Option (1-5):")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
        ##exit()
    else:
        print("Invalid choice, Try again (Use 1-5)")