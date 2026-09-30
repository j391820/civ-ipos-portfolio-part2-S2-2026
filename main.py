from src.task_manager import add_task, delete_task, list_tasks, filter_tasks_by_status
from src.file_handler import load_tasks


def handle_filter_task(tasks, choice):
    """
    Filter task list display depending on users input.

    Args:
        tasks (list): The list of existing Task objects.
        choice (string): Users choice as a number string.
    Returns:
        None.
    Side Effects:
        - Print all or status filtered list of tasks.
    """
    if choice == "1":
        list_tasks(tasks)
    elif choice == "2":
        filtered_tasks = filter_tasks_by_status(tasks, "pending")
        list_tasks(filtered_tasks)
    elif choice == "3":
        filtered_tasks = filter_tasks_by_status(tasks, "completed")
        list_tasks(filtered_tasks)
    else:
        print("Invalid choice. Try again.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("Please choose a filter: ")
            print("1. All")
            print("2. Pending")
            print("3. Completed")
            choice = input("Enter your choice: ")
            handle_filter_task(tasks, choice)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
