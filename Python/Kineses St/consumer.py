import json
import base64


# intialize client 

kinesis = boto3.client('kinesis')


# define handler
 def func-handle(event, context):
    try:

        # get records from event
        for record in event['Records']:
            # decode base64 data
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')

            # parse json
            data = json.loads(payload)
            print(data)

    except Exception as e:
        print(f"Error: {e}")
        raise e


