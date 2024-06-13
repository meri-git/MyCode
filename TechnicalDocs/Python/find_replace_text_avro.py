import fastavro

def read_avro_file(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        records = [record for record in reader]
    return records, reader.schema

def write_avro_file(file_path, records, schema):
    with open(file_path, 'wb') as f:
        writer = fastavro.writer(f, schema, records)

def replace_field_value(records, field_name, new_value):
    for record in records:
        if field_name in record:
            record[field_name] = new_value
    return records

# Example usage
input_avro_file = 'input.avro'
output_avro_file = 'output.avro'
field_name_to_replace = 'field_to_replace'
new_field_value = 'new_value'

# Read the Avro file
records, schema = read_avro_file(input_avro_file)

# Replace the field value in the specified field
modified_records = replace_field_value(records, field_name_to_replace, new_field_value)

# Write the modified records back to an Avro file
write_avro_file(output_avro_file, modified_records, schema)
