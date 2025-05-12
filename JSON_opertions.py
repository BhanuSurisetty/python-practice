#JSON Operations in Python
import json
data = {
    "name": "Bhanu",
    "age": 25,
    "city": "India",
    "skills": ["Python", "Git"]
 }
# 1. JSON Encoding: Converting a Python object into a JSON string.
Json_strng = json.dumps(data)
print(Json_strng)
# 2. JSON Decoding: Converting a JSON string back into a Python object.
Json_obj = json.loads(Json_strng)
print(Json_obj)
# 3. Writing JSON to a file: Saving a Python object as a JSON file.
with open("data.json", "w") as json_file:
    json.dump(data, json_file)
# 4. Reading JSON from a file: Loading a JSON file into a Python object.
with open("data.json", "r") as json_file:
    data_from_file = json.load(json_file)
print(data_from_file)
# 5. Pretty Printing JSON: Making JSON data more readable.