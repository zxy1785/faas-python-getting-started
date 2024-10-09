def handler(event):
    print("Function was invoked with event: {}".format(event))
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }