import boto3


endpoint_url = "http://localhost.localstack.cloud:4566"
# alternatively, to use HTTPS endpoint on port 443:
# endpoint_url = "https://localhost.localstack.cloud"
QUEUE_NAME = "login-queue"

def main():
    sqs = boto3.resource("sqs", endpoint_url=endpoint_url, region_name='us-east-1')
    # print(sqs.__dict__)
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    print(queue.url)
    # print(queue.url)
    # for message in queue.receive_messages():
    #     print(message)
    # print(result)

if __name__ == "__main__":
    main()

#
# while True:
#     sqs = boto3.client('sqs')
#     sql.read()



