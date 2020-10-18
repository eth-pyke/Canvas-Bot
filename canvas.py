import requests
import os

API_URL = "https://canvas.uw.edu"
KEY = os.getenv('API_KEY')
headers = {'Authorization': 'Bearer %s' % KEY}

def getEvents():
    upcoming_events = requests.get("https://canvas.uw.edu/api/v1/users/self/upcoming_events", headers=headers).json()
    event = []
    for events in upcoming_events:
        event.append({
            'name': events['title'],
            'start_time': events['start_at']
        })
    return event

def getCourses():
    fav_courses = requests.get("https://canvas.uw.edu/api/v1/courses", headers=headers, params={'enrollment_state':'active', 'include':['term']}).json()
    result = []
    for course in fav_courses:
        if (course['term']['name'] == "Autumn 2020"):
            result.append(course['name'])
    return result
