import boto3
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("csv")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    Students = data.split("\n")
    #print(students)
    for stud in Students:
        print(stud)
        stud_data = stud.split(",")
        # add to dynamodb
        try:
            table.put_item(
                Item = {
                    "author"    : stud_data[0],
                    "type"      : stud_data[1],
                    "label"     : stud_data[2],
                    "information": stud_data[3]
                  
                }
            )
        except Exception as e:
            print("End of file")
