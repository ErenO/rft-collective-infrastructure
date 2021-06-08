import json
import boto3
import botocore
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tiles')
Primary_column_name = 'tile_id'

def handler(event, context):
    '''
        deleteTileInfo
    '''
    if isinstance(event['body'], str):
        post_data = base64.b64decode(event['body'])
        dict_str = post_data.decode("UTF-8")
        data = json.loads(dict_str)
    else:
        data = event['body']
    
    try:
        table.delete_item(
            Key={
                'tile_number': event['tile_number']
            }
        )
        return {"statusCode": 200, "message": "User has been deleted"}
    except botocore.exceptions.ClientError as error: 
        print (error)
        return error
        