# This script will perform the following actions:
#   1. GET a joke from the icanhazdadjoke database of jokes.
#   2. POST the joke to the relevant Webex Teams Room

import requests
import json

ROOMID = "insert-roomid-here"
TOKEN = "Bearer insert-bot-token-here"

#Step 1: GET joke from icanhazdadjoke database
def getJoke():

    url = "https://icanhazdadjoke.com"
    headers = {
        "Accept":"application/json"
    }
    
    response = requests.request("GET", url=url, headers=headers)
    return response.json()["joke"]


#Step 2: POST that joke to Webex Teams Room
def postJoke(joke):

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
    joke = getJoke()
    postJoke(joke)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Success, joke has been sent!')
    }
