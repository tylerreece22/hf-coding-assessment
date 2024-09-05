from typing import Dict

from aws_lambda_typing import context as context_, events


'''
TODO:

1. Get user from event query params
2. Get user from auth0
3. Perform risk assessment on the user
4. Responses: 
    - If riskRating is "low" send "green" back to the client
    - If riskRating is "medium" send "yellow" back to the client
    - If riskRating is "high" send "red" back to the client
'''
def lambda_handler(event: events.APIGatewayProxyEventV2, context: context_.Context) -> Dict[str, int]:
