#file handling

#create a file
#with defined path
import os
directory = "C:/Users/venkata pavan kumar/Documents/PythonPractice/Day3"
filename = "filehandling1.txt"

# Create the directory if it doesn't exist
os.makedirs(directory, exist_ok=True)
filepath = os.path.join(directory, filename)

# 1. "x" – Exclusive creation:  
try:
    with open(filepath,"x") as file:
        file.write("this is a new text file\n")
except FileExistsError:
    print("File ALreadyExists")

#2."w" – Write mode: creates the file if it doesn’t exist, overwrites if it does.
with open(filepath,"w")as file:
    file.write("This write command will overrite the existing text\n")

#3 "a" – Append mode: creates the file if it doesn’t exist, appends to the end of the file if it does.	
with open(filepath,"a")as file:
    file.write("This will append the existing data in the file\n")
   
# 4. "r" - read mode: opens the file for reading. If the file does not exist, it raises a FileNotFoundError.
with open(filepath,"r")as file:
    content = file.read()
    print(content)
    
# 5. "r+" - read and write mode: opens the file for both reading and writing. The file pointer is placed at the beginning of the file.
with open(filepath,"r+")as file:
    content = file.read()
    file.write("This is a Read Write command\n") 
    print(content)


