import boto3
import json
import psycopg2
from datetime import datetime
from user import User

endpoint_url = "http://localhost.localstack.cloud:4566"
# alternatively, to use HTTPS endpoint on port 443:
# endpoint_url = "https://localhost.localstack.cloud"
QUEUE_NAME = "login-queue"

connection_string = "host=localhost port=5432 user=postgres password=postgres"
"""
psql -d postgres -U postgres  -p 5432 -h localhost -W
"""

def main():
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()

    sqs = boto3.resource("sqs", endpoint_url=endpoint_url, region_name='us-east-1')
    # print(sqs.__dict__)
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
    print(queue.url)
    # print(queue.url)
    foo = queue.receive_messages()
    user_details = json.loads(foo[0].body)
    user = User(user_id=user_details['user_id'],
                app_version=user_details['app_version'][0],  # just take major app version
                device_type=user_details['device_type'],
                masked_ip="####",  # "user_details['ip'],
                locale=user_details['locale'],
                masked_device_id="#####",  # user_details['device_id'],
                )
    now = datetime.now()
    """
INSERT INTO categories
(category_id, category_name)
VALUES
(150, 'Miscellaneous');"""

    """
    
CREATE TABLE IF NOT EXISTS user_logins(
    user_id             varchar(128),
    device_type         varchar(32),
    masked_ip           varchar(256),
    masked_device_id    varchar(256),
    locale              varchar(32),
    app_version         integer,
    create_date         date
);"""
    query_sql = '\n'.join([f"insert into user_logins ",
                           "(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)"
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
    print(query_sql)
    cursor.execute(query_sql)
    connection.commit()

    # psycopg2.write()
    pass
    # for message in queue.receive_messages():
    #     print(message)
    # print(result)

if __name__ == "__main__":
    main()

#
# while True:
#     sqs = boto3.client('sqs')
#     sql.read()



