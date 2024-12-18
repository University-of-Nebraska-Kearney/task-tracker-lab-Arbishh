FILE_NAME = "tasks.txt"  # Define the filename for task storage

def load_tasks():
    # Loads tasks from a file and returns them as a list of tuples.
    tasks = []  # Initialize an empty task list for storing
   
    with open(FILE_NAME, "r") as file:  # Open the file in read mode
        for line in file:  # read through each line in file
                line = line.strip()  # Remove trailing whitespace/newlines
                if line:  # Skip empty lines(if any)
                    title, description, due_date, status = line.split("|")  # Split task attributes(ie. title) using |
                    tasks.append((title, description, due_date, status))  # Append task tuple to list
        print("Tasks loaded successfully.")  # Confirm successful loading
    
    
    return tasks  # Return the loaded task list

def save_tasks(tasks):
    # Saves the list of tasks to a file.
    
     with open(FILE_NAME, "w") as file:  # Open the file in write mode
        for task in tasks:  # Iterate through the list of tasks
                line = "|".join(task)  # Convert task tuple into string for stroing in file
                file.write(line + "\n")  # Write the task string to file

    