#!/usr/bin/python
from pprint import pprint
from Google import Create_Service
import sys

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print("input name for event: ")
name = input()
print("wanna weekly recurrence event input \"yes\" else input \"no\": ")
user_recurrence = input()

start_datetime = "2021-04-26T15:00:00+10:00"
end_datetime = "2021-04-26T17:00:00+10:00"

if ("yes" == user_recurrence):

    event = {
        
        #event name
        'summary': name,

        #event location
        #'location': '800 Howard St., San Francisco, CA 94103',

        'description': 'A chance to hear more about Google\'s developer products.',

        #start time
        'start': {
        'dateTime': start_datetime,
        'timeZone': 'Australia/Sydney',
        },
        #end time
        'end': {
        # eg 2021-04-07T17:00:00+10:00 +10:00 is use to find sydneytime
        'dateTime': end_datetime,
        'timeZone': 'Australia/Sydney',
        },

            
        #make event recursive each week
        'recurrence': [
        'RRULE:FREQ=WEEKLY;UNTIL=20210807T170000Z'
        ],

        }
else:

    event = {

        #event name
        'summary': name,

        #event location
        #'location': '800 Howard St., San Francisco, CA 94103',

        'description': 'A chance to hear more about Google\'s developer products.',

        #start time
        'start': {
        'dateTime': start_datetime,
        'timeZone': 'Australia/Sydney',
        },
        #end time
        'end': {
        # eg 2021-04-07T17:00:00+10:00 +10:00 is use to find sydneytime
        'dateTime': end_datetime,
        'timeZone': 'Australia/Sydney',
        },

        }

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))
