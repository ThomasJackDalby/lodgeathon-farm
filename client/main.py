# python requests client

import requests

URL = "http://localhost:8000"

FARMER_ID = 1
FARMER_TOKEN = "abcde"

def move(direction):
    requests.post(URL+"/farmers/"+str(FARMER_ID), json={
        "token" : FARMER_TOKEN,
        "commands" : [
            { 
                "type" : "move",
                "direction" : direction
            }
        ]
})

if __name__ == "__main__":
    move("left")