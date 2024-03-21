import os

# Define the output directory
output_directory = "download"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Generate 100 files with specified content
for i in range(1, 101):
    # Create the file path
    file_path = os.path.join(output_directory, f"{i}.txt")

    # Generate content (1MB per file)
    content = str(i) * (1024 * 1024)

    # Write the content to the file
    with open(file_path, "w") as file:
        file.write(content)

    print(f"Generated file {file_path}")

print("All 100 files have been generated successfully.")
