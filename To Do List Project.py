tasks = []

def add_task(tasks):
    task_description = input("Enter what task you'd like to add")
    tasks.append({"task": task_description, "completed": False})
    print(f"task '{task_description}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"{i}. {task['task']} - {status}")

def mark_task(tasks):
    try:    
        view_tasks(tasks)
        if tasks:
            task_number = int(input("Enter the number of which task you'd like to mark complete"))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['completed'] = True
                print(f"Task '{tasks[task_number - 1]['task']}' marked completed.")
            else:
                print("Invalid task selection")
    except ValueError:
        print("Please enter a valid number")

def delete_task(tasks):
    try:
        view_tasks(tasks)
        if tasks:
            task_number = int(input("Enter the number of the task you'd like to delete:"))
            if 1 <= task_number <= len(tasks):
                task = tasks.pop(task_number - 1)
                print(f"Task '{task['task']}' deleted.")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    menu = input("Menu: \n 1. Add a Task \n 2. View tasks \n 3. Mark a Task as complete \n 4. Delete a task \n 5. Quit \n")
    if menu == "1":
        add_task(tasks)
    elif menu == "2":
        view_tasks(tasks)
    elif menu == "3":
        mark_task(tasks)
    elif menu == "4":
        delete_task(tasks)
    elif menu == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid selection, try again!")
