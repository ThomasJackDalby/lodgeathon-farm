# python requests client

import requests

response = requests.post("http://localhost:8000/farmers/1", json={
    "token" : "abcde",
    "commands" : [
        { 
            "type" : "move",
            "direction" : "left"
        },
        { 
            "type" : "other",
            "stuff" : "what"
        }
    ]
})

print(response.json())