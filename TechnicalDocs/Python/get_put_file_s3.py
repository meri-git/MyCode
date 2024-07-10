import boto3
import json
import re
import os
from fastavro import reader, writer, parse_schema
from io import BytesIO

s3 = boto3.client('s3')

def list_s3_files(bucket_name, prefix=''):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    files = []
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['Key'].endswith('.json') or obj['Key'].endswith('.avro'):
                files.append(obj['Key'])
    return files

def download_s3_file(bucket_name, s3_key, local_path):
    s3.download_file(bucket_name, s3_key, local_path)

def upload_s3_file(bucket_name, s3_key, local_path):
    s3.upload_file(local_path, bucket_name, s3_key)

def find_replace_in_json(file_path, find_text, replace_text):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    data_str = json.dumps(data)
    data_str = re.sub(find_text, replace_text, data_str)
    
    with open(file_path, 'w') as f:
        json.dump(json.loads(data_str), f, indent=4)

def find_replace_in_avro(file_path, find_text, replace_text):
    with open(file_path, 'rb') as f:
        avro_reader = reader(f)
        schema = avro_reader.writer_schema
        records = [record for record in avro_reader]
    
    modified_records = []
    for record in records:
        record_str = json.dumps(record)
        record_str = re.sub(find_text, replace_text, record_str)
        modified_records.append(json.loads(record_str))
    
    with open(file_path, 'wb') as f:
        avro_writer = writer(f, parse_schema(schema), modified_records)

def process_files(bucket_name, download_path, find_text, replace_text, upload_folder):
    files = list_s3_files(bucket_name)
    
    for s3_key in files:
        local_path = os.path.join(download_path, os.path.basename(s3_key))
        download_s3_file(bucket_name, s3_key, local_path)
        
        if local_path.endswith('.json'):
            find_replace_in_json(local_path, find_text, replace_text)
        elif local_path.endswith('.avro'):
            find_replace_in_avro(local_path, find_text, replace_text)
        
        upload_s3_key = os.path.join(upload_folder, os.path.basename(s3_key))
        upload_s3_file(bucket_name, upload_s3_key, local_path)
        os.remove(local_path)

if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    download_path = '/path/to/download'
    find_text = 'text_to_find'
    replace_text = 'text_to_replace'
    upload_folder = 'processed-files'
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    process_files(bucket_name, download_path, find_text, replace_text, upload_folder)
