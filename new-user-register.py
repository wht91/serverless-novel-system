import json
import boto3

def lambda_handler(event, context):
    # Extract user information from the event
    user_data = json.loads(event['body'])
    username = user_data['username']
    email = user_data['email']
    password = user_data['password']
    phone = user_data['phone']
    # Add any additional fields you require

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')

    # Put user information in the DynamoDB table
    table.put_item(Item={
        'name': username,
        'email': email,
        'password':password,
        'phone':phone
        # Add any additional fields you require
    })

    # Return a response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'User registration successful'})
    }
    return response
