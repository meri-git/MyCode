import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize a session using Amazon S3
s3_client = boto3.client('s3')

def list_deleted_files(bucket_name, prefix=None):
    """List deleted files (delete markers) in an S3 bucket."""
    try:
        # Initialize the list to store deleted file keys
        deleted_files = []

        # Set the arguments for pagination
        paginator = s3_client.get_paginator('list_object_versions')
        if prefix:
            page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        else:
            page_iterator = paginator.paginate(Bucket=bucket_name)

        # Iterate through each page of results
        for page in page_iterator:
            if 'DeleteMarkers' in page:
                for marker in page['DeleteMarkers']:
                    if marker['IsLatest']:
                        deleted_files.append({
                            'Key': marker['Key'],
                            'VersionId': marker['VersionId'],
                            'LastModified': marker['LastModified']
                        })

        return deleted_files
    except NoCredentialsError:
        print("Credentials not available")
        return []
    except ClientError as e:
        print(f"Error: {e}")
        return []

def restore_deleted_file(bucket_name, file_key, version_id):
    """Restore a specific deleted file by version ID."""
    try:
        # Copy the deleted version (with the specific version_id) to restore it
        copy_source = {'Bucket': bucket_name, 'Key': file_key, 'VersionId': version_id}
        s3_client.copy_object(
            Bucket=bucket_name,
            CopySource=copy_source,
            Key=file_key
        )
        print(f"Restored: {file_key}")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Error: {e}")

def main():
    # Replace with your bucket name
    bucket_name = 'your-bucket-name'
    
    # Prefix (optional) to limit the search to a specific folder
    prefix = 'your-folder-prefix/'  # Optional, use None if no prefix filtering is needed
    
    # List the deleted files (delete markers)
    deleted_files = list_deleted_files(bucket_name, prefix)

    if deleted_files:
        print(f"Found {len(deleted_files)} deleted files:")
        for file in deleted_files:
            print(f"File: {file['Key']}, Version: {file['VersionId']}, Deleted on: {file['LastModified']}")
        
        # Recover each deleted file by its version
        for file in deleted_files:
            restore_deleted_file(bucket_name, file['Key'], file['VersionId'])
    else:
        print("No deleted files found.")

if __name__ == "__main__":
    main()
