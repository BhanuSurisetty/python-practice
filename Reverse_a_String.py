#reverse a 'String
def reverse_string(string):
    # Check if the input is a string
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    # Reverse the string using slicing
    reversed_string = string[::-1]
    return reversed_string

# Example usage
if __name__ == "__main__":
    input_string = "Hello, World!"
    reversed_str = reverse_string(input_string)
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_str}")