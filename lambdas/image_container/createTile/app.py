import json
import boto3
import uuid
import base64
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tiles')


def lambda_handler(event, context):
    '''
        lambda name: createTile
    '''
    post_data = base64.b64decode(event['body'])
    dict_str = post_data.decode("UTF-8")
    jsonUser = json.loads(dict_str)
    
    tile_id = str(uuid.uuid4())
    tile_number = jsonUser['id']
    instagram_link = jsonUser['instagramLink']
    twitter_link = jsonUser['twitterLink']
    website = jsonUser['website']
    img = jsonUser['img']
    buyer_name = jsonUser['buyerName']
    is_bought = jsonUser['isBought']
    email = jsonUser['email']
    
    try:
        table.put_item(Item={
            "tile_id": tile_id,
            "email": email,
            "tile_number": tile_number,
            "instagram_link": instagram_link,
            "twitter_link": twitter_link,
            "website": website,
            "img": img,
            "buyer_name": buyer_name,
            "is_bought": is_bought
        })
        
        print ("done")
        
        return {
            "statusCode": 200, 
            "message": "tile has been inserted",
            "body": {
                "email": email,
                "tile_number": tile_number
            }
        }
    
    except botocore.exceptions.ClientError as error: 
        print (error)
        return error

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
