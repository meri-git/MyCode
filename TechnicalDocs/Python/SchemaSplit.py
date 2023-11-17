import re
import os

def split_ddl(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Split by 'Create or replace schema'
    schema_blocks = re.split(r'(?=Create or replace schema)', content)

    for block in schema_blocks:
        schema_name_match = re.search(r'Create or replace schema\s+(\w+)', block, re.IGNORECASE)
        if schema_name_match:
            schema_name = schema_name_match.group(1)

            # Create a directory for each schema if it doesn't exist
            if not os.path.exists(schema_name):
                os.makedirs(schema_name)

            # Write schema DDL to a file
            schema_file_path = os.path.join(schema_name, f"{schema_name}_schema.ddl")
            with open(schema_file_path, 'w') as schema_file:
                schema_file.write(block)

            # Split tables and views DDLs
            table_view_blocks = re.split(r'(?=Create table|Create view)', block, flags=re.IGNORECASE)
            for table_view_block in table_view_blocks:
                table_view_name_match = re.search(r'Create (table|view)\s+(\w+)', table_view_block, re.IGNORECASE)
                if table_view_name_match:
                    obj_type = table_view_name_match.group(1)
                    obj_name = table_view_name_match.group(2)

                    # Write table/view DDL to a file in the respective schema directory
                    obj_file_path = os.path.join(schema_name, f"{obj_name}_{obj_type}.ddl")
                    with open(obj_file_path, 'w') as obj_file:
                        obj_file.write(table_view_block)

# Replace 'input_file' with the path to your large DDL file
split_ddl('input_file.sql')
