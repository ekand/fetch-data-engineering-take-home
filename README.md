# Fetch Rewards Take Home Challenge Solution

## Steps to run

- Follow the instructions in REAMDE-old.md for "Project Setup"
- run `pip install -r requirements.txt`
- run `python app/main.py`

## Commentary

### How would I deploy this application in production?

I would deploy it the only way I know how, which is to spin up an EC2 instance, ssh into it, clone the repo, and run `python app/main.py` from the root directory of the repository.

### What other components would I want to add to make this production ready?

I would like to add logging to replace the print statements, and refactor the code into functions.

### How can this application scale with a growing data set?

To scale this, it would need to be re-written to use async capabilities.

### How can PII be recovered later on?

In order to be able to recover PII, you would need to keep the following data in a secure location: the original PII data, as well as the corresponding hashed values.