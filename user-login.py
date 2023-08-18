import json
import boto3

def lambda_handler(event, context):
    # Extract username and password from the event
    login_data = json.loads(event['body'])
    username = login_data['username']
    password = login_data['password']

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')

    # Retrieve the user from DynamoDB
    response = table.get_item(Key={'name': username})

    # Check if the user exists and the password matches
    if 'Item' in response and response['Item'].get('password') == password:
        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Login successful'})
        }
    else:
        # Return a failure response
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Invalid credentials'})
        }
