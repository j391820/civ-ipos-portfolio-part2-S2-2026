from src.task_manager import add_task, delete_task, list_tasks, filter_tasks_by_status
from src.task_manager import complete_task
from src.file_handler import load_tasks
from loguru import logger


logger.remove()
logger.add("logs/app.log", retention="30 days")


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


def handle_complete_task(tasks):
    """
    Updates task status from pending to completed.

    Args:
        tasks (list): The list of existing Task objects.

    Returns:
        None.
    """
    filtered_tasks = filter_tasks_by_status(tasks, "pending")
    list_tasks(filtered_tasks)
    title = input("Title of the task to complete: ")
    complete_task(tasks, title)


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
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            handle_add_task(tasks)
        elif choice == "2":
            handle_delete_task(tasks)
        elif choice == "3":
            handle_complete_task(tasks)
        elif choice == "4":
            print("Please choose a filter: ")
            print("1. All")
            print("2. Pending")
            print("3. Completed")
            choice = input("Enter your choice: ")
            handle_filter_task(tasks, choice) 
        elif choice == "5":
            print("Exiting Task Manager.")
            logger.info("User closed app.")
            break
        else:
            print("Invalid choice. Try again.")
            logger.warning("User selected invalid menu option.")


if __name__ == "__main__":
    main()
