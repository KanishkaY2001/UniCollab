import sys
import datetime

'''Given a list of group objects and the current user object, sorts the groups in
terms of availability compatibilities (in terms of percentage of group's meetings the
user can attend)'''
def sortGroupByAvailabilities(groups, user):
    sortedGroups = []

    # Convert the user's calendar to date time objects
    userDateTimes = []
    for event in user['calendar']:
        date_time_start = datetime.datetime.strptime(event['start'], '%Y-%m-%dT%H:%M:%SZ')
        date_time_end = datetime.datetime.strptime(event['end'], '%Y-%m-%dT%H:%M:%SZ')
        userDateTimes.append({
            "name": event['name'],
            "start": date_time_start,
            "end": date_time_end
        })

    for group in groups:
        nMeetings = 0
        nAvailable = 0
        for meeting in group['preferredMeetingTimes']:
            nMeetings += 1

            date_time_start = datetime.datetime.strptime(meeting['start'], '%Y-%m-%dT%H:%M:%SZ')
            date_time_end = datetime.datetime.strptime(meeting['end'], '%Y-%m-%dT%H:%M:%SZ')
            

            # Check if any of the user's times clash with this
            available = True
            for time in userDateTimes:
                if not ((time['start'] < date_time_start and time['end'] <= date_time_start) or (date_time_end <= time['start'])):
                    # They are not free at this time
                    #print(f"You are not available for {group['name']} {meeting['name']} because of {time['name']}")
                    available = False        
                    break
            
            if available == True:
                nAvailable += 1

        if nMeetings != 0:
            percentageAvailable = nAvailable / nMeetings
        else :
            percentageAvailable = 1

        matchedScore = 0
        if percentageAvailable >= 0.6:
            matchedScore = 1
        if percentageAvailable >= 0.9:
            matchedScore = 2

        print(f"You are available for {percentageAvailable} of {group['name']}'s meetings")
        group['score'] = percentageAvailable
        group['match'] = matchedScore
        sortedGroups.append(group)

    # Sort for groups with highest score first
    sortedGroups = sorted(sortedGroups, key=lambda k: k['score'], reverse=True)
    
    return sortedGroups

'''Given a list of user objects and the current group object, sorts the users in
terms of availability compatibilities (in terms of percentage of group's meetings the
user can attend)'''
def sortUserByAvailabilities(users, group):
    sortedUsers = []

    # Convert the group's preferred meeting times to date time objects
    groupPreferredMeetingTimes = []
    for event in group['preferredMeetingTimes']:
        date_time_start = datetime.datetime.strptime(event['start'], '%Y-%m-%dT%H:%M:%SZ')
        date_time_end = datetime.datetime.strptime(event['end'], '%Y-%m-%dT%H:%M:%SZ')
        groupPreferredMeetingTimes.append({
            "name": event['name'],
            "start": date_time_start,
            "end": date_time_end
        })

    for user in users:
        nMeetings = 0
        nAvailable = 0

        # Convert user's calendar to date time objects and check for clashes
        for event in user['calendar']:
            date_time_start = datetime.datetime.strptime(event['start'], '%Y-%m-%dT%H:%M:%SZ')
            date_time_end = datetime.datetime.strptime(event['end'], '%Y-%m-%dT%H:%M:%SZ')

            available = True
            for time in groupPreferredMeetingTimes:
                if not ((time['start'] < date_time_start and time['end'] <= date_time_start) or (date_time_end <= time['start'])):
                    available = False
                    break
            
            if available == True:
                nAvailable += 1
        if nMeetings != 0:
            percentageAvailable = nAvailable / nMeetings
        else :
            percentageAvailable = 1

        matchedScore = 0
        if percentageAvailable >= 0.6:
            matchedScore = 1
        if percentageAvailable >= 0.9:
            matchedScore = 2

        user['score'] = percentageAvailable
        user['match'] = matchedScore
        sortedUsers.append(user)

    # Sort for groups with highest score first
    sortedUsers = sorted(sortedUsers, key=lambda k: k['score'], reverse=True)
    
    return sortedUsers




'''TEST DATA'''
user = {
    # And other data such as id, etc
    "calendar": [
        {
            "name": "Meeting Friends",
            "start": "2021-04-23 08:00",
            "end": "2021-04-23 09:30",
        },
        {
            "name": "Breakfast with family",
            "start": "2021-04-24 09:00",
            "end": "2021-04-24 10:30",
        },    
        {
            "name": "Social sport",
            "start": "2021-04-25 14:00",
            "end": "2021-04-25 17:30",
        },    
    ]
}

dummyGroups = [
    {
        "id": 7,
        "name": "Group 1",
        "preferredMeetingTimes": [
            {
                "name": "Weekly Meeting 1",
                "start": "2021-04-23 09:00",
                "end": "2021-04-23 10:00"
            },
            {
                "name": "Weekly Meeting 2",
                "start": "2021-04-26 15:00",
                "end": "2021-04-26 16:00"
            },
        ]
    },
    {
        "id": 8,
        "name": "Group 2",
        "preferredMeetingTimes": [
            {
                "name": "Introduction",
                "start": "2021-04-24 11:00",
                "end": "2021-04-24 13:00"
            },
            {
                "name": "Team bonding",
                "start": "2021-04-25 14:00",
                "end": "2021-04-25 15:30"
            },
        ]
    },
    {
        "id": 9,
        "name": "Group 3",
        "preferredMeetingTimes": [
            {
                "name": "Project outline",
                "start": "2021-04-25 09:00",
                "end": "2021-04-25 15:00"
            },
            {
                "name": "Uni brainstorm",
                "start": "2021-04-26 09:00",
                "end": "2021-04-26 15:00"
            },
            {
                "name": "Presentation",
                "start": "2021-04-27 09:00",
                "end": "2021-04-27 15:00"
            },
        ]
    },
    {
        "id": 10,
        "name": "Group 4",
        "preferredMeetingTimes": [
            {
                "name": "Trial run",
                "start": "2021-04-23 08:00",
                "end": "2021-04-23 11:00"
            }
        ]
    },
    {
        "id": 11,
        "name": "Group 5",
        "preferredMeetingTimes": [
            {
                "name": "Initial Meeting",
                "start": "2021-04-28 16:00",
                "end": "2021-04-28 19:00"
            }
        ]
    },
    {
        "id": 12,
        "name": "Group 6",
        "preferredMeetingTimes": [
            {
                "name": "Discussion Meeting",
                "start": "2021-04-25 08:00",
                "end": "2021-04-25 09:00"
            },
            {
                "name": "Brainstorm Meeting",
                "start": "2021-04-26 18:00",
                "end": "2021-04-26 19:00"
            },            
        ]
    }
]

#print(sortGroupByAvailabilities(dummyGroups, user))