#!/usr/bin/env python
from pprint import pprint
from Google import Create_Service
import sys
import datetime

# convert google calendar time to correct format
def correct_time_format(time, start_or_end):
    #convert 2020-12-27T13:00:00+11:00 to 2020-12-27T13:00:00
    counter = 19
    event_time_str = ''
    for char in time[start_or_end]['dateTime']:
        if counter == 0:
            break
        event_time_str += char
        counter -= 1
    return event_time_str

# find the finish time of a recurrence event
def recurrence_finish_time(time):
    #convert RRULE:FREQ=WEEKLY;UNTIL=20210507T170000Z to 20210507T170000
    counter = 0
    event_time_str = ''
    for char in time:
        if (counter < 39 and counter > 23):
            event_time_str += char
        counter += 1
    return event_time_str

# return next month with the same numbered day
def next_month(time):
    try:
        nextmonthdate = time.replace(month=time.month+1)
    except ValueError:
        if time.month == 12:
            nextmonthdate = time.replace(year=time.year+1, month=1)
    return nextmonthdate

def main():
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'calendar'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # search start time
    start_datetime = datetime.datetime.now()

    # search end time, 10 weeks after search start time
    end_datetime = start_datetime + datetime.timedelta(weeks=10)

    # store all events in an array
    event_array = []

    page_token = None
    # when no more events can found, loop ends
    while True:
        # get event list from google calendar
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()

        # for each event
        for event in events['items']:

            # call funtion
            start_time_str = correct_time_format(event, "start")
            end_time_str = correct_time_format(event, "end")

            # convert time string to time
            #                  module   class     method
            event_start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S')
            event_end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M:%S')

            # have timezone problem need to fix
            # but we can assume all time zone is sydney time

            # check if event is recurrence or not
            if ('recurrence' in event):
                
                # find event end time
                event_end_time = recurrence_finish_time(event['recurrence'][0])
                
                # monthly
                if (event_end_time[0] == '='):
    
                    # convert to time format
                    event_end_time_time_format = datetime.datetime.strptime(event_end_time, '=%Y%m%dT%H%M%S')
                    start_time = datetime.datetime.strptime(event['start']['dateTime'][0:19], '%Y-%m-%dT%H:%M:%S')
                    end_time = datetime.datetime.strptime(event['end']['dateTime'][0:19], '%Y-%m-%dT%H:%M:%S')

                    while True:
                        # find event append to event array
                        if (event_end_time_time_format >= start_datetime):
                            event_array.append({
                                "name":  event['summary'],
                                "event id": event['id'],
                                "start": str(start_time),
                                "end": str(end_time),
                                "recurrence": "monthly event",
                            })

                            # move to next event time 
                            start_time = next_month(start_time)
                            end_time = next_month(end_time)
            
                        # dont need events after 10 weeks
                        if (start_time > end_datetime):
                            break

                # weekly
                else:
                    # convert to time format
                    event_end_time_time_format = datetime.datetime.strptime(event_end_time, '%Y%m%dT%H%M%S')
                    start_time = datetime.datetime.strptime(event['start']['dateTime'][0:19], '%Y-%m-%dT%H:%M:%S')
                    end_time = datetime.datetime.strptime(event['end']['dateTime'][0:19], '%Y-%m-%dT%H:%M:%S')

                    while True:

                        # find event append to event array
                        if (event_end_time_time_format >= start_datetime):
                            event_array.append({
                                "name":  event['summary'],
                                "event id": event['id'],
                                "start": str(start_time),
                                "end": str(end_time),
                                "recurrence": "weekly event",
                            })

                            # move to next event time 
                            start_time += datetime.timedelta(days=7)
                            end_time += datetime.timedelta(days=7)
                        
                        # dont need events after 10 weeks
                        if (start_time > end_datetime):
                            break

            else:
                # check event still going after our search time    
                if (event_end_time >= start_datetime):
                    event_array.append({
                        "name":  event['summary'],
                        "event id": event['id'],
                        "start": event['start']['dateTime'],
                        "end": event['end']['dateTime'],
                        "recurrence": "one time event"
                    })

            # find next event
            page_token = events.get('nextPageToken')

    # when no more events can found
        if not page_token:
            break

    # print("--------\n")
    # # print events inside event_array
    # for event in event_array:
    #     print(event)

    # # print event_array
    # print("------------")
    # print(event_array)


    # return event_array
    print(event_array)
    return event_array

if __name__ == "__main__":
    main()
