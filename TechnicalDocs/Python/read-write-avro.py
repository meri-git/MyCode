import fastavro
import io

def read_avro_file(file_path):
    with open(file_path, 'rb') as f:
        reader = fastavro.reader(f)
        records = [record for record in reader]
    return records, reader.writer_schema

def write_avro_file(file_path, records, schema):
    with open(file_path, 'wb') as f:
        fastavro.writer(f, schema, records)

def find_and_replace(records, field, find_text, replace_text):
    for record in records:
        if field in record and isinstance(record[field], str):
            record[field] = record[field].replace(find_text, replace_text)
    return records

def main():
    input_file = 'input.avro'   # Path to your input Avro file
    output_file = 'output.avro' # Path to your output Avro file
    field_to_modify = 'your_field'  # The field in the Avro record where you want to perform find-and-replace
    text_to_find = 'find_this'      # The text you want to find
    text_to_replace = 'replace_with_this' # The text you want to replace with

    # Read the Avro file
    records, schema = read_avro_file(input_file)

    # Perform find and replace
    updated_records = find_and_replace(records, field_to_modify, text_to_find, text_to_replace)

    # Write the updated records to a new Avro file
    write_avro_file(output_file, updated_records, schema)

if __name__ == '__main__':
    main()
