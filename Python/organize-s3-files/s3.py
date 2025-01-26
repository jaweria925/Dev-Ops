import boto3
from datetime import datetime


current_date = datetime.today()


formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formated_date)


s3_client = boto3.client('s3')
bucket_name = 'python0985'

client_response = s3_client.client.list_objects_v2(Bucket=bucket_name)

get_content = client_response.get('Contents')

s3_objects_name_and_folder = [] #create an empty list to store the s3 objects name and folder
for item in get_content:
    s3_object_name = item.get['Key']

    s3_objects_name_and_folder.append(s3_object_name) #sent objects ino the empty list

folder_name = formated_date + "/"
print(folder_name)


if folder_name not in s3_objects_name_and_folder: # To check folder is exist or not if foler not exist run this commmand
    s3_client.put_object(Bucket=bucket_name, Key=folder_name)


for item in get_content:
    obj_creation_date = item.get('LastModified').strftime("%Y-%m-%D %H:%M:%S") + "/"
    object_name = item.get("Key")

    if obj_creation_date == folder_name and "/" not in object_name:
        s3_client.copy_object(Bucket=bucket_name, CopySource=bucket_name+"/"+object_name, Key=folder_name+object_name)


if obj_creation_date == folder_name and "/" not in object_name:
    s3_client.copy_object(Bucket=bucket_name, CopySource=bucket_name+"/"+object_name, Key=folder_name+object_name)
    s3_client.delete_object(Bucket=bucket_name, Key=object_name)


