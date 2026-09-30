from src.task import Task
from src.file_handler import save_tasks
from datetime import datetime
from rich import box
from rich.console import Console
from rich.table import Table


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Raises:
        ValueError: If the due date is not in the correct format.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    # Prevent duplicate tasks
    if any(task.title == title for task in tasks):
        print("Error: A task with this title already exists.")
        return False

    # Validate due date format
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return False

    tasks.append(Task(title, description, due_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def list_tasks(tasks, status=None):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks
        by (e.g., "pending" or "completed").

    Returns:
        None

    Side Effects:
        - Prints the list of tasks to the console.
    """
    if not status:
        # If status is not set
        filtered = tasks
    else:
        # Filter tasks based on their status
        filtered = []
        for task in tasks:
            if task.status == status:
                filtered.append(task)

    if not filtered:
        print("No tasks found.")
        return
    # Create new table with four columns with headers.
    table = Table(
        show_header=True,
        box=box.SQUARE_DOUBLE_HEAD,
        header_style="bold magenta",
        show_lines=True
        )
    table.add_column("Due Date", style="dim", width=12)
    table.add_column("Title", justify="center")
    table.add_column("Description", justify="center")
    table.add_column("Status", justify="right")
    console = Console()
    # Loop through tasks and add each as new row
    for task in filtered:
        table.add_row(
            task.due_date,
            task.title,
            task.description,
            task.status
            )
    console.print(table)


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]
