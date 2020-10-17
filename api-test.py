from canvasapi import Canvas
import discord

API_URL = "https://canvas.uw.edu/"
API_KEY = "10~xLbBIb7Mw9HOU5ce3ihhXTl2A8nLHqEbppHxfZnsGO2zda3IwtES54Sx1qStOHwy"

canvas = Canvas(API_URL, API_KEY)
user = canvas.get_user("self")
user_calendar = user.get_calendar_events_for_user()

for calendar in user_calendar:
    print(calendar)
#10~xLbBIb7Mw9HOU5ce3ihhXTl2A8nLHqEbppHxfZnsGO2zda3IwtES54Sx1qStOHwy
