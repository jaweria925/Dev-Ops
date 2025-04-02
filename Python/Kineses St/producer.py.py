import json
import datetime
import boto3

# initialize client

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')


# define handler
def lambda_handler(event, context):

    try:
        # get bucket and object key
        print("Full Event: ", json.dumps(event, indent=2))  # Log the event

    # Check if 'Records' exists
        if 'Records' not in event:
            print("Error: 'Records' key is missing from the event")
            return {
                "statusCode": 400,
                "body": "Invalid event format: 'Records' key is missing"
            }
        
        # If 'Records' exists, proceed
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        return {
            "statusCode": 200,
            "body": f"File {key} from {bucket} processed successfully."
        }
        # get object
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')


        # generate payload for kinesis
        payload = {
            "data": content
        }

        # send data to kinesis
        send = send_to_kinesis(payload, key_name)
        print(send)

    except Exception as e:
        print(e)
        raise e 

    # fucntion to send data to kinesis
    def send_to_kinesis(payload, key_name):
        try:
            response = kineses.put_record(
                StreamName='kgl09876',
                Data=json.dumps(payload),
                PartitionKey=key_name
            )
            return f"Data sent to kinesis: {response}"
        except Exception as e:
            print(f"Error sending data to kinesis: {e}")
            raise e

        
        
        
