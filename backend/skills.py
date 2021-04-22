import sys
import re
import json

from courses.models import Course

'''Given a list of group objects and the current user object, sorts the groups in
terms of skill compatibilities (groups which match the user's skills.
Skill compatibilitiy is determined by how needed a user is by a group (lookingFor)
and how well the user already synergises with the group's existing 'We Have' skills.
Furthermore, the more times a keyword pops up in different courses, the more 'familiar'
a user is with that keyword and so, '''
def sortGroupBySkills(groups, user):
    #file = open("scrape.json", "r")
    #coursesInfo = json.load(file)
    sortedGroups = []
    for group in groups:
        # print(f"MATCHING FOR GROUP {group['name']}")
        lookingForMatched = {}
        hasMatched = {}
        for course in Course.objects.all():
            # A skill can only match once for each course to prevent repeated keywords
            # from affecting the stats
            lookingForMatchedSkills = []
            hasMatchedSkills = []

            if course in user.courses.all():
                # See if this user is what the group is looking for
                for skill in group['lookingFor']:
                    # print(f"LOOKING FOR {skill} in {course}")
                    match = re.search(r'[\s|\"]'+skill+r'[\s|,|:|\"|\;]', course.info, re.IGNORECASE)
                    if match and not skill in lookingForMatchedSkills:
                        if not skill in lookingForMatched:
                            lookingForMatched[skill] = 1
                        else:
                            lookingForMatched[skill] += 1
                
                # See if this group has existing synergies with the user
                for skill in group['weHave']:
                    # print(f"HAS {skill} in {course}")
                    match = re.search(r'[\s|\"]'+skill+r'[\s|,|:|\"|\;]', course.info, re.IGNORECASE)
                    if match and not skill in hasMatchedSkills:
                        if not skill in hasMatched:
                            hasMatched[skill] = 1
                        else:
                            hasMatched[skill] += 1
        
        # print(lookingForMatched)
        # print(hasMatched)
        # Determine the synergy the user has with this group
        synergyScore = 0

        # User having skills that the group is looking for is worth 1
        for skill, count in lookingForMatched.items():
            synergyScore += count

        # User having skills that the group already has is worth 0.3
        for skill, count in hasMatched.items():
            synergyScore += count * 0.5

        # print("FINISHED")
        
        matchScore = 0
        if synergyScore >= 1:
            matchScore = 1
        if synergyScore >= 3:
            matchScore = 2
        group['match'] = matchScore
        group['score'] = synergyScore
        sortedGroups.append(group)

    # Sort groups with highest synergy score first
    sortedGroups = sorted(sortedGroups, key=lambda k: k['score'], reverse=True)

    return sortedGroups

'''Given a list of user objects and the current group object, sorts the users in
terms of skill compatibilities. Skill compatibility is determined by how needed
that user is by the group and how well the user already synergises with the group's
existing 'We Have'. Basically same logic as above^ '''
def sortUserBySkills(users, group):
    file = open("scrape.json", "r")
    coursesInfo = json.load(file)
    sortedUsers = []
    for user in users:
        # print(f"MATCHING FOR USER {user['name']}")
        lookingForMatched = {}
        hasMatched = {}
        for course in coursesInfo:
            # A skill can only match once for each course to prevent repeated keywords
            # from affecting the stats
            lookingForMatchedSkills = []
            hasMatchedSkills = []

            if course in user['courses']:
                # See if this user is what the group is looking for
                for skill in group['lookingForSkills']:
                    # print(f"LOOKING FOR {skill} in {course}")
                    match = re.search(r'[\s|\"]'+skill+r'[\s|,|:|\"|\;]', coursesInfo[course], re.IGNORECASE)
                    if match and not skill in lookingForMatchedSkills:
                        if not skill in lookingForMatched:
                            lookingForMatched[skill] = 1
                        else:
                            lookingForMatched[skill] += 1
                
                # See if this group has existing synergies with the user
                for skill in group['hasSkills']:
                    # print(f"HAS {skill} in {course}")
                    match = re.search(r'[\s|\"]'+skill+r'[\s|,|:|\"|\;]', coursesInfo[course], re.IGNORECASE)
                    if match and not skill in hasMatchedSkills:
                        if not skill in hasMatched:
                            hasMatched[skill] = 1
                        else:
                            hasMatched[skill] += 1
        
        # print(lookingForMatched)
        # print(hasMatched)
        # Determine the synergy the user has with this group
        synergyScore = 0

        # User having skills that the group is looking for is worth 1
        for skill, count in lookingForMatched.items():
            synergyScore += count

        # User having skills that the group already has is worth 0.3
        for skill, count in hasMatched.items():
            synergyScore += count * 0.5

        # print("FINISHED")
        
        matchScore = 0
        if synergyScore >= 1:
            matchScore = 1
        if synergyScore >= 3:
            matchScore = 2

        sortedUsers.append({
            'id': user['id'],
            'score': synergyScore,
            'match': matchScore
        })

    # Sort groups with highest synergy score first
    sortedUsers = sorted(sortedUsers, key=lambda k: k['score'], reverse=True)

    return sortedUsers


'''TESTING DATA'''
user = {
    # And other data such as id, etc
    "courses": ["COMP1511", "COMP1531"],
}

groups = [
    {
        "id": 1,
        "name": "Group 1",
        "lookingForSkills": ["Python", "SQLite"],
        "hasSkills": ["Data Modelling", "Programming", "C"]
    },
    {
        "id": 2,
        "name": "Group 2",
        "lookingForSkills": ["User Interfaces", "Django", "C"],
        "hasSkills": ["Python", "Algorithms"]
    },
    {
        "id": 3,
        "name": "Group 3",
        "lookingForSkills": ["Text Processing", "Binary Search Trees", "Graphs", "Sorting"],
        "hasSkills": ["Heaps", "Balanced Search Trees"]
    },
    {
        "id": 4,
        "name": "Group 4",
        "lookingForSkills": ["C"],
        "hasSkills": ["Data Modelling", "Programming", "C"]
    },
    {
        "id": 5,
        "name": "Group 5",
        "lookingForSkills": ["Python", "C"],
        "hasSkills": ["Data Modelling", "Algorithms"]
    },
    {
        "id": 6,
        "name": "Group 6",
        "lookingForSkills": ["Java", "OOP"],
        "hasSkills": ["Shell", "Perl"]
    }
]

#print(sortGroupBySkills(groups, user))