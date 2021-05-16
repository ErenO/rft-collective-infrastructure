import json
import boto3
import requests
import base64
import botocore
from boto3.dynamodb.conditions import Key
from authlib.integrations.requests_client import OAuth2Session

NOTION_CLIENT_ID = 'f752b2cc-317c-4532-bec9-0376d23fb609'
NOTION_CLIENT_SECRET = 'secret_XYdM3l7VI3fRK4ewxd0ORTFEPwlx8oTyEpDN77mW90e'
NOTION_AUTH_URL = 'https://api.notion.com/v1/oauth/authorize'
NOTION_TOKEN_URL = 'https://api.notion.com/v1/oauth/token'
NOTION_REDIRECT_URI = 'http://localhost:3000/callback/notion'

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('users')
PRIMARY_COLUMN_NAME = "user_id"

    
def get_user_info(email):
    '''
        params: email(str)
    '''
    
    print(f"get_user_info, email: {email}")
    try:
        response = users_table.scan(
            ProjectionExpression="user_id",
            FilterExpression=Key('email').eq(email)
        )
        print("response")
        print(response)
        if response['Count'] > 0:
            return response['Items'][0]['user_id']
        else:
            return None
    except Exception as e:
        return {
          
          "statusCode": 400,
          "Message": "Email scan query didn't work",
          "errorMessage": e
          
        }
    

def create_authorization_url():
    notion_session = OAuth2Session(NOTION_CLIENT_ID)
    return notion_session.create_authorization_url(NOTION_AUTH_URL, redirect_uri=NOTION_REDIRECT_URI)
    
    
def add_state_to_user(user_id, authorization_url, state):
    '''
        add state to user
    '''
    notion_info = {
        "authorization_info": {
            "authorization_url": authorization_url,
            "state": state
        }
    }
    
    try:
        response = users_table.update_item(
            Key={
                PRIMARY_COLUMN_NAME: user_id
            },
            UpdateExpression="set connected_app.notion=:o, connected=:c",
            ExpressionAttributeValues={
                ":o": notion_info,
                ":c": False
            },
            ReturnValues="UPDATED_NEW"
        )
        
        return response 
    
    except botocore.exceptions.ClientError as error: 
        print (error)
        return None
        
def handler(event, context):
    '''
        notion_api_authorization
    '''
    print("event")
    print(event)
    
    user_id = get_user_info(event['email'])
    authorization_url, state = create_authorization_url()
    res = add_state_to_user(user_id, authorization_url, state)
    print(f"response {res}")
    
    return {
        'statusCode': 200,
        'body': {
            "authorization_url": authorization_url,
            "state": state
        }
    }
