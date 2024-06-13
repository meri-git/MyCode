import fastavro
import json

def read_avro_file(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        records = [record for record in reader]
    return records, reader.schema

def write_avro_file(file_path, records, schema):
    with open(file_path, 'wb') as f:
        writer = fastavro.writer(f, schema, records)
        
def find_and_replace_in_json_field(records, field_name, find_text, replace_text):
    for record in records:
        if field_name in record:
            try:
                # Parse the JSON field
                json_data = json.loads(record[field_name])
                # Replace text in JSON data
                modified_json_data = json.dumps(json_data).replace(find_text, replace_text)
                # Convert back to JSON string and update the record
                record[field_name] = json.dumps(json.loads(modified_json_data))
            except json.JSONDecodeError:
                print(f"Field {field_name} does not contain valid JSON data")
    return records

# Example usage
input_avro_file = 'input.avro'
output_avro_file = 'output.avro'
json_field_name = 'json_field'
text_to_find = 'old_text'
text_to_replace = 'new_text'

# Read the Avro file
records, schema = read_avro_file(input_avro_file)

# Find and replace text in the specified JSON field
modified_records = find_and_replace_in_json_field(records, json_field_name, text_to_find, text_to_replace)

# Write the modified records back to an Avro file
write_avro_file(output_avro_file, modified_records, schema)
