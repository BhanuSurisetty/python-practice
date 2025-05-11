# Create an empty list
temp_list = []

# Number of elements to add
n = int(input("Enter number of elements: "))

for i in range(n):
    value = input(f"Enter value {i+1}: ")
    temp_list.append(value)

# Convert list to tuple
dynamic_tuple = tuple(temp_list)

print("Dynamic Tuple:", dynamic_tuple)

# Tuple with mixed data types
# Packing
person = ("Alice", 25, "Engineer")
# Unpacking
name, age, job = person
print(name, age, job)  # Alice 25 Engineer
