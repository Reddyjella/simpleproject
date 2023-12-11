# todo_list.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully.")
        else:
            print(f"Task '{task}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. List Tasks\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
