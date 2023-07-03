import boto3

s3 = boto3.client('s3')

# Set the bucket name and prefix (optional)
bucket_name = 'ravi-testing-bucket'
prefix = 'input-data-files'

# Set the page size and start token (optional)
page_size = 1000
start_token = None

# Iterate over all object versions using pagination
while True:
    # Call the list_object_versions() method to get a page of object versions
    response = s3.list_object_versions(Bucket=bucket_name, Prefix=prefix, MaxKeys=page_size)
    
    # Process the object versions in the response
    for version in response['Versions']:
        print(version['Key'])
    
    # Check if there are more pages of object versions to retrieve
    if response['IsTruncated']:
        start_token = response['NextKeyMarker']
    else:
        break
