#dictionary in python
employee = {
    "id": 101,
    "name": "Bob",
    "skills": ["Python", "SQL"],
    "experience": 2
}

#acessing the value using key
print(employee.get("name"))

#adding a new key-value pair
employee["age"] = 30
print(employee)
#updating the value of an existing key
employee["experience"] = 5
print(employee)
#deleting a key-value pair
del employee["skills"]
print(employee)
#checking if a key exists
if "name" in employee:
    print("Key exists")
else:
    print("Key does not exist")
#dict.keys()	Returns all keys
print(employee.keys())
#dict.values()	Returns all values
print(employee.values())
#dict.items()	Returns all key-value pairs
print(employee.items())
#dict.update()	Updates with another dictionary
employee.update({"department": "IT"})
print(employee)

#dict.pop(key)	Removes the key and returns its value
print(employee.pop("age"))
#dict.clear()	Removes all items 
employee.clear()
print(employee)
