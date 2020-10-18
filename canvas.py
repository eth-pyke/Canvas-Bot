import requests
import dateutil.parser
import time
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://canvas.uw.edu"
KEY = os.getenv('API_KEY')
headers = {'Authorization': 'Bearer %s' % KEY}

def getEvents():
    upcoming_events = requests.get("https://canvas.uw.edu/api/v1/users/self/upcoming_events", headers=headers).json()
    event = []
    for events in upcoming_events:
        date = dateutil.parser.parse(events['start_at'])
        event.append({
            'name': events['title'],
            'start_time': date.strftime("%m/%d/%y %I:%M%p")
        })
    return event

def getCourses():
    fav_courses = requests.get("https://canvas.uw.edu/api/v1/courses", headers=headers, params={'enrollment_state':'active', 'include':['term']}).json()
    result = []
    for course in fav_courses:
        if (course['term']['name'] == "Autumn 2020"):
            result.append(course['name'])
    return result