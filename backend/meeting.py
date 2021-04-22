import requests
import smtplib

# IMPORTANT META DATA
api_key = 'AIzaSyAfy-gg_WXSvjhaDMlMS1T93vpevDrpmuc'
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"

# # ========== EXAMPLE USAGE ========== 
# # Address of current user
# you = "Townhall Station, Sydney"

# # Address of group
# group = "UNSW"

# # get response
# r = requests.get(url + "origins=" + you + "&destinations=" + group + "&key=" + api_key)

'''Given a list of group objects and the current user object, returns the list
of groups in sorted ascending order within the given distance'''
def sortGroupByDistance(groups, user):
    nearestGroups = []
    for group in groups:
        r = requests.get(url + "origins=" + user['location'] + "&destinations=" + group['location'] + "&key=" + api_key)
        res = r.json()
        if res['rows'][0]['elements'][0]['status'] == 'OK':
            distance = res['rows'][0]['elements'][0]['distance']['text']
            distance = float(distance.split(' ')[0])
            match = 0
            if 0 <= distance and distance < 10:
                match = 2
            elif distance <= 10 and distance < 30:
                match = 1
            else:
                match = 0
            group['distance'] = distance
            group['match'] = match
            nearestGroups.append(group)

    nearestGroups = sorted(nearestGroups, key=lambda k: k['distance'])

    return nearestGroups

'''Given a list of user objects and the current group object, returns the list of users
sorted in ascending order within the given distance'''
def sortUserByDistance(users, group):
    nearestUsers = []
    for user in users:
        r = requests.get(url + "origins=" + user['location'] + "&destinations=" + group['location'] + "&key=" + api_key)
        res = r.json()
        if res['rows'][0]['elements'][0]['status'] == 'OK':
            distance = res['rows'][0]['elements'][0]['distance']['text']
            distance = float(distance.split(' ')[0])
            match = 0
            if 0 <= distance and distance < 10:
                match = 2
            elif distance <= 10 and distance < 30:
                match = 1
            else:
                match = 0
            nearestUsers.append({
                "id": group['id'],
                "name": group['name'],
                "location": group['location'],
                "distance": distance,
                "match": match
            })

    nearestUsers = sorted(nearestUsers, key=lambda k: k['distance'])

    return nearestUsers





'''TEST DATA'''
user = {
    # And other data such as id, etc
    "location": "Townhall Station, Sydney"
}

groups = [
    {
        "id": 1,
        "name": "Group 1",
        "location": "Chatswood, Sydney"
    },
    {
        "id": 2,
        "name": "Group 2",
        "location": "Burwood, Sydney"
    },
    {
        "id": 3,
        "name": "Group 3",
        "location": "Ashfield, Sydney"
    },
    {
        "id": 4,
        "name": "Group 4",
        "location": "Blacktown, Sydney"
    },
    {
        "id": 5,
        "name": "Group 5",
        "location": "UNSW, Sydney"
    },
    {
        "id": 6,
        "name": "Group 6",
        "location": "Cabramatta, Sydney"
    }
]


print(sortGroupByDistance(groups, user))