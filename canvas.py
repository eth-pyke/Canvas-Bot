import requests
import dateutil.parser
import time

API_URL = "https://canvas.uw.edu"
API_KEY = "10~xLbBIb7Mw9HOU5ce3ihhXTl2A8nLHqEbppHxfZnsGO2zda3IwtES54Sx1qStOHwy"
headers = {'Authorization': 'Bearer %s' % API_KEY}

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

print(getEvents())