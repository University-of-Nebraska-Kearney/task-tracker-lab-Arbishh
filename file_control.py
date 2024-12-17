FILE_NAME = "tasks.txt"  # Define the filename for task storage

def load_tasks():
    # Loads tasks from a file and returns them as a list of tuples.
    tasks = []  # Initialize an empty task list 
    try:
        with open(FILE_NAME, "r") as file:  # Open the file in read mode
            for line in file:  # Iterate through each line in file
                line = line.strip()  # Remove trailing whitespace/newlines
                if line:  # Skip empty lines
                    title, description, due_date, status = line.split("|")  # Split task attributes
                    tasks.append((title, description, due_date, status))  # Append task tuple to list
        print("Tasks loaded successfully.")  # Confirm successful loading
    except FileNotFoundError:  # Handle file not found error
        print("No saved tasks found. Starting with an empty list.")  # Notify user
    
    return tasks  # Return the loaded task list

def save_tasks(tasks):
    # Saves the list of tasks to a file.
    
     with open(FILE_NAME, "w") as file:  # Open the file in write mode
        for task in tasks:  # Iterate through the list of tasks
                line = "|".join(task)  # Convert task tuple to pipe-separated string
                file.write(line + "\n")  # Write the task string to file
     print("Tasks saved successfully.")  # Confirm successful saving
    