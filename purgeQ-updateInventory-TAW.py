import json
import boto3

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    print("Purging queue...")
    sqs.purge_queue(QueueUrl='https://sqs.us-east-2.amazonaws.com/569624437018/q-updateInventory-TAW')
    return {
        'statusCode': 200,
        'headers' : {
			'Access-Control-Allow-Origin' : '*'
		},
        'body': json.dumps("Purge request sent.")
    }
