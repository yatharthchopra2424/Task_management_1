tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(task_index):
    try:
        index = int(task_index) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a task number to remove.")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter a new task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        task_index = input("Enter the task number to remove: ")
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-4).")
