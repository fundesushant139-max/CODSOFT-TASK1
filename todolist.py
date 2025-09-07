tasks = []
def add_task():
    task = input("Enter a task to add:")
    tasks.append(task)
    print("Task added")

def view_tasks():
     print("your To-Do List:\n")
     for index, task in enumerate(tasks,start = 1):
        print(f"{index}.{task}")

     if not tasks:
            print("No Tasks") 

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: "))-1  
     
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("task deleted")
        else:
            print("invalid task number.")
    except ValueError:    

         print("please enter a valid number.")  
         
while True:
    print("\n menu:")
    print("1- Add Task")
    print("2- View Tasks")
    print("3- Delete Task")
    print("4- Exit")
    choice = input("Enter your choice(1-4):")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks() 
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Good bye!!")
        break
    else:
        print("Invalid choice.Please enter a number from 1-4.")



