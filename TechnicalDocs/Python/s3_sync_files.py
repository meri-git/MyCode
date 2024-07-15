import boto3
import logging
import os
from datetime import datetime
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging
log_file = 's3_sync_log.txt'
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', handlers=[logging.FileHandler(log_file), logging.StreamHandler()])
logger = logging.getLogger()

def sync_files(source_bucket, destination_bucket):
    s3 = boto3.resource('s3')
    source_bucket_obj = s3.Bucket(source_bucket)
    destination_bucket_obj = s3.Bucket(destination_bucket)

    try:
        for obj in source_bucket_obj.objects.all():
            source_key = obj.key
            destination_key = obj.key

            source_obj = source_bucket_obj.Object(source_key)
            destination_obj = destination_bucket_obj.Object(destination_key)

            source_etag = source_obj.e_tag
            try:
                destination_etag = destination_obj.e_tag
            except Exception:
                destination_etag = None

            if source_etag != destination_etag:
                # Copy the file to the destination bucket
                copy_source = {
                    'Bucket': source_bucket,
                    'Key': source_key
                }
                destination_bucket_obj.copy(copy_source, destination_key)
                logger.info(f'Copied {source_key} to {destination_bucket}')

    except NoCredentialsError:
        logger.error('Credentials not available')
    except PartialCredentialsError:
        logger.error('Incomplete credentials')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == "__main__":
    source_bucket = 'your-source-bucket-name'
    destination_bucket = 'your-destination-bucket-name'
    sync_files(source_bucket, destination_bucket)
