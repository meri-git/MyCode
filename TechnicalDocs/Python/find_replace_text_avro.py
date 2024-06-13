import fastavro

def read_avro_file(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        records = [record for record in reader]
    return records, reader.schema

def write_avro_file(file_path, records, schema):
    with open(file_path, 'wb') as f:
        fastavro.writer(f, schema, records)

def replace_field(records, field_name, new_value):
    for record in records:
        if field_name in record:
            record[field_name] = new_value
    return records

# Example usage
input_avro_file = 'input.avro'
output_avro_file = 'output.avro'
field_to_replace = 'field_name'
new_value_for_field = 'new_value'

# Read the Avro file
records, schema = read_avro_file(input_avro_file)

# Replace the specified field in each record
modified_records = replace_field(records, field_to_replace, new_value_for_field)

# Write the modified records back to a new Avro file
write_avro_file(output_avro_file, modified_records, schema)
