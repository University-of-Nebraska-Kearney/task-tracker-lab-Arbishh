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



# Create a function called display_tasks that takes a list of taks and
# displays every task in the list.
def display_tasks(tasks):
 #display tasks on list with intervals
 print(tasks)
 return tasks
def add_tasks():
  #ask the user for new tasks
  new_tasks =[]
  Title = input("What task would you like to add?")
  Description = input("Add description of your tasks:")
  Date = input("Add the to-do date")
  #put all into another list
  new_tasks = [Title,Description,Date]

  #add new task to the list via appending
  test.append("new_tasks")
  tasks.append(new_tasks)

  #return the update list
  return tasks

#function for complete task
def complete(tasks):
  #display the 0 index  of each index in tasks
  for title in tasks:
    print(title[0])
  #prompt user to choose task
  utask = input("Which task would you like to mark as complete?")
  if not utask.isdigit():
    utask = input("Please choose a numbered task ")
  if utask.isdigit():
    index = int(utask) - 1
    for i in range(tasks.len()):
     #change the status to complete
     tasks[index][3] = "complete"
     break
  

 
  


 
     
  
  











# Create a function called complete that takes a lists of tasks,
# displays them to the user, and then lets the user choose one
# to mark as complete. It will then update the status of the 
# task in the list and return the updated list.



if __name__ == "__main__":
  main()
