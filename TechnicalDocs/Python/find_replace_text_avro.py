import fastavro
import re

def read_avro_file(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        records = [record for record in reader]
    return records, reader.schema

def write_avro_file(file_path, records, schema):
    with open(file_path, 'wb') as f:
        writer = fastavro.writer(f, schema, records)

def find_and_replace_s3_path(records, field_name, find_text, replace_text):
    s3_regex = r's3://[^/]+/[^ ]+'
    
    for record in records:
        if field_name in record and isinstance(record[field_name], str):
            # Find all S3 paths in the field
            s3_paths = re.findall(s3_regex, record[field_name])
            
            # Replace specified S3 paths
            for path in s3_paths:
                if find_text in path:
                    new_path = path.replace(find_text, replace_text)
                    record[field_name] = record[field_name].replace(path, new_path)
                    
    return records

# Example usage
input_avro_file = 'input.avro'
output_avro_file = 'output.avro'
field_name = 's3_field'
text_to_find = 's3://old-bucket/'
text_to_replace = 's3://new-bucket/'

# Read the Avro file
records, schema = read_avro_file(input_avro_file)

# Find and replace S3 paths in the specified field
modified_records = find_and_replace_s3_path(records, field_name, text_to_find, text_to_replace)

# Write the modified records back to an Avro file
write_avro_file(output_avro_file, modified_records, schema)
