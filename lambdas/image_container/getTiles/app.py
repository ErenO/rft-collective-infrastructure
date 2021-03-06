import json
import boto3
import requests
import base64
import botocore
from boto3.dynamodb.conditions import Key
from authlib.integrations.requests_client import OAuth2Session

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('tiles')
PRIMARY_COLUMN_NAME = "tile_id"
    
def get_tiles_info():
    '''
        params: tile_number
    '''
    try:
        response = users_table.scan(
            ProjectionExpression="email, tile_number, instagram_link, twitter_link, website, img, buyer_name, is_bought",
            FilterExpression=Key('tile_number').between(0, 2500)
        )
        print("response")
        print(response)
        if response['Count'] > 0:
            return response['Items']
        else:
            return None
    except Exception as e:
        return {
          
          "statusCode": 400,
          "Message": "Email scan query didn't work",
          "errorMessage": e
          
        }
    
def handler(event, context):
    '''
        getTiles 
    '''
    print("event")
    print(event)
    
    tiles_info = get_tiles_info()
    
    return {
        'statusCode': 200,
        'body': {
            "tiles": tiles_info
        }
    }