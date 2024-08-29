import json
import boto3

mytanscribe=boto3.client("transcribe",
aws_access_key_id = "your access key",
                        aws_secret_access_key = "your secret key",
                        region_name="ap-south-1"
                        )
def lambda_handler(event, context):
    # TODO implement
    print("hello these side pri")
    
    bucketname=event['Records'][0]['s3']['bucket']['name']
    
    filename=event['Records'][0]['s3']['object']['key']
    
    finalurl="s3://"+bucketname+"/"+filename
    
    print(finalurl)
    
    mytanscribe.start_transcription_job(
            TranscriptionJobName='myjob123',
            LanguageCode="en-US",
            MediaFormat='mp3',
            Media={
                'MediaFileUri': finalurl
                
            },
            OutputBucketName='mybucket-s3-lambda-transcribe-output9399',#replace your  output bucket name
            OutputKey='myfinaltranscribe.json',
        )
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
