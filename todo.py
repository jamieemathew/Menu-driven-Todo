# Simple To-Do App in Python

# Function to display the to-do list
def display_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

# Function to add a task to the to-do list
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added to the to-do list.\n")

# Function to remove a task from the to-do list
def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.\n")
    else:
        print("Invalid task index. Please enter a valid index.\n")

# Main function to run the to-do app
def main():
    tasks = []

    while True:
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            print("Quitting the to-do app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
