# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.
def load_tasks():
 #open the file in read mode
 file = open('tasks.txt','r')
 # creatinf a list to hold records
 task = []
 #read first line
 line = file.readline()
 #loop for task if list is not empty
 while line !='':
     #secondary list for holding the temporary field
     new_task =[]
     #codes for adding and stripping new lines 1-4:
     new_task.append(line.rstrip('\n'))
     new_task.append(file.readline().rstrip("\n"))
     new_task.append(file.readline().rstrip("\n"))
     new_task.append(file.readline().rstrip("\n"))
     task.append(new_task)#appending the fields 1-4 to task list
     #restarting the loop
     line = file.readline()
 file.close()




# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.
def save_tasks(tasks):
 #open file to append
 with open('task.txt','a') as finaletask:
 
      finaletask.write(tasks)
      tasks.append(line.rstrip('\n'))
      tasks(file.readline().rstrip('\n'))
      tasks.append(file.readline().rstrip('\n'))
      tasks.append(file.readline().rstrip('\n'))
      tasks.append(new_task)
      line = file.readline()