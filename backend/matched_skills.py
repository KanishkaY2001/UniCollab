import json, re 

groupSkills = ["Programming", "C", "Data modelling", "Django", "Python", "SQLite"]
courses = ["COMP1511", "COMP1531"]

from courses.models import Course

def lookingfor(words, courses):
    skills = []
    #f = open("scrape.json", "rb")
    #data = json.load(f)

    for course in Course.objects.all():  
        if (course.name in courses):
            for word in words:
                match = re.search(r'[\s|\"]'+word+r'[\s|,|:|\"|\;]', course.info, re.IGNORECASE)
                if (match and word not in skills):
                    skills.append(word)
    #f.close()
    return skills

usersSkills = lookingfor(groupSkills, courses)