import boto3
import json

dynamodb = boto3.resource('dynamodb')
table_name = 'csv'
primary_key = 'author'

def lambda_handler(event, context):
    # Retrieve the author from the query parameters
    author = event.get('queryStringParameters', {}).get('author')

    # If author is not provided, return an error response
    if not author:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'author parameter is missing in the request'})
        }

    # Retrieve the item from DynamoDB table
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={primary_key: author})
    item = response.get('Item')

    # If item is not found, return a not found response
    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': f'Item with author {author} not found'})
        }

    # Return the item data as a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
