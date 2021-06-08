import json
import boto3
import uuid
import base64
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tiles')


def handler(event, context):
    '''
        lambda name: updateTile
    '''
    if isinstance(event['body'], str):
        post_data = base64.b64decode(event['body'])
        dict_str = post_data.decode("UTF-8")
        data = json.loads(dict_str)
    else:
        data = event['body']
    
    tile_id = str(uuid.uuid4())
    tile_number = data['id']
    instagram_link = data['instagramLink']
    twitter_link = data['twitterLink']
    website = data['website']
    img = data['img']
    buyer_name = data['buyerName']
    is_bought = data['isBought']
    email = data['email']
    
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
