import fastavro
import json

def read_avro(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        schema = reader.writer_schema
        records = [record for record in reader]
    return schema, records

def write_avro(file_path, schema, records):
    with open(file_path, 'wb') as f:
        fastavro.writer(f, schema, records)

def find_and_replace_in_json_field(records, field_name, search_text, replace_text):
    for record in records:
        if field_name in record:
            try:
                json_data = json.loads(record[field_name])
                updated_json_data = json.dumps(json_data).replace(search_text, replace_text)
                record[field_name] = json.loads(updated_json_data)
            except json.JSONDecodeError:
                print(f"Field {field_name} in record {record} is not valid JSON.")
    return records

# File paths
input_file_path = 'input.avro'
output_file_path = 'output.avro'

# Field name containing JSON, and the text to find and replace
json_field_name = 'your_json_field_name'
search_text = 'text_to_find'
replace_text = 'text_to_replace'

# Read the Avro file
schema, records = read_avro(input_file_path)

# Perform find and replace in the JSON field
updated_records = find_and_replace_in_json_field(records, json_field_name, search_text, replace_text)

# Write the updated records back to an Avro file
write_avro(output_file_path, schema, updated_records)

print("Find and replace operation completed and written to output.avro")
