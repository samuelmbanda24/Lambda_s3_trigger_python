import json

def lambda_handler(event, context):
    # TODO implement
 
    data=event["Records"]
    bucket=(data[0]["s3"]["bucket"]["name"])
    file=(data[0]["s3"]["object"]["key"])
    ip_address=(data[0]["requestParameters"]["sourceIPAddress"])
    arn=(data[0]["s3"]["bucket"]["arn"])
    print(f"bucket_name is {bucket} & file_name is {file} & IP is {ip_address} & arn is {arn}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
