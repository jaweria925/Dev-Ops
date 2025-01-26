import boto3
from datetime import datetime

# Get the current date and time
current_date = datetime.today()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_date)

# Initialize S3 client
s3_client = boto3.client('s3')
bucket_name = 'python0985'

# List objects in the bucket
client_response = s3_client.list_objects_v2(Bucket=bucket_name)
get_content = client_response.get('Contents', [])

# Create an empty list to store S3 object names
s3_objects_name_and_folder = [item.get('Key') for item in get_content]

# Create folder name based on the current date
folder_name = formatted_date + "/"
print("Folder name:", folder_name)

# Check if the folder exists; if not, create it
if folder_name not in s3_objects_name_and_folder:
    s3_client.put_object(Bucket=bucket_name, Key=folder_name)

# Process objects
for item in get_content:
    obj_creation_date = item.get('LastModified').strftime("%Y-%m-%d %H:%M:%S") + "/"
    object_name = item.get("Key")

    # Check if the object's creation date matches the folder name and is not a folder
    if obj_creation_date == folder_name and "/" not in object_name:
        # Copy the object into the folder
        copy_source = {'Bucket': bucket_name, 'Key': object_name}
        s3_client.copy_object(Bucket=bucket_name, CopySource=copy_source, Key=folder_name + object_name)

        # Delete the original object
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)

print("Operation completed successfully.")
