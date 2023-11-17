import re

def split_ddl_file(input_file_path):
    # Read the input DDL file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        ddl_content = file.read()

    # Split DDL content based on "create or replace schema" statements
    ddl_parts = re.split(r'(?=create\s+or\s+replace\s+schema)', ddl_content, flags=re.IGNORECASE)

    # Output multiple DDL files
    output_files = []
    for idx, part in enumerate(ddl_parts):
        if part.strip():
            output_file_path = f"output_{idx + 1}.sql"
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(part.strip())
            output_files.append(output_file_path)

    return output_files

# Replace 'input_file_path' with the path to your huge DDL file
input_file_path = 'path/to/your/huge_ddl_file.sql'
result_files = split_ddl_file(input_file_path)

print(f"Split the DDL file into {len(result_files)} parts:")
for file_path in result_files:
    print(file_path)
