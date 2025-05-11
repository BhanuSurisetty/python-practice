# Create an empty list
dynamic_list = []

# Number of elements to add to the list
num_elements = int(input("Enter the number of elements you want to add: "))

# Add elements to the list based on user input
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    dynamic_list.append(element)

print("Dynamic list:", dynamic_list)


#Append elements to the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

#remove elements from the list
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
#insert elements at a specific index
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]
#pop elements from the list
my_list = [1, 2, 3]
my_list.pop()
print(my_list)  # Output: [1, 2]
#pop elements from a specific index
my_list = [1, 2, 3]
my_list.pop(1)

print(my_list)  # Output: [1, 3]
#clear all elements from the list
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []



