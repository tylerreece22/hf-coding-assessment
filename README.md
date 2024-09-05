# HF Code Assessment
The purpose of this repo is to test your ability in the HF environment. This is a mocked repo
similar to what you may run into on the HF client.

## Context 
This is a AWS lambda monorepo. There is a single lambda function in `get_bad_actor_assessment.py`.
The idea of this assessment is to create high quality code which determines if a user is a "bad actor".
Follow the instructions starting in [get_bad_actor_assessment.py](lambdas%2Fget_bad_actor_assessment%2Fget_bad_actor_assessment.py).
You will not have an environment to test this in so you will need to complete a "best effort" approach only
using tests. There is an example `get_users` response in `tests/resources` you can use for your tests.

**To complete this assessment you will need to** 
- Write functional code
- Write tests reinforcing them
- And include types along the way

## Getting started
- Install [poetry](https://python-poetry.org/)
- Run `poetry shell`
- Run `poetry install`