import requests
import discord

API_URL = "https://canvas.uw.edu"
API_KEY = "10~xLbBIb7Mw9HOU5ce3ihhXTl2A8nLHqEbppHxfZnsGO2zda3IwtES54Sx1qStOHwy"
headers = {'Authorization': 'Bearer %s' % API_KEY}

upcoming_events = requests.get("https://canvas.uw.edu/api/v1/users/self/upcoming_events", headers=headers).json()
for event in upcoming_events:
    print(event["title"])