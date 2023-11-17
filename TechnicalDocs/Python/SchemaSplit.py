def split_file(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Splitting the content based on the pipe delimiter
    parts = content.split('|')

    # Output multiple files
    output_files = []
    for idx, part in enumerate(parts):
        output_file_path = f"output_{idx + 1}.txt"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(part)
        output_files.append(output_file_path)

    return output_files

# Replace 'input_file_path' with the path to your huge file
input_file_path = 'path/to/your/huge_file.txt'
result_files = split_file(input_file_path)

print(f"Split the file into {len(result_files)} parts:")
for file_path in result_files:
    print(file_path)
