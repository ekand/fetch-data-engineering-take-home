import boto3
import json
import psycopg2
from datetime import datetime
import time

import hashlib

from user import User


endpoint_url = "http://localhost.localstack.cloud:4566"
# alternatively, to use HTTPS endpoint on port 443:
# endpoint_url = "https://localhost.localstack.cloud"
QUEUE_NAME = "login-queue"

connection_string = "host=localhost port=5432 user=postgres password=postgres"

def main():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()

    sqs = boto3.resource("sqs", endpoint_url=endpoint_url, region_name='us-east-1')
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    print('queue url:', queue.url)

    i = 0
    while True:
        print('i:', i)
        i += 1
        received_message = None
        try:
            print('trying to receive message')
            received_message = queue.receive_messages()

        except:
            print('error receiving message')
        if received_message:

            user_details = None
            try:
                print('parsing json')
                user_details = json.loads(received_message[0].body)
            except:
                print('error parsing json')

            user = None
            try:
                user = User(user_id=user_details['user_id'],
                            app_version=user_details['app_version'][0],  # just take major app version
                            device_type=user_details['device_type'],
                            masked_ip=hashlib.sha256(user_details['ip'].encode()).hexdigest(),
                            locale=user_details['locale'],
                            masked_device_id=hashlib.sha256(user_details['device_id'].encode()).hexdigest(),
                            )
            except Exception as e:
                print('error parsing user:', e)

            try:
                print('writing to postgresql')
                now = datetime.now()
                query_sql = '\n'.join([f"insert into user_logins ",
                                       "("
                                       "user_id, device_type, masked_ip, masked_device_id, locale, app_version, "
                                       "create_date"
                                       ")"
                                       "VALUES (",
                                       f"'{user.user_id}', ",
                                       f"'{user.device_type}', ",
                                       f"'{user.masked_ip}', ",
                                       f"'{user.masked_device_id}', ",
                                       f"'{user.locale}', ",
                                       f"'{user.app_version}', ",
                                       f"'{now.isoformat()}'",
                                       ")",
                                       ';',
                                       ])
                print('query sql:', query_sql)
                cursor.execute(query_sql)
                connection.commit()
            except Exception as e:
                print('error writing to sql:', e)
        else:
            print('no message found, waiting 10 seconds')
            time.sleep(10)


if __name__ == "__main__":
    main()
