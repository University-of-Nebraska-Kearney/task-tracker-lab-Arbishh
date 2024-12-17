# Import library of functions
import file_control

def main():
  # Get tasks from file
  tasks = file_control.load_tasks()

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_tasks(tasks)
    elif choice == "3":
      complete(tasks)
    elif choice == "4":
      file_control.save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")
def display_tasks(tasks):
    
  index = 1  # Initialize task numbering at 1
  for task in tasks:  # Iterate over the list of tasks
    print(f"\nTask {index}:")  # Display task number
    print(f"Title: {task[0]}")  # Display task title
    print(f"Description: {task[1]}")  # Display task description
    print(f"Due Date: {task[2]}")  # Display task due date
    print(f"Status: {task[3]}")  # Display task status
    index += 1  # Increment task numbering

def add_tasks(tasks):
    title = input("Enter task title: ")  # Get task title from user
    description = input("Enter task description: ")  # Get task description from user
    due_date = input("Enter due date (YYYY-MM-DD): ")  # Get due date from user
    task = (title, description, due_date, "Incomplete")  # Create task tuple
    tasks.append(task)  # Add task tuple to the list
    return tasks  # Return updated task list

def complete(tasks):
    if not tasks:  # Check if task list is empty
        print("No tasks available to mark as complete.")  # Inform user of no tasks
        return tasks  # Return task list unchanged
    display_tasks(tasks)  # Display all tasks for selection
    try:
        index = int(input("Enter the task number to mark as complete: ")) - 1  # Get task number, adjust for index
        if 0 <= index < len(tasks):  # Check if task number is valid
            task = tasks[index]  # Get selected task
            tasks[index] = (task[0], task[1], task[2], "Complete")  # Update status to complete
            print(f"Task '{task[0]}' marked as complete.")  # Confirm task completion
        else:
            print("Invalid task number.")  # Inform user of invalid selection
    except ValueError:  # Catch non-numeric input errors
        print("Please enter a valid number.")  # Inform user of input error
    return tasks  # Return updated task list


 
     
  
  













if __name__ == "__main__":
  main()
