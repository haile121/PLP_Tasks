# File Read & Write Challenge with Error Handling

# Ask the user for the input filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file for reading
    with open(filename, "r") as file:
        content = file.read()
    
    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content has been written to '{new_filename}'")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Cannot read the file '{filename}'.")
