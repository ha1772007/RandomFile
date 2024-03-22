import os
import random
import string

# Define the directory where the files will be created
output_directory = "random"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate a random string of specified size
def generate_random_string(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

# Define the new target file size (3 MB in bytes)
target_file_size = 3 * 1024 * 1024

# Update the size of each file to the target size
for i in range(1, 101):
    filename = f"{i}.txt"
    filepath = os.path.join(output_directory, filename)
    with open(filepath, "a+") as file:
        current_content = file.read()
        current_size = len(current_content)
        if current_size < target_file_size:
            # Append additional random characters to reach the target size
            additional_content = generate_random_string(target_file_size - current_size)
            file.write(additional_content)
        elif current_size > target_file_size:
            # Truncate the file to the target size
            file.truncate(target_file_size)

print(f"Updated the size of each file to {target_file_size / (1024 * 1024)} MB.")
