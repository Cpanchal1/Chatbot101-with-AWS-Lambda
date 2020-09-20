# This script will perform the following actions:
#   1. GET a joke from the icanhazdadjoke database of jokes.
#   2. POST the joke to the relevant Webex Teams Room

import requests
import json

ROOMID = "Y2lzY29zcGFyazovL3VzL1JPT00vNTEzOGViNTAtZjgyMy0xMWVhLWJkNzUtYjE1MjlhODIyMzkx"
TOKEN = "Bearer YTBmOTQwOGYtY2JiNC00ODkwLThlYWQtMTI5ZjcxZGRkYTMwNWY2OTEwNjgtMDZm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

#Step 1: GET joke from icanhazdadjoke database
def getJoke():
    print("\n ...Starting getJoke function... \n")
    
    url = "https://icanhazdadjoke.com"
    headers = {
        "Accept":"application/json"
    }
    
    response = requests.request("GET", url=url, headers=headers)
    return response.json()["joke"]


#Step 2: POST that joke to Webex Teams Room
def postJoke(joke):
    print("\n ...Starting postJoke function... \n")
    
    url = "https://api.ciscospark.com/v1/messages"
    headers = {
        "Authorization": TOKEN,  # Bot's access token
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": ROOMID,
        "text": joke
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)


def main(event, context):
    print("\n ...Starting main function... \n")
    joke = getJoke()
    postJoke(joke)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success, joke has been sent!')
    }