"""
✅ PRACTICE TASKS
1.Create a file called info.txt, write a sentence and read it back.

2.Create a Python dictionary and save it as a JSON file.

3.Read the JSON file and print only one key-value pair.

4.Append multiple lines to a text file and read them line by line.

"""
# 1. Create a file called info.txt, write a sentence and read it back.
import os
path ="c:/Users/venkata pavan kumar/Documents/PythonPractice/Day3/"
filename = "info.txt"
filepath = os.path.join(path,filename)

with open(filepath,"w") as file:
    file.write("This is a newly created fie \n")
    with open(filepath,"r")as file:
        content = file.read()
        print(content)
# 2. Create a Python dictionary and save it as a JSON file.
import json
filename = "data.json"
filepath_JSON = os.path.join(path,filename)
data= {
    "name":"Bhanu",
    "age":25,
    "city":"India"
}
with open(filepath_JSON,"w")as file:
    json.dump(data,file)
# 3. Read the JSON file and print only one key-value pair.
with open(filepath_JSON,"r")as file:
    content = json.load(file)
    print(content["age"])
# 4. Append multiple lines to a text file and read them line by line.

with open(filepath,"a")as file:
    file.write("This is a 1st Line\n")
    file.write("This is a 2nd line \n")
    file.write("this is a 3 rd line \n")
with open(filepath,"r")as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())