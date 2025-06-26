"""
This module provides a simple command-line to-do list application.

Functions:
    add_task(): Add new tasks to the to-do list.
    view_task(): View tasks from the to-do list.
    edit_task(): Delete a task from the to-do list by its ID.

The tasks are stored in the global dictionary 'todos', where each key is a task ID and the value is a list containing the task description, notes, and status.
"""
# At the top
import json
import os

DATA_FILE = "data.json"

def load_todos():
    """
    Load the to-do list from the data.json file.
    Returns an empty dictionary if the file does not exist or is empty.
    """
    if os.path.exists(DATA_FILE):
        if os.path.getsize(DATA_FILE) == 0:
            return {}
        with open(DATA_FILE, "r") as f:
            return {int(k): v for k, v in json.load(f).items()}
    return {}

def save_todos():
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f)

# Load at start
todos = load_todos()


def add_task():
    """
    Add new tasks to the to-do list. Prompts the user for the number of tasks, task description, and notes.
    Each task is assigned a unique ID and stored in the global 'todos' dictionary.
    """
    try:
        total_task = int(input("How many tasks you want to create: "))
        start_id = max(todos)+1 if todos else 1
        for i in range(start_id, start_id+total_task):
            id = i
            task = input("Enter Your Task: ")
            notes = input('Enter Your Notes: ')
            status = False
            todos[id] = [task, notes, status]
            print("Your Task created successfully!!")
        save_todos()
    except (TypeError, ValueError):
        print("Please Enter correct Input: ")
def view_task():
    """
    View tasks from the to-do list. Prompts the user to view all tasks or a specific number of tasks.
    Displays the task ID, description, notes, and status.
    """
    try:
        usr_choice = input("How many tasks you want to view, Enter A to select all: ").lower()
        if usr_choice == 'a':
            for key, value in todos.items():
                print(f"id : {key}\tTask: {value[0]}\tNotes: {value[1]}\tstatus: {value[2]}")
        else:
            num = int(usr_choice)
            shown = 0
            for key in sorted(todos):
                if shown >= num:
                    print("No Task")
                value = todos[key]
                print(f"id: {key}\tTask: {value[0]}\tNotes: {value[1]}\tStatus: {value[2]}")
                shown += 1
    except (TypeError, ValueError):
        print("Please enter a correct input.")
def edit_task():
    """
    Edit or delete a task from the to-do list by its ID.
    Displays all tasks and prompts the user for the action to perform:
        0 - Delete the task
        1 - Edit the task's description and notes
        2 - Mark the task as completed or incomplete
    Saves changes to the data file after any modification.
    """
    # Display all tasks for user reference
    for key, value in todos.items():
        print(f"id : {key}\tTask: {value[0]}\tNotes: {value[1]}\tstatus: {value[2]}")
    try:
        # Prompt user for action
        edit_choice = int(input("Enter 0 to Delete task\nEnter 1 to Edit task\tEnter 2 to mark task as completed "))
        # Prompt user for task ID
        edit_id = int(input("Enter id of task you want to edit: "))
        if edit_choice == 0:
            # Delete the selected task
            del todos[edit_id]
            print("Task Deleted Successfully!! ")
        elif edit_choice == 1:
            # Edit task description and notes
            todos[edit_id][0] = input("Enter Your Task: ")
            todos[edit_id][1] = input("Enter Your Notes: ")
            print("Your Task has been updated!!")
        elif edit_choice == 2:
            # Mark task as completed or incomplete
            updt_choice = int(input("Enter 0 for Incomplete 1 for Completed"))
            if updt_choice == 0:
                todos[edit_id][2] = False
            elif updt_choice == 1:
                todos[edit_id][2] = True
                print("Your task is completed!!")
            else:
                print("please enter correct input!!")
            print("Your Action has been completed")
        # Save changes to file
        save_todos()
    except (TypeError, ValueError, KeyError):
        print("Wrong input, Please Enter a Valid Task Id")

if __name__=="__main__":
    choice = int(input("Enter 1 to Add task 2 to edit task and 3 for view task and enter 0 to exit: "))
    while choice!=0:
        if choice==1:
            add_task()
        elif choice==2:
            edit_task()
        elif choice==3:
            view_task()
        else:
            print("Please enter correct input")
        choice = int(input("Enter 1 to Add task 2 to edit task and 3 for view task and enter 0 to exit: "))


