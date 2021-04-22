import sys
from meeting import sortGroupByDistance, sortUserByDistance
from skills import sortGroupBySkills, sortUserBySkills
from availability import sortGroupByAvailabilities, sortUserByAvailabilities
def sortOverallGroups(groups, user):
    sortedDistance = sortGroupByDistance(groups, user)
    sortedSkills = sortGroupBySkills(groups, user)
    sortedAvailabilities = sortGroupByAvailabilities(groups, user)

    # Get the total matched score for each group
    overallScore = {}

    sortedOverall = []

    for group in groups:
        overallScore[group['id']] = {
            'match': 0
        }

    for group in sortedDistance:
        overallScore[group['id']]['match'] += group['match']
    
    for group in sortedSkills:
        overallScore[group['id']]['match'] += group['match']

    for group in sortedAvailabilities:
        overallScore[group['id']]['match'] += group['match']
    
    for key in overallScore:
        sortedOverall.append({
            'id': key,
            'match': overallScore[key]['match']
        })

    sortedOverall = sorted(sortedOverall, key=lambda k: k['match'], reverse=True)
    return sortedOverall

def sortOverallUsers(users, group):
    sortedDistance = sortUserByDistance(users, group)
    sortedSkills = sortUserBySkills(users, group)
    sortedAvailabilities = sortGroupByAvailabilities(users, group)

    overallScore = {}

    sortedOverall = []

    for user in users:
        overallScore[user['id']] = {
            'match': 0
        }

    for user in sortedDistance:
        overallScore[user['id']]['match'] += user['match']
    
    for user in sortedSkills:
        overallScore[user['id']]['match'] += user['match']

    for user in sortedAvailabilities:
        overallScore[user['id']]['match'] += user['match']

    for key in overallScore:
        sortedOverall.append({
            'id': key,
            'match': overallScore[key]['match']
        })

    sortedOverall = sorted(sortedOverall, key=lambda k: k['match'], reverse=True)
    return sortedOverall






''' TESTING DATA '''
user = {
    "courses": ["COMP1511", "COMP1531"],
    "location": "Townhall Station, Sydney",
    "calendar": [
        {
            "name": "Meeting Friends",
            "start": "2021-04-12 08:00",
            "end": "2021-04-12 09:30",
        },
        {
            "name": "Eating with family",
            "start": "2021-04-13 09:00",
            "end": "2021-04-13 10:30",
        },    
        {
            "name": "Social sport",
            "start": "2021-04-14 14:00",
            "end": "2021-04-14 17:30",
        },    
    ]
}

groups = [
    {
        "id": 1,
        "name": "Group 1",
        "lookingForSkills": ["Python", "SQLite"],
        "hasSkills": ["Data Modelling", "Programming", "C"],
        "location": "Chatswood, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Weekly Meeting 1",
                "start": "2021-04-12 09:00",
                "end": "2021-04-12 10:00"
            },
            {
                "name": "Weekly Meeting 2",
                "start": "2021-04-15 15:00",
                "end": "2021-04-15 16:00"
            },
        ]
    },
    {
        "id": 2,
        "name": "Group 2",
        "lookingForSkills": ["User Interfaces", "Django", "C"],
        "hasSkills": ["Python", "Algorithms"],
        "location": "Burwood, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Introduction",
                "start": "2021-04-13 11:00",
                "end": "2021-04-13 13:00"
            },
            {
                "name": "Team bonding",
                "start": "2021-04-14 14:00",
                "end": "2021-04-14 15:30"
            },
        ]
    },
    {
        "id": 3,
        "name": "Group 3",
        "lookingForSkills": ["Text Processing", "Binary Search Trees", "Graphs", "Sorting"],
        "hasSkills": ["Heaps", "Balanced Search Trees"],
        "location": "Ashfield, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Project outline",
                "start": "2021-04-14 09:00",
                "end": "2021-04-14 15:00"
            },
            {
                "name": "Uni brainstorm",
                "start": "2021-04-15 09:00",
                "end": "2021-04-15 15:00"
            },
            {
                "name": "Presentation",
                "start": "2021-04-16 09:00",
                "end": "2021-04-16 15:00"
            },
        ]
    },
    {
        "id": 4,
        "name": "Group 4",
        "lookingForSkills": ["C"],
        "hasSkills": ["Data Modelling", "Programming", "C"],
        "location": "Blacktown, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Trial run",
                "start": "2021-04-12 08:00",
                "end": "2021-04-12 11:00"
            }
        ]
    },
    {
        "id": 5,
        "name": "Group 5",
        "lookingForSkills": ["Python", "C"],
        "hasSkills": ["Data Modelling", "Algorithms"],
        "location": "UNSW, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Test Meeting",
                "start": "2021-04-17 16:00",
                "end": "2021-04-17 19:00"
            }
        ]
    },
    {
        "id": 6,
        "name": "Group 6",
        "lookingForSkills": ["Java", "OOP"],
        "hasSkills": ["Shell", "Perl"],
        "location": "Cabramatta, Sydney",
        "preferredMeetingTimes": [
            {
                "name": "Discussion Meeting",
                "start": "2021-04-14 08:00",
                "end": "2021-04-14 09:00"
            },
            {
                "name": "Brainstorm Meeting",
                "start": "2021-04-15 18:00",
                "end": "2021-04-15 19:00"
            },            
        ]
    }
]


print(sortOverallGroups(groups, user))