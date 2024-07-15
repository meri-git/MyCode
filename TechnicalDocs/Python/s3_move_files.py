import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def move_files(source_bucket, destination_bucket):
    s3 = boto3.resource('s3')
    source_bucket_obj = s3.Bucket(source_bucket)
    destination_bucket_obj = s3.Bucket(destination_bucket)

    try:
        for obj in source_bucket_obj.objects.all():
            copy_source = {
                'Bucket': source_bucket,
                'Key': obj.key
            }
            # Copy the file to the destination bucket
            destination_bucket_obj.copy(copy_source, obj.key)
            logger.info(f'Copied {obj.key} to {destination_bucket}')

            # Delete the file from the source bucket
            obj.delete()
            logger.info(f'Deleted {obj.key} from {source_bucket}')

    except NoCredentialsError:
        logger.error('Credentials not available')
    except PartialCredentialsError:
        logger.error('Incomplete credentials')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == "__main__":
    source_bucket = 'your-source-bucket-name'
    destination_bucket = 'your-destination-bucket-name'
    move_files(source_bucket, destination_bucket)
