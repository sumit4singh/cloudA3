# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/
# Reference from https://us-east-1.console.aws.amazon.com/secretsmanager/home?region=us-east-1#!/secret?name=assignment3DB

import boto3
import base64
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "assignment3DB"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session(
        aws_access_key_id="ASIARVAB6G2YZ5JVLNGZ",
        aws_secret_access_key="mwbzpJKWb0URU9N9dRHhKBfn+b7+i4huui5pExfs",
        aws_session_token="FwoGZXIvYXdzEO7//////////wEaDNUTQSuGd9FynVVF2iLAAawx1zlv4aJ/LhJm6WejGK7SacbAt2JyNMzv+4BPUvQRgiAgTOD5T4JJHCE+RIf89jw6SUpv3H125K7CJD2kNaBD5mACEoyRFC2i5E8Zx1NjcKmj/Lot9FVkVqhAB8IJVthRwQWI5I7y8V0PGfWwcV9w5XikB8/nCNYv8DRnwNLtJZA2OoaAYlsT1VUreHxnAWExCUtiyhlNQkEPNM/YC4IUH09+Pb76kl3dOQgbLDD1MiRRG3Nw9KfQ1T1EXPrQbSjvsPORBjIt0mVwIs4QXdGGmnx+TipqDZkA1VK9j86PqWL/xm35DZ6+1FMBnUK2KVWKgkla",
        region_name="us-east-1"
        )
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    # Your code goes here.
    return get_secret_value_response