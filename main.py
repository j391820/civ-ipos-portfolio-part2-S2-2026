from src.task_manager import add_task, delete_task, list_tasks
from src.file_handler import load_tasks


def handle_add_task(tasks):
    """
    Ask user for details of new task then add new task to list.

    Args:
        tasks (list): The list of existing Task objects.

    Returns:
        None.

    Side Effects:
        - Add a new task to list.
    """
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date (DD-MM-YYYY): ")
    add_task(tasks, title, description, due_date)


def handle_delete_task(tasks):
    """
    Check if any tasks currently exist
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.

    Returns:
        None.

    Side Effects:
        - Prints
            - Task deleted successfully.
            - Task not found.
            - No tasks added yet.
    """
    if len(tasks):
        list_tasks(tasks)
        title = input("Title of the task to delete: ")
        if delete_task(tasks, title):
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    else:
        print("No tasks added yet.")


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
            handle_add_task(tasks)
        elif choice == "2":
            handle_delete_task(tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
