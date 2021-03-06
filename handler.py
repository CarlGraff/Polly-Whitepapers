import json


def pdftotext(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your pdftotext function executed successfully!",
        "event": event
    }


def texttospeech(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your texttospeech function executed successfully!",
        "event": event
    }



def speechtopodcast(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your speechtopodcast function executed successfully!",
        "event": event
    }



def status(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    return {
        "message": "Go Serverless v1.0! Your status function executed successfully!",
        "event": event
    }

