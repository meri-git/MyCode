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

def find_and_replace_json_value(records, field_name, json_key, new_value):
    for record in records:
        if field_name in record:
            try:
                # Parse the JSON field
                json_data = json.loads(record[field_name])
                
                # Check if the JSON key exists and replace its value
                if json_key in json_data:
                    json_data[json_key] = new_value
                    
                # Convert back to JSON string and update the record
                record[field_name] = json.dumps(json_data)
            except json.JSONDecodeError:
                print(f"Field {field_name} does not contain valid JSON data")
    return records

# Example usage
input_avro_file = 'input.avro'
output_avro_file = 'output.avro'
json_field_name = 'json_field'
json_key_to_find = 'key_to_replace'
new_value_for_key = 'new_value'

# Read the Avro file
records, schema = read_avro_file(input_avro_file)

# Find the JSON key and replace its value in the specified JSON field
modified_records = find_and_replace_json_value(records, json_field_name, json_key_to_find, new_value_for_key)

# Write the modified records back to an Avro file
write_avro_file(output_avro_file, modified_records, schema)
