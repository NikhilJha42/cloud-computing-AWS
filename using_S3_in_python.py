import boto3

class s3_python_commands():

    def __init__(self):
        s3 = boto3.client('s3')

    def make_bucket(bucket_name):
        location = {'LocationConstraint': 'eu-west-1'}
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    def upload_file(file_name, bucket, obj_name):
        with open(file_name, "rb") as f:
            s3.upload_fileobj(f, bucket, obj_name)

    def download_file(obj_name, bucket, file_name):
        s3.download_file(bucket, obj_name, file_name)

    def delete_file(file_name, bucket):
        s3.delete_object(Bucket=bucket, Key=file_name)

    def delete_bucket(bucket_name):
        s3.delete_bucket(Bucket=bucket_name)