steps taken

$ git clone https://bitbucket.org/fetchrewards/data-engineering-take-home.git
$ cd data-engineering-take-home

$ python -m venv venv
$ source venv/bin/activate

$ git remote remove origin
$ git remote add origin https://github.com/ekand/fetch-data-engineering-take-home.git
$ git branch -M main
$ git push -u origin main

$ make pip-install

$ make start
got stuck

$ awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
ModuleNotFoundError: No module named 'awscli'

$ brew insatll aws

$ PWD=`pwd`
$ make start
got stuck...

$ brew install awscli

restarted mac

$ make start
it worked.


new terminal

$ source venv/bin/activate

$ awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
a message is received

$ psql -d postgres -U postgres  -p 5432 -h localhost -W
a table is present, named user_logins

:
