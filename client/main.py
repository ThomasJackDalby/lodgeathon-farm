# python requests client


import requests


requests.post("http://localhost:8000/farmers", json={"name" : "Tom", "token" : "abcde"})